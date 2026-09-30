# -*- coding: utf-8 -*-
"""
حاسبة العمر الافتراضي - وقود صلب مزدوج الأساس
معايرة ببيانات تقادم معجل حقيقية (HELL FIRE Motor)
"""
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    trapz = np.trapezoid
except AttributeError:
    trapz = np.trapz

st.set_page_config(
    page_title="العمر الافتراضي - DB Propellant",
    page_icon="🚀",
    layout="wide"
)

R = 8.314
T_ref_K = 298.15  # 25°C

# ==================== CSS مخصص ====================
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
</style>
""", unsafe_allow_html=True)

st.title("🚀 حاسبة العمر الافتراضي - وقود مزدوج الأساس")
st.caption("معايرة ببيانات تقادم معجل | COMPOSITE MODIFIED DB | HELL FIRE Motor")

# ==================== الشريط الجانبي ====================
st.sidebar.header("🔧 معايير المادة (مستخرجة من بياناتك)")
Ea_kJ = st.sidebar.number_input(
    "طاقة التنشيط Ea (kJ/mol)",
    value=115.0, step=1.0,
    help="قيمة من الأدبيات للـ DB. عدّلها لو عندك بيانات أكثر"
)

A_arr = st.sidebar.number_input(
    "معامل Arrhenius A (1/day)",
    value=1.06e13, format="%.2e",
    help="مستخرج من بياناتك عند 65°C"
)

st.sidebar.header("📊 معيار الفشل")
criterion = st.sidebar.selectbox(
    "اختر الخاصية الحاكمة",
    [
        "تغير معامل يونج (%)",
        "تغير الصلابة Shore A (%)",
        "تغير الدفع الأقصى (%)"
    ]
)

threshold_pct = st.sidebar.number_input(
    "الحد المسموح (%)",
    value=20.0, step=1.0,
    help="القيمة النموذجية: 15-25% للـ DB"
)

st.sidebar.header("🌡️ ظروف التخزين")
T_storage_C = st.sidebar.number_input(
    "درجة حرارة التخزين (°C)",
    value=25.0, step=1.0
)

# ==================== القيم المرجعية ====================
REF = {
    "young_modulus": {"value": 15.26, "k_65": 0.087, "unit": "kg/cm²"},
    "shore_A":       {"value": 45.0,  "k_65": 0.057, "unit": "-"},
    "max_thrust":    {"value": 988.0, "k_65": 0.00207, "unit": "dan"},
}

# ==================== الحسابات ====================
Ea = Ea_kJ * 1000
T_storage_K = T_storage_C + 273.15

k_65 = A_arr * np.exp(-Ea / (R * 338.15))
k_ref = A_arr * np.exp(-Ea / (R * T_ref_K))
k_storage = A_arr * np.exp(-Ea / (R * T_storage_K))

AF = k_storage / k_ref

# ==================== العرض ====================
st.header("📊 المؤشرات الأساسية")

col1, col2, col3 = st.columns(3)
col1.metric("⚡ معامل التسريع AF", f"{AF:.2f}",
            help="مقارنة بالتخزين عند 25°C")
col2.metric("🌡️ معدل k عند التخزين", f"{k_storage:.4e} /day")
col3.metric("📅 k عند 25°C", f"{k_ref:.4e} /day")

# ==================== تحديد الخاصية ====================
prop_map = {
    "تغير معامل يونج (%)": ("young_modulus", 15.26),
    "تغير الصلابة Shore A (%)": ("shore_A", 45.0),
    "تغير الدفع الأقصى (%)": ("max_thrust", 988.0),
}
prop_key, prop_0 = prop_map[criterion]

# ==================== نموذج التدهور ====================
t_array = np.linspace(0, 365 * 30, 2000)
prop_array = prop_0 * (1 + k_storage * t_array)
threshold_value = prop_0 * (1 + threshold_pct / 100)

t_fail_idx = np.where(prop_array >= threshold_value)[0]
if len(t_fail_idx) > 0:
    t_fail_days = t_array[t_fail_idx[0]]
    t_fail_years = t_fail_days / 365
    life_found = True
else:
    t_fail_years = float('inf')
    life_found = False

# ==================== النتيجة ====================
st.header("⏳ العمر الافتراضي")

if life_found:
    st.markdown(f"""
    <div class="success-box">
        <h2 style="color: #155724; margin: 0;">
        🎯 العمر الافتراضي عند {T_storage_C:.1f}°C = {t_fail_years:.2f} سنة
        </h2>
        <p style="margin: 10px 0 0 0; color: #155724;">
        <b>معيار الفشل:</b> {criterion} ≥ {threshold_pct}%<br>
        <b>المدة بالأيام:</b> {t_fail_days:.0f} يوم
        </p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.warning("⚠️ الخاصية لم تصل لحد الفشل خلال 30 سنة")

