# -*- coding: utf-8 -*-
"""
حاسبة العمر الافتراضي - وقود صلب مزدوج الأساس
معايرة ببيانات تقادم معجل حقيقية (65°C - HELL FIRE Motor)
"""
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="العمر الافتراضي - DB Propellant",
    page_icon="🚀",
    layout="wide"
)

R = 8.314
T_ref_K = 298.15   # 25°C (مرجع المقارنة)
T_exp_C = 65.0     # درجة حرارة التجربة
T_exp_K = T_exp_C + 273.15

# ==================== بيانات تجربتك (65°C) ====================
EXP_DATA = {
    "young_modulus": {
        "name": "معامل يونج",
        "unit": "kg/cm²",
        "t": [0, 10, 20, 35],
        "y": [15.26, 17.05, 17.35, 17.83],
        "y0": 15.26,
    },
    "shore_A": {
        "name": "الصلابة Shore A",
        "unit": "-",
        "t": [0, 10, 20, 35],
        "y": [45, 46, 46, 47],
        "y0": 45.0,
    },
    "max_thrust": {
        "name": "الدفع الأقصى",
        "unit": "dan",
        "t": [0, 35],
        "y": [988, 1062],
        "y0": 988.0,
    },
}

# ==================== حساب k من البيانات ====================
def compute_k_from_data(prop_key):
    """حساب k (1/day) من البيانات عند 65°C بطريقة الانحدار"""
    d = EXP_DATA[prop_key]
    t = np.array(d["t"], dtype=float)
    y = np.array(d["y"], dtype=float)
    y0 = d["y0"]

    # نموذج: y = y0 * (1 + k * t)  →  k = (y/y0 - 1) / t
    with np.errstate(divide='ignore', invalid='ignore'):
        k_vals = (y / y0 - 1) / t
    k_vals = k_vals[~np.isnan(k_vals) & ~np.isinf(k_vals)]
    return float(np.mean(k_vals))


K_OBS = {key: compute_k_from_data(key) for key in EXP_DATA}

