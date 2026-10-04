# -*- coding: utf-8 -*-
"""
منصة محاكاة اختبارات التقادم - محركات صاروخية صلبة
تدعم 5 أنواع من الوقود الصلب (DB, CMDB, Composite, NEPE, HTPE)
"""

from datetime import datetime
import re
from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# ============================================================
# إعدادات الصفحة (يجب أن تكون في البداية)
# ============================================================
st.set_page_config(
    page_title="منصة التقادم - وقود صلب",
    page_icon="🚀",
    layout="wide",
)

R = 8.314
T_ref_K = 298.15  # 25°C


# ============================================================
# دلالات مساعدة
# ============================================================
def has_valid_experimental_data(prop):
    """التحقق التلقائي إن النوع ده فيه بيانات تجريبية صالحة"""
    data = prop.get("experimental_data")
    if not data:
        return False
    for key, d in data.items():
        if isinstance(d, dict) and d.get("y") and len(d["y"]) >= 2:
            return True
    return False


def clean_text_for_pdf(text):
    """إزالة أي حروف عربية من النص لعدم دعمها المباشر في fpdf القياسية"""
    cleaned = re.sub(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+", "", text)
    return " ".join(cleaned.split()).strip()


# ============================================================
# قاعدة بيانات أنواع الوقود
# ============================================================
PROPELLANT_TYPES = {
    "CMDB - Composite Modified DB (وقودك)": {
        "name_ar": "مركب معدل ثنائي الأساس",
        "Ea_default": 125.0,
        "Ea_range": (110.0, 140.0),
        "aging_mechanism": "استهلاك المُثبِّت + أكسدة AP/Al",
        "stabilizers": "2-NDPA + مضادات أكسدة",
        "failure_criteria": [
            "زيادة معامل يونج 20%",
            "زيادة الدفع الأقصى 15%",
            "زيادة الصلابة Shore A 10%",
        ],
        "reference": "Asthana et al., Solid Propellant Chemistry",
        "k_exp_65C": 0.0048,
        "has_real_data": True,
        "experimental_data": {
            "young_modulus": {
                "label": "معامل يونج",
                "t": [0, 10, 20, 35],
                "y": [15.26, 17.05, 17.35, 17.83],
                "y0": 15.26,
                "unit": "kg/cm²",
            },
            "shore_A": {
                "label": "الصلابة Shore A",
                "t": [0, 10, 20, 35],
                "y": [45, 46, 46, 47],
                "y0": 45.0,
                "unit": "-",
            },
            "max_thrust": {
                "label": "الدفع الأقصى",
                "t": [0, 35],
                "y": [988, 1062],
                "y0": 988.0,
                "unit": "dan",
            },
        },
    },
    "DB - Double Base": {
        "name_ar": "ثنائي الأساس",
        "Ea_default": 115.0,
        "Ea_range": (100.0, 130.0),
        "aging_mechanism": "تحلل الإسترات النيتراتية → استهلاك المُثبِّت",
        "stabilizers": "2-NDPA, Ethyl Centralite, Akardite II",
        "failure_criteria": [
            "استهلاك 50% من المُثبِّت",
            "زيادة معامل يونج 20%",
            "زيادة الصلابة Shore A 10%",
        ],
        "reference": "NATO STO-MP-AVT-268 (2017)",
        "k_exp_65C": 0.0048,
        "has_real_data": False,
        "experimental_data": None,
    },
    "Composite - HTPB/AP": {
        "name_ar": "مركب HTPB/AP",
        "Ea_default": 90.0,
        "Ea_range": (80.0, 100.0),
        "aging_mechanism": "أكسدة الـ binder + تكوين روابط عرضية",
        "stabilizers": "مضادات أكسدة (Antioxidants)",
        "failure_criteria": [
            "انخفاض Elongation 30%",
            "زيادة الصلابة Shore A 15%",
            "زيادة معامل يونج 25%",
        ],
        "reference": "Shekhar, Prediction of Shelf Life (2014)",
        "k_exp_65C": 0.0035,
        "has_real_data": False,
        "experimental_data": None,
    },
    "NEPE - Nitrate Ester Plasticized": {
        "name_ar": "إستر نيتراتي ملدن",
        "Ea_default": 135.0,
        "Ea_range": (120.0, 150.0),
        "aging_mechanism": "تحلل الإسترات + هجرة plasticizer",
        "stabilizers": "مُثبِّتات خاصة",
        "failure_criteria": [
            "استهلاك 40% من المُثبِّت",
            "تغير معامل يونج 15%",
            "فقدان وزن 2%",
        ],
        "reference": "NATO STO-TR-AVT-171",
        "k_exp_65C": 0.0080,
        "has_real_data": False,
        "experimental_data": None,
    },
    "HTPE - High Performance": {
        "name_ar": "عالي الأداء",
        "Ea_default": 100.0,
        "Ea_range": (90.0, 110.0),
        "aging_mechanism": "أكسدة البوليمر",
        "stabilizers": "مضادات أكسدة",
        "failure_criteria": [
            "انخفاض Elongation 25%",
            "زيادة معامل يونج 20%",
        ],
        "reference": "Insensitive Munitions Program Reports",
        "k_exp_65C": 0.0040,
        "has_real_data": False,
        "experimental_data": None,
    },
}

# ============================================================
# CSS مخصص
# ============================================================
st.markdown(
    """
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
""",
    unsafe_allow_html=True,
)

st.title("🚀 منصة محاكاة اختبارات التقادم")
st.caption("وقود صاروخي صلب | 5 أنواع مدعومة | معايرة ببيانات تجريبية")

# ============================================================
# الشريط الجانبي: اختيار نوع الوقود
# ============================================================
st.sidebar.header("🔥 نوع الوقود")
propellant_key = st.sidebar.selectbox(
    "اختر نوع الوقود",
    list(PROPELLANT_TYPES.keys()),
)

prop = PROPELLANT_TYPES[propellant_key]

st.sidebar.markdown(f"""
**📌 معلومات النوع:**
- **الاسم بالعربي:** {prop['name_ar']}
- **آلية التقادم:** {prop['aging_mechanism']}
- **المُثبِّت:** {prop['stabilizers']}
- **المرجع:** {prop['reference']}
""")

# ============================================================
# اختيار الخاصية الحاكمة
# ============================================================
st.sidebar.header("🎯 الخاصية الحاكمة")

use_real_data = False
if prop["has_real_data"]:
    prop_options = {
        "معامل يونج": "young_modulus",
        "الصلابة Shore A": "shore_A",
        "الدفع الأقصى": "max_thrust",
    }
    use_real_data = st.sidebar.checkbox(
        "استخدام البيانات التجريبية (65°C)",
        value=True,
        help="لو فعلت، هتستخدم بياناتك الحقيقية. لو لأ، هتستخدم قيم أدبيات.",
        key="use_real_data_checkbox",
    )
else:
    prop_options = {
        "معامل يونج": "young_modulus",
        "الصلابة Shore A": "shore_A",
    }

prop_label = st.sidebar.selectbox("اختر الخاصية", list(prop_options.keys()))
prop_key = prop_options[prop_label]

# ============================================================
# إعدادات Ea و k
# ============================================================
st.sidebar.header("🌡️ طاقة التنشيط Ea")
Ea_min, Ea_max = prop["Ea_range"]
Ea_kJ = st.sidebar.slider(
    "Ea (kJ/mol)",
    min_value=float(Ea_min),
    max_value=float(Ea_max),
    value=float(prop["Ea_default"]),
    step=1.0,
    help=f"النطاق الموصى به: {Ea_min}-{Ea_max} kJ/mol",
)

# ============================================================
# معيار الفشل الظروف
# ============================================================
st.sidebar.header("⚠️ معيار الفشل")
criterion = st.sidebar.selectbox("اختر المعيار", prop["failure_criteria"])
threshold_pct = st.sidebar.slider(
    "النسبة المسموحة (%)",
    min_value=5.0,
    max_value=50.0,
    value=20.0,
    step=1.0,
)

st.sidebar.header("📦 ظروف التخزين")
T_storage_C = st.sidebar.number_input(
    "درجة حرارة التخزين (°C)", value=25.0, step=1.0
)

# ============================================================
# الحسابات
# ============================================================
Ea = Ea_kJ * 1000
T_storage_K = T_storage_C + 273.15
T_exp_C = 65.0
T_exp_K = T_exp_C + 273.15

# حساب k عند 65°C
if prop["has_real_data"] and use_real_data:
    d = prop["experimental_data"][prop_key]
    t = np.array(d["t"], dtype=float)
    y = np.array(d["y"], dtype=float)
    y0 = d["y0"]

    # مواءمة خطية أدق للانحدار y/y0 - 1 = k * t
    y_norm = (y / y0) - 1.0
    slope, _ = np.polyfit(t, y_norm, 1)
    k_obs = float(slope)
    data_source = "Experimental data (65°C)"
else:
    k_obs = prop["k_exp_65C"]
    data_source = f"Literature values ({prop['reference']})"

A_arr = k_obs / np.exp(-Ea / (R * T_exp_K))


def k_at(T_K):
    return A_arr * np.exp(-Ea / (R * T_K))


k_storage = k_at(T_storage_K)
k_ref = k_at(T_ref_K)
AF = k_storage / k_ref

# ============================================================
# عرض المعلومات والمؤشرات
# ============================================================
st.markdown(
    f"""
<div class="info-box">
<b>📌 معايرة النموذج:</b><br>
• <b>نوع الوقود:</b> {propellant_key}<br>
• <b>الخاصية:</b> {prop_label}<br>
• <b>مصدر البيانات:</b> {data_source}<br>
• <b>k عند 65°C:</b> {k_obs:.6f} /day → {k_obs*100:.4f}% يوميًا<br>
• <b>معامل Arrhenius A:</b> {A_arr:.4e} /day
</div>
""",
    unsafe_allow_html=True,
)

st.header("📊 المؤشرات الأساسية")
col1, col2, col3 = st.columns(3)
col1.metric("⚡ معامل التسريع AF", f"{AF:.3f}")
col2.metric("🌡️ k عند التخزين", f"{k_storage:.4e} /day")
col3.metric("📅 k عند 25°C", f"{k_ref:.4e} /day")

# ============================================================
# العمر الافتراضي
# ============================================================
st.header("⏳ العمر الافتراضي")
t_fail_days = (threshold_pct / 100) / k_storage
t_fail_years = t_fail_days / 365

st.markdown(
    f"""
<div class="success-box">
    <h2 style="color: #155724; margin: 0;">
    🎯 العمر عند {T_storage_C:.1f}°C = {t_fail_years:.2f} سنة
    </h2>
    <p style="margin: 10px 0 0 0; color: #155724;">
    <b>معيار الفشل:</b> {criterion}<br>
    <b>المدة بالأيام:</b> {t_fail_days:.0f} يوم
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# رسم التحقق (لو بيانات حقيقية)
# ============================================================
if has_valid_experimental_data(prop) and use_real_data:
    st.header("🔬 التحقق: النموذج مقابل البيانات التجريبية")
    d = prop["experimental_data"][prop_key]
    t_data = np.array(d["t"], dtype=float)
    y_data = np.array(d["y"], dtype=float)
    y0 = d["y0"]

    fig, ax = plt.subplots(figsize=(11, 4.5))
    fig.patch.set_facecolor("#f5f7fa")
    ax.set_facecolor("#ffffff")

    ax.scatter(
        t_data,
        y_data,
        s=120,
        c="red",
        zorder=5,
        label=f"بيانات تجريبية ({T_exp_C:.0f}°C)",
    )
    t_smooth = np.linspace(0, max(t_data) * 1.2, 100)
    y_smooth = y0 * (1 + k_obs * t_smooth)
    ax.plot(
        t_smooth,
        y_smooth,
        "b-",
        linewidth=2.5,
        label=f"النموذج عند {T_exp_C:.0f}°C",
    )

    ax.set_xlabel("الزمن (يوم)", fontsize=12)
    ax.set_ylabel(f'{d["label"]} ({d["unit"]})', fontsize=12)
    ax.set_title(
        f"مطابقة النموذج للبيانات عند {T_exp_C:.0f}°C",
        fontsize=13,
        fontweight="bold",
    )
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

# ============================================================
# رسم تطور الخاصية عند التخزين
# ============================================================
st.header(f"📈 تطور {prop_label} عند {T_storage_C:.0f}°C")

if has_valid_experimental_data(prop) and use_real_data:
    y0_display = prop["experimental_data"][prop_key]["y0"]
    unit_display = prop["experimental_data"][prop_key]["unit"]
else:
    y0_display = 1.0
    unit_display = "قيمة نسبية"

fig2, ax2 = plt.subplots(figsize=(11, 5))
fig2.patch.set_facecolor("#f5f7fa")
ax2.set_facecolor("#ffffff")

t_arr = np.linspace(0, max(365 * 50, t_fail_days * 1.5), 2000)
y_arr = y0_display * (1 + k_storage * t_arr)
threshold_val = y0_display * (1 + threshold_pct / 100)

ax2.plot(t_arr / 365, y_arr, "b-", linewidth=2.5, label="القيمة المتوقعة")
ax2.axhline(
    threshold_val,
    color="r",
    linestyle="--",
    linewidth=2,
    label=f"حد الفشل (+{threshold_pct:.0f}%)",
)

if t_fail_years < 50:
    ax2.axvline(
        t_fail_years,
        color="g",
        linestyle=":",
        linewidth=2.5,
        label=f"العمر = {t_fail_years:.2f} سنة",
    )
    ax2.scatter(
        [t_fail_years],
        [threshold_val],
        s=200,
        c="red",
        zorder=5,
        marker="X",
    )

ax2.set_xlabel("الزمن (سنة)", fontsize=12)
ax2.set_ylabel(f"{prop_label} ({unit_display})", fontsize=12)
ax2.set_title(
    f"منحنى التقادم عند {T_storage_C:.0f}°C", fontsize=13, fontweight="bold"
)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)
st.pyplot(fig2)

# ============================================================
# جدول المقارنة ومقارنة الأنواع
# ============================================================
st.header("🌡️ مقارنة العمر عند درجات حرارة مختلفة")
data = []
for T_C in [15, 20, 25, 30, 35, 40, 50, 60, 65]:
    T_K = T_C + 273.15
    k = k_at(T_K)
    t_y = (threshold_pct / 100) / k / 365
    AF_i = k / k_ref
    data.append({
        "الحرارة (°C)": f"{T_C}",
        "k (/day)": f"{k:.4e}",
        "معامل التسريع": f"{AF_i:.2f}",
        "العمر (سنة)": f"{t_y:.2f}" if t_y < 1000 else "> 1000",
    })
st.dataframe(pd.DataFrame(data), use_container_width=True)

st.header("🔥 مقارنة أنواع الوقود المختلفة")
comparison = []
for name, p in PROPELLANT_TYPES.items():
    k_65 = p["k_exp_65C"]
    A = k_65 / np.exp(-Ea / (R * T_exp_K))
    k_25 = A * np.exp(-Ea / (R * T_ref_K))
    life_25 = (threshold_pct / 100) / k_25 / 365
    comparison.append({
        "نوع الوقود": name.split(" - ")[0],
        "k عند 65°C": f"{k_65:.4e}",
        "Ea الافتراضي (kJ/mol)": f"{p['Ea_default']:.0f}",
        "العمر عند 25°C (سنة)": f"{life_25:.2f}" if life_25 < 1000 else "> 1000",
    })
st.dataframe(pd.DataFrame(comparison), use_container_width=True)

# ============================================================
# رفع بيانات CSV جديدة
# ============================================================
st.markdown("---")
st.header("📤 رفع بيانات تجريبية جديدة (CSV)")
uploaded_file = st.file_uploader("اختر ملف CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df_upload = pd.read_csv(uploaded_file)
        st.success("✅ تم رفع الملف بنجاح!")
        st.dataframe(df_upload, use_container_width=True)

        required_cols = ["temperature_C", "time_days"]
        if not all(col in df_upload.columns for col in required_cols):
            st.error(f"⚠️ الملف يجب أن يحتوي على الأعمدة: {required_cols}")
        else:
            property_cols = [
                c for c in df_upload.columns if c not in required_cols
            ]
            if property_cols:
                selected_prop = st.selectbox(
                    "اختر الخاصية للتحليل", property_cols
                )
                results = []
                for T in sorted(df_upload["temperature_C"].unique()):
                    sub = df_upload[df_upload["temperature_C"] == T].dropna(
                        subset=[selected_prop]
                    )
                    if len(sub) >= 2:
                        t_vals = sub["time_days"].values
                        y_vals = sub[selected_prop].values
                        y0 = y_vals[0]

                        # حساب المنحدر خطياً
                        slope, _ = np.polyfit(t_vals, (y_vals / y0) - 1.0, 1)
                        results.append({
                            "T_C": T,
                            "T_K": T + 273.15,
                            "k": slope,
                            "n_points": len(sub),
                            "y0": y0,
                        })

                results_df = pd.DataFrame(results)
                st.dataframe(results_df, use_container_width=True)

                if len(results_df) >= 3:
                    inv_T = 1 / results_df["T_K"].values
                    ln_k = np.log(np.abs(results_df["k"].values))
                    slope, intercept = np.polyfit(inv_T, ln_k, 1)
                    Ea_calc = -slope * R / 1000
                    A_calc = np.exp(intercept)

                    st.success(f"✅ طاقة التنشيط Ea = {Ea_calc:.2f} kJ/mol")

                    fig_a, ax_a = plt.subplots(figsize=(8, 4))
                    ax_a.scatter(inv_T * 1000, ln_k, color="red", s=100)
                    ax_a.plot(
                        inv_T * 1000, slope * inv_T + intercept, "b--"
                    )
                    ax_a.set_xlabel("1000/T (K⁻¹)")
                    ax_a.set_ylabel("ln(k)")
                    st.pyplot(fig_a)
    except Exception as e:
        st.error(f"❌ خطأ في معالجة الملف: {str(e)}")

# ============================================================
# تصدير تقرير PDF
# ============================================================
st.markdown("---")
st.header("📄 تصدير تقرير PDF")


def generate_pdf_report():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(
        0, 10, "Solid Rocket Motor - Aging Simulation Report", ln=True, align="C"
    )
    pdf.ln(5)

    pdf.set_font("Arial", "", 10)
    pdf.cell(
        0,
        6,
        f"Propellant: {clean_text_for_pdf(propellant_key).split('-')[0]}",
        ln=True,
    )
    pdf.cell(0, 6, f"Activation Energy (Ea): {Ea_kJ:.1f} kJ/mol", ln=True)
    pdf.cell(0, 6, f"Storage Temp: {T_storage_C:.1f} C", ln=True)
    pdf.cell(
        0,
        6,
        f"Estimated Life: {t_fail_years:.2f} years ({t_fail_days:.0f} days)",
        ln=True,
    )

    return pdf.output()


if st.button("📥 إنشاء التقرير PDF", type="primary"):
    try:
        pdf_bytes = generate_pdf_report()
        st.download_button(
            label="💾 تحميل التقرير PDF",
            data=bytes(pdf_bytes),
            file_name=f"aging_report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
            mime="application/pdf",
        )
    except Exception as e:
        st.error(f"❌ خطأ في إنشاء التقرير: {str(e)}")