# ==================== الرسم البياني ====================
st.header(f"📈 تطور {criterion}")

fig, ax = plt.subplots(figsize=(11, 5))
fig.patch.set_facecolor('#f5f7fa')
ax.set_facecolor('#ffffff')

ax.plot(t_array / 365, prop_array, 'b-', linewidth=2.5,
        label='القيمة عند التخزين')
ax.axhline(threshold_value, color='r', linestyle='--', linewidth=2,
           label=f'حد الفشل ({threshold_pct}% زيادة)')
if life_found:
    ax.axvline(t_fail_years, color='g', linestyle=':', linewidth=2.5,
               label=f'العمر = {t_fail_years:.1f} سنة')
    ax.scatter([t_fail_years], [threshold_value], s=200, c='red',
               zorder=5, marker='X')

ax.set_xlabel('الزمن (سنة)', fontsize=12)
ax.set_ylabel(f'{criterion}', fontsize=12)
ax.set_title(f'منحنى التقادم عند {T_storage_C:.1f}°C',
             fontsize=14, fontweight='bold')
ax.legend(loc='best', fontsize=10)
ax.grid(True, alpha=0.3)
st.pyplot(fig)

# ==================== جدول المقارنة ====================
st.header("🌡️ مقارنة العمر عند درجات حرارة مختلفة")

data = []
for T_C in [15, 20, 25, 30, 40, 50, 60]:
    T_K = T_C + 273.15
    k = A_arr * np.exp(-Ea / (R * T_K))
    t_years = (threshold_pct / 100) / k / 365
    AF_i = k / k_ref
    data.append({
        "الحرارة (°C)": f"{T_C}",
        "معامل التسريع": f"{AF_i:.2f}",
        "معدل k (/day)": f"{k:.4e}",
        "العمر (سنة)": f"{t_years:.2f}" if t_years < 100 else "> 100"
    })

st.dataframe(pd.DataFrame(data), use_container_width=True)

# ==================== بيانات الدراسة ====================
with st.expander("📋 عرض بيانات الدراسة الأصلية (65°C)"):
    df_display = pd.DataFrame({
        "الزمن (يوم)": [0, 10, 20, 35],
        "Young Modulus": [15.26, 17.05, 17.35, 17.83],
        "Yield Stress (kg/cm²)": [0.92, 1.10, 1.20, 1.10],
        "Max Strain (%)": [86.20, 79.50, 76.30, 88.40],
        "Shore A": [45, 46, 46, 47],
        "Max Thrust (dan)": [988, None, None, 1062],
    })
    st.dataframe(df_display, use_container_width=True)

# ==================== تحذير ====================
st.warning(
    "⚠️ **تنبيه:** النموذج معاير ببيانات تجريبية عند 65°C. "
    "القيم المعروضة تقديرية. يُنصح بإضافة بيانات من درجات حرارة "
    "أخرى (50، 60، 70°C) لتحسين دقة Ea."
)