# ==================== CSS ====================
st.markdown("""
<style>
    .main { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
    h1 { color: #1e3a8a; text-align: center; }
    .stMetric {
        background: white; padding: 15px; border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .success-box {
        background: linear-gradient(90deg, #d4edda 0%, #c3e6cb 100%);
        padding: 20px; border-radius: 10px; border-right: 5px solid #28a745;
    }
    .info-box {
        background: #e7f3ff; padding: 15px; border-radius: 10px;
        border-right: 5px solid #0066cc;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚀 حاسبة العمر الافتراضي - وقود مزدوج الأساس")
st.caption("معايرة بنقطة واحدة | البيانات التجريبية عند 65°C | HELL FIRE Motor")

# ==================== الشريط الجانبي ====================
st.sidebar.header("🎯 الخاصية الحاكمة")
prop_label = st.sidebar.selectbox(
    "اختر الخاصية",
    ["معامل يونج (Young Modulus)", "الصلابة (Shore A)", "الدفع الأقصى (Max Thrust)"]
)
prop_map = {
    "معامل يونج (Young Modulus)": "young_modulus",
    "الصلابة (Shore A)": "shore_A",
    "الدفع الأقصى (Max Thrust)": "max_thrust",
}
prop_key = prop_map[prop_label]
prop_info = EXP_DATA[prop_key]

st.sidebar.header("🌡️ طاقة التنشيط Ea")
Ea_kJ = st.sidebar.slider(
    "Ea (kJ/mol)",
    min_value=70.0, max_value=130.0,
    value=90.0, step=1.0,
    help="90 kJ/mol قيمة نموذجية للـ DB. غيّرها لتشوف الحساسية."
)

st.sidebar.header("⚠️ معيار الفشل")
threshold_pct = st.sidebar.slider(
    "الحد المسموح (%)",
    min_value=5.0, max_value=50.0, value=20.0, step=1.0
)

st.sidebar.header("📦 ظروف التخزين")
T_storage_C = st.sidebar.number_input(
    "درجة حرارة التخزين (°C)",
    value=25.0, step=1.0
)

# ==================== الحسابات ====================
Ea = Ea_kJ * 1000
T_storage_K = T_storage_C + 273.15

# k المُشاهد عند 65°C من بياناتك
k_obs = K_OBS[prop_key]

# نحسب A من k المُشاهد عند 65°C
A_arr = k_obs / np.exp(-Ea / (R * T_exp_K))

# k عند أي درجة حرارة
def k_at(T_K):
    return A_arr * np.exp(-Ea / (R * T_K))

k_storage = k_at(T_storage_K)
k_ref = k_at(T_ref_K)

# معامل التسريع
AF = k_storage / k_ref

# ==================== عرض المعلومات ====================
st.markdown(f"""
<div class="info-box">
<b>📌 معايرة النموذج:</b><br>
• <b>الخاصية:</b> {prop_info['name']} ({prop_info['unit']})<br>
• <b>k عند 65°C (من بياناتك):</b> {k_obs:.6f} /day  →  {k_obs*100:.4f}% يوميًا<br>
• <b>معامل Arrhenius A:</b> {A_arr:.4e} /day
</div>
""", unsafe_allow_html=True)

# ==================== المؤشرات ====================
st.header("📊 المؤشرات الأساسية")

col1, col2, col3 = st.columns(3)
col1.metric("⚡ معامل التسريع AF", f"{AF:.3f}",
            help=f"مقارنة بالتخزين عند 25°C")
col2.metric("🌡️ k عند التخزين", f"{k_storage:.4e} /day")
col3.metric("📅 k عند 25°C", f"{k_ref:.4e} /day")

# ==================== العمر الافتراضي ====================
st.header("⏳ العمر الافتراضي")

# t_fail = (threshold/100) / k   (من المعادلة y/y0 - 1 = k*t)
t_fail_days = (threshold_pct / 100) / k_storage
t_fail_years = t_fail_days / 365

st.markdown(f"""
<div class="success-box">
    <h2 style="color: #155724; margin: 0;">
    🎯 العمر عند {T_storage_C:.1f}°C = {t_fail_years:.2f} سنة
    </h2>
    <p style="margin: 10px 0 0 0; color: #155724;">
    <b>معيار الفشل:</b> زيادة {prop_info['name']} بنسبة {threshold_pct:.0f}%<br>
    <b>المدة بالأيام:</b> {t_fail_days:.0f} يوم
    </p>
</div>
""", unsafe_allow_html=True)

# ==================== الرسم 1: مطابقة النموذج مع البيانات ====================
st.header("🔬 التحقق: النموذج مقابل البيانات التجريبية")

fig, ax = plt.subplots(figsize=(11, 4.5))
fig.patch.set_facecolor('#f5f7fa')
ax.set_facecolor('#ffffff')

# البيانات التجريبية
ax.scatter(prop_info["t"], prop_info["y"], s=120, c='red', zorder=5,
           label=f'بيانات تجريبية ({T_exp_C:.0f}°C)')

# المنحنى النظري عند 65°C
t_smooth = np.linspace(0, max(prop_info["t"]) * 1.2, 100)
y_smooth = prop_info["y0"] * (1 + k_obs * t_smooth)
ax.plot(t_smooth, y_smooth, 'b-', linewidth=2.5,
        label=f'النموذج عند {T_exp_C:.0f}°C')

ax.set_xlabel('الزمن (يوم)', fontsize=12)
ax.set_ylabel(f'{prop_info["name"]} ({prop_info["unit"]})', fontsize=12)
ax.set_title(f'مطابقة النموذج للبيانات عند {T_exp_C:.0f}°C', fontsize=13, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
st.pyplot(fig)

st.caption(
    f"✅ النموذج مضبوط تلقائيًا على بياناتك. "
    f"الخط الأزرق يمثل المعادلة y = y0(1 + k·t) مع k = {k_obs:.6f}/day"
)

# ==================== الرسم 2: تطور الخاصية عند التخزين ====================
st.header(f"📈 تطور {prop_info['name']} عند {T_storage_C:.0f}°C")

fig2, ax2 = plt.subplots(figsize=(11, 5))
fig2.patch.set_facecolor('#f5f7fa')
ax2.set_facecolor('#ffffff')

t_arr = np.linspace(0, max(365 * 50, t_fail_days * 1.5), 2000)
y_arr = prop_info["y0"] * (1 + k_storage * t_arr)
threshold_val = prop_info["y0"] * (1 + threshold_pct / 100)

ax2.plot(t_arr / 365, y_arr, 'b-', linewidth=2.5, label='القيمة المتوقعة')
ax2.axhline(threshold_val, color='r', linestyle='--', linewidth=2,
            label=f'حد الفشل (+{threshold_pct:.0f}%)')

if t_fail_years < 50:
    ax2.axvline(t_fail_years, color='g', linestyle=':', linewidth=2.5,
                label=f'العمر = {t_fail_years:.2f} سنة')
    ax2.scatter([t_fail_years], [threshold_val], s=200, c='red',
                zorder=5, marker='X')

ax2.set_xlabel('الزمن (سنة)', fontsize=12)
ax2.set_ylabel(f'{prop_info["name"]} ({prop_info["unit"]})', fontsize=12)
ax2.set_title(f'منحنى التقادم عند {T_storage_C:.0f}°C', fontsize=13, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)
st.pyplot(fig2)

# ==================== جدول المقارنة ====================
st.header("🌡️ مقارنة العمر عند درجات حرارة مختلفة")

data = []
for T_C in [15, 20, 25, 30, 40, 50, 60, 65]:
    T_K = T_C + 273.15
    k = k_at(T_K)
    t_y = (threshold_pct / 100) / k / 365
    AF_i = k / k_ref
    data.append({
        "الحرارة (°C)": f"{T_C}",
        "k (/day)": f"{k:.4e}",
        "معامل التسريع": f"{AF_i:.2f}",
        "العمر (سنة)": f"{t_y:.2f}" if t_y < 1000 else "> 1000"
    })

st.dataframe(pd.DataFrame(data), use_container_width=True)

# ==================== تحذير ====================
st.warning(
    f"⚠️ **تنبيه:** النموذج معاير بنقطة واحدة (65°C) باستخدام Ea = {Ea_kJ:.0f} kJ/mol. "
    "لتقليل عدم اليقين، يُنصح بإضافة بيانات من درجات حرارة أخرى (50°C و 70°C مثلاً) "
    "لإجراء تحليل Arrhenius كامل."
)
