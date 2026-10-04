# ============================================================
# قاموس الترجمات (Translations Dictionary)
# ============================================================
TRANSLATIONS = {
    "ar": {
        "title": "🚀 منصة محاكاة اختبارات التقادم",
        "caption": "وقود صاروخي صلب | 5 أنواع مدعومة | معايرة ببيانات تجريبية",
        "propellant_type": "🔥 نوع الوقود",
        "select_propellant": t("select_propellant"),
        "prop_info": "📌 معلومات النوع",
        "governing_property": "🎯 الخاصية الحاكمة",
        "select_property": "اختر الخاصية",
        "use_exp_data": "استخدام البيانات التجريبية (65°C)",
        "ea_header": "🌡️ طاقة التنشيط Ea",
        "failure_criterion": "⚠️ معيار الفشل",
        "select_criterion": "اختر المعيار",
        "allowed_change": "النسبة المسموحة (%)",
        "storage_header": "📦 ظروف التخزين",
        "storage_temp": "درجة حرارة التخزين (°C)",
        "humidity_header": "💧 ظروف الرطوبة",
        "use_humidity": "تفعيل تأثير الرطوبة (Peck Model)",
        "rh_storage": "الرطوبة النسبية (%)",
        "rh_ref": "الرطوبة المرجعية (%)",
        "n_humidity": "معامل الرطوبة n",
        "results_header": "📊 النتائج",
        "af_label": "⚡ معامل التسريع AF",
        "k_storage": "🌡️ k عند التخزين",
        "k_ref": "📅 k عند 25°C",
        "life_header": "⏳ العمر الافتراضي",
        "life_years": "سنة",
        "life_days": "يوم",
        "failure_mode": "معيار الفشل",
        "duration_days": "المدة بالأيام",
        "not_failed": "⚠️ الخاصية لم تصل لحد الفشل خلال 30 سنة",
        "comparison_header": "🌡️ مقارنة العمر عند درجات حرارة مختلفة",
        "temperature": "الحرارة (°C)",
        "k_per_day": "k (/day)",
        "af_col": "معامل التسريع",
        "life_col": "العمر (سنة)",
        "pdf_header": "📄 تصدير تقرير PDF",
        "pdf_caption": "حمّل تقرير شامل يحتوي على كل النتائج والتحليلات",
        "pdf_generate": "📥 إنشاء التقرير PDF",
        "pdf_download": "💾 تحميل التقرير PDF",
        "csv_header": "📤 رفع بيانات تجريبية جديدة (CSV)",
        "csv_caption": "ارفع ملف CSV فيه بيانات التقادم المعجل لتحليلها فورًا",
        "csv_upload": "اختر ملف CSV",
        "csv_success": "✅ تم رفع الملف بنجاح!",
        "csv_data": "📋 البيانات المرفوعة",
        "csv_analysis": "🔬 تحليل البيانات",
        "select_property_analysis": "اختر الخاصية للتحليل",
        "arrhenius_plot": "Arrhenius Plot",
        "comparison_types": "⚔️ مقارنة تفصيلية بين نوعين من الوقود",
        "comparison_caption": "قارن بين نوعين: k، Ea، والعمر الافتراضي عند درجات حرارة مختلفة",
        "type_a": "النوع الأول (A)",
        "type_b": "النوع الثاني (B)",
        "compare_btn": "🔍 قارن الآن",
        "comparison_curve": "📈 منحنى العمر الافتراضي مقابل درجة الحرارة",
        "mc_header": "🎲 محاكاة Monte Carlo - التوزيع الاحتمالي",
        "mc_caption": "بدل رقم واحد، هتطلعلك عيّنة احتمالية للعمر بناءً على عدم اليقين",
        "mc_n_sim": "عدد مرات المحاكاة",
        "mc_ea_unc": "عدم اليقين في Ea (%)",
        "mc_k_unc": "عدم اليقين في k (%)",
        "mc_run": "🎲 تشغيل Monte Carlo",
        "mc_results": "📊 نتائج Monte Carlo",
        "mc_mean": "المتوسط",
        "mc_median": "الوسيط",
        "mc_p5": "P5 (تحفظي)",
        "mc_p95": "P95 (متفائل)",
        "years": "سنة",
        "abaqus_header": "🔧 تصدير البيانات لـ Abaqus",
        "abaqus_caption": "حمّل الملفات الجاهزة للتشغيل في برنامج Abaqus/CAE",
        "abaqus_inp": "📄 تحميل ملف INP",
        "abaqus_py": "🐍 تحميل سكريبت Python",
        "abaqus_csv": "📥 تحميل بيانات الإجهاد-الانفعال (CSV)",
        "abaqus_guide": "📖 دليل استخدام ملفات Abaqus",
        "language": "🌐 اللغة / Language",
    },
    "en": {
        "title": "🚀 Aging Simulation Platform",
        "caption": "Solid Rocket Propellant | 5 Types Supported | Data-Calibrated",
        "propellant_type": "🔥 Propellant Type",
        "select_propellant": "Select Propellant",
        "prop_info": "📌 Propellant Info",
        "governing_property": "🎯 Governing Property",
        "select_property": "Select Property",
        "use_exp_data": "Use Experimental Data (65°C)",
        "ea_header": "🌡️ Activation Energy Ea",
        "failure_criterion": "⚠️ Failure Criterion",
        "select_criterion": "Select Criterion",
        "allowed_change": "Allowed Change (%)",
        "storage_header": "📦 Storage Conditions",
        "storage_temp": "Storage Temperature (°C)",
        "humidity_header": "💧 Humidity Conditions",
        "use_humidity": "Enable Humidity Effect (Peck Model)",
        "rh_storage": "Relative Humidity (%)",
        "rh_ref": "Reference Humidity (%)",
        "n_humidity": "Humidity Factor n",
        "results_header": "📊 Results",
        "af_label": "⚡ Acceleration Factor AF",
        "k_storage": "🌡️ k at Storage",
        "k_ref": "📅 k at 25°C",
        "life_header": "⏳ Estimated Shelf Life",
        "life_years": "years",
        "life_days": "days",
        "failure_mode": "Failure Criterion",
        "duration_days": "Duration in Days",
        "not_failed": "⚠️ Property did not reach failure threshold within 30 years",
        "comparison_header": "🌡️ Shelf Life at Different Temperatures",
        "temperature": "Temperature (°C)",
        "k_per_day": "k (/day)",
        "af_col": "Acceleration Factor",
        "life_col": "Life (years)",
        "pdf_header": "📄 Export PDF Report",
        "pdf_caption": "Download a comprehensive report with all results and analyses",
        "pdf_generate": "📥 Generate PDF Report",
        "pdf_download": "💾 Download PDF Report",
        "csv_header": "📤 Upload New Experimental Data (CSV)",
        "csv_caption": "Upload CSV file with accelerated aging data for immediate analysis",
        "csv_upload": "Choose CSV file",
        "csv_success": "✅ File uploaded successfully!",
        "csv_data": "📋 Uploaded Data",
        "csv_analysis": "🔬 Data Analysis",
        "select_property_analysis": "Select property for analysis",
        "arrhenius_plot": "Arrhenius Plot",
        "comparison_types": "⚔️ Head-to-Head Comparison Between Two Propellants",
        "comparison_caption": "Compare two types: k, Ea, and shelf life at various temperatures",
        "type_a": "Type A",
        "type_b": "Type B",
        "compare_btn": "🔍 Compare Now",
        "comparison_curve": "📈 Shelf Life vs Temperature",
        "mc_header": "🎲 Monte Carlo Simulation - Probabilistic Distribution",
        "mc_caption": "Get a probabilistic distribution instead of a single value",
        "mc_n_sim": "Number of Simulations",
        "mc_ea_unc": "Ea Uncertainty (%)",
        "mc_k_unc": "k Uncertainty (%)",
        "mc_run": "🎲 Run Monte Carlo",
        "mc_results": "📊 Monte Carlo Results",
        "mc_mean": "Mean",
        "mc_median": "Median",
        "mc_p5": "P5 (Conservative)",
        "mc_p95": "P95 (Optimistic)",
        "years": "years",
        "abaqus_header": "🔧 Export Data to Abaqus",
        "abaqus_caption": "Download ready-to-use files for Abaqus/CAE",
        "abaqus_inp": "📄 Download INP File",
        "abaqus_py": "🐍 Download Python Script",
        "abaqus_csv": "📥 Download Stress-Strain Data (CSV)",
        "abaqus_guide": "📖 Abaqus Usage Guide",
        "language": "🌐 اللغة / Language",
    },
}


def t(key):
    """دالة الترجمة - ترجع النص حسب اللغة المختارة"""
    if "language" not in st.session_state:
        st.session_state.language = "ar"
    return TRANSLATIONS[st.session_state.language].get(key, key)
# -*- coding: utf-8 -*-
"""
منصة محاكاة اختبارات التقادم - محركات صاروخية صلبة
تدعم 5 أنواع من الوقود الصلب (DB, CMDB, Composite, NEPE, HTPE)
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

def has_valid_experimental_data(prop):
    """التحقق التلقائي إن النوع ده فيه بيانات تجريبية صالحة"""
    data = prop.get("experimental_data")
    if not data:
        return False
    for key, d in data.items():
        if isinstance(d, dict) and d.get("y") and len(d["y"]) >= 2:
            return True
    return False
st.set_page_config(
    page_title="منصة التقادم - وقود صلب",
    page_icon="🚀",
    layout="wide"
)

R = 8.314
T_ref_K = 298.15  # 25°C

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
        "aging_mechanism_en": "Stabilizer depletion (2-NDPA, Carbamite) + AP/NG interaction",
        "stabilizers_en": "2-NDPA, Carbamite (EC), MNA",
        "reference_en": "HELL FIRE Motor Test (1998) + Asthana et al.",
        "properties_en": {
            "young_modulus": "Young Modulus",
            "shore_A": "Shore A Hardness",
            "max_thrust": "Max Thrust",
        },
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

st.title(t("title"))
st.caption(t("caption"))
st.caption("وقود صاروخي صلب | 5 أنواع مدعومة | معايرة ببيانات تجريبية")

# ============================================================
# الشريط الجانبي: اختيار نوع الوقود
# ============================================================
# اختيار اللغة
lang_choice = st.sidebar.radio(
    "🌐 اللغة / Language",
    ["العربية", "English"],
    horizontal=True,
    key="lang_selector",
)
st.session_state.language = "ar" if lang_choice == "العربية" else "en"
st.sidebar.markdown("---")
st.sidebar.header(t("propellant_type"))
propellant_key = st.sidebar.selectbox(
    t("select_propellant"),
    list(PROPELLANT_TYPES.keys()),
)

prop = PROPELLANT_TYPES[propellant_key]

# عرض معلومات النوع
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
st.sidebar.header(t("governing_property"))
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

if prop["has_real_data"]:
    # استخلاص k من البيانات الفعلية
    d = prop["experimental_data"][prop_key]
    t_data = np.array(d["t"], dtype=float)
    y_data = np.array(d["y"], dtype=float)
    y0_data = d["y0"]
    with np.errstate(divide='ignore', invalid='ignore'):
        k_vals = (y_data / y0_data - 1) / t_data
    k_vals = k_vals[~np.isnan(k_vals) & ~np.isinf(k_vals)]
    k_obs_calc = float(np.mean(k_vals))

    # Ea من الأدبيات (لأن عندنا نقطة واحدة بس)
    Ea_kJ = float(prop["Ea_default"])

    st.sidebar.info(
        f"**k من بياناتك:** {k_obs_calc:.6f} /day\n\n"
        f"**Ea (من الأدبيات):** {Ea_kJ:.0f} kJ/mol"
    )
    st.sidebar.metric("Ea المستخدمة", f"{Ea_kJ:.0f} kJ/mol")
else:
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
# معيار الفشل
# ============================================================
st.sidebar.header(t("failure_criterion"))
criterion = st.sidebar.selectbox(
    "اختر المعيار",
    prop["failure_criteria"],
)

threshold_pct = st.sidebar.slider(
    "النسبة المسموحة (%)",
    min_value=5.0, max_value=50.0, value=20.0, step=1.0,
)

# ============================================================
# ظروف التخزين
# ============================================================
st.sidebar.header(t("storage_header"))
T_storage_C = st.sidebar.number_input(
    "درجة حرارة التخزين (°C)",
    value=25.0, step=1.0,
)

# ============================================================
# ظروف الرطوبة (Peck Model)
# ============================================================
st.sidebar.header(t("humidity_header"))
use_humidity = st.sidebar.checkbox(
    "تفعيل تأثير الرطوبة (Peck Model)",
    value=False,
    help="يستخدم نموذج Peck لدمج تأثير الرطوبة مع الحرارة",
    key="use_humidity_check",
)

if use_humidity:
    RH_storage = st.sidebar.slider(
        "الرطوبة النسبية (%)",
        0, 100, 50, 1,
        key="rh_storage_slider",
    )
    RH_ref = st.sidebar.number_input(
        "الرطوبة المرجعية (%)",
        value=50, min_value=1, max_value=100,
        key="rh_ref_input",
    )
    n_humidity = st.sidebar.slider(
        "معامل الرطوبة n",
        0.5, 3.0, 1.5, 0.1,
        help="عادة 1-3 للبوليمرات",
        key="n_humidity_slider",
    )
else:
    RH_storage = 50.0
    RH_ref = 50.0
    n_humidity = 1.0
# ============================================================
# الحسابات
# ============================================================
Ea = Ea_kJ * 1000
T_storage_K = T_storage_C + 273.15
T_exp_C = 65.0
T_exp_K = T_exp_C + 273.15

# حساب k عند 65°C
if prop["has_real_data"]:
    # من البيانات التجريبية
    d = prop["experimental_data"][prop_key]
    t = np.array(d["t"], dtype=float)
    y = np.array(d["y"], dtype=float)
    y0 = d["y0"]
    with np.errstate(divide='ignore', invalid='ignore'):
        k_vals = (y / y0 - 1) / t
    k_vals = k_vals[~np.isnan(k_vals) & ~np.isinf(k_vals)]
    k_obs = float(np.mean(k_vals))
    data_source = "Experimental data (65 c)"
else:
    # من الأدبيات
    k_obs = prop["k_exp_65C"]
    data_source = f"Literature values ({prop['reference']})"

# حساب A من k_obs
A_arr = k_obs / np.exp(-Ea / (R * T_exp_K))

def k_at(T_K):
    return A_arr * np.exp(-Ea / (R * T_K))

k_storage = k_at(T_storage_K)
k_ref = k_at(T_ref_K)
# حساب عامل الرطوبة (Peck Model)
if use_humidity:
    RH_factor_storage = (RH_storage / RH_ref) ** n_humidity
    RH_factor_ref = 1.0
else:
    RH_factor_storage = 1.0
    RH_factor_ref = 1.0

AF = (k_storage * RH_factor_storage) / (k_ref * RH_factor_ref)

# ============================================================
# عرض المعلومات
# ============================================================
st.markdown(f"""
<div class="info-box">
<b>📌 معايرة النموذج:</b><br>
• <b>نوع الوقود:</b> {propellant_key}<br>
• <b>الخاصية:</b> {prop_label}<br>
• <b>مصدر البيانات:</b> {data_source}<br>
• <b>k عند 65°C:</b> {k_obs:.6f} /day → {k_obs*100:.4f}% يوميًا<br>
• <b>معامل Arrhenius A:</b> {A_arr:.4e} /day
</div>
""", unsafe_allow_html=True)

# ============================================================
# المؤشرات
# ============================================================
st.header("📊 المؤشرات الأساسية")

col1, col2, col3 = st.columns(3)
col1.metric("⚡ معامل التسريع AF", f"{AF:.3f}")
col2.metric("🌡️ k عند التخزين", f"{k_storage:.4e} /day")
col3.metric("📅 k عند 25°C", f"{k_ref:.4e} /day")

# ============================================================
# العمر الافتراضي
# ============================================================
st.header("⏳ العمر الافتراضي")

k_effective = k_storage * RH_factor_storage
t_fail_days = (threshold_pct / 100) / k_effective
t_fail_years = t_fail_days / 365

st.markdown(f"""
<div class="success-box">
    <h2 style="color: #155724; margin: 0;">
    🎯 العمر عند {T_storage_C:.1f}°C = {t_fail_years:.2f} سنة
    </h2>
    <p style="margin: 10px 0 0 0; color: #155724;">
    <b>معيار الفشل:</b> {criterion}<br>
    <b>المدة بالأيام:</b> {t_fail_days:.0f} يوم
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# رسم التحقق (لو بيانات حقيقية)
# ============================================================
if has_valid_experimental_data(prop):
    st.header("🔬 التحقق: النموذج مقابل البيانات التجريبية")
    
    d = prop["experimental_data"][prop_key]
    t_data = np.array(d["t"], dtype=float)
    y_data = np.array(d["y"], dtype=float)
    y0 = d["y0"]
    
    fig, ax = plt.subplots(figsize=(11, 4.5))
    fig.patch.set_facecolor('#f5f7fa')
    ax.set_facecolor('#ffffff')
    
    ax.scatter(t_data, y_data, s=120, c='red', zorder=5,
               label=f'بيانات تجريبية ({T_exp_C:.0f}°C)')
    
    t_smooth = np.linspace(0, max(t_data) * 1.2, 100)
    y_smooth = y0 * (1 + k_obs * t_smooth)
    ax.plot(t_smooth, y_smooth, 'b-', linewidth=2.5,
            label=f'النموذج عند {T_exp_C:.0f}°C')
    
    ax.set_xlabel('الزمن (يوم)', fontsize=12)
    ax.set_ylabel(f'{d["label"]} ({d["unit"]})', fontsize=12)
    ax.set_title(f'مطابقة النموذج للبيانات عند {T_exp_C:.0f}°C',
                 fontsize=13, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    
    st.caption(f"✅ النموذج مضبوط تلقائيًا على بياناتك مع k = {k_obs:.6f}/day")

# ============================================================
# رسم تطور الخاصية عند التخزين
# ============================================================
st.header(f"📈 تطور {prop_label} عند {T_storage_C:.0f}°C")

# القيمة الابتدائية
if has_valid_experimental_data(prop):
    y0_display = prop["experimental_data"][prop_key]["y0"]
    unit_display = prop["experimental_data"][prop_key]["unit"]
else:
    y0_display = 1.0
    unit_display = "قيمة نسبية"

fig2, ax2 = plt.subplots(figsize=(11, 5))
fig2.patch.set_facecolor('#f5f7fa')
ax2.set_facecolor('#ffffff')

t_arr = np.linspace(0, max(365 * 50, t_fail_days * 1.5), 2000)
y_arr = y0_display * (1 + k_storage * t_arr)
threshold_val = y0_display * (1 + threshold_pct / 100)

ax2.plot(t_arr / 365, y_arr, 'b-', linewidth=2.5, label='القيمة المتوقعة')
ax2.axhline(threshold_val, color='r', linestyle='--', linewidth=2,
            label=f'حد الفشل (+{threshold_pct:.0f}%)')

if t_fail_years < 50:
    ax2.axvline(t_fail_years, color='g', linestyle=':', linewidth=2.5,
                label=f'العمر = {t_fail_years:.2f} سنة')
    ax2.scatter([t_fail_years], [threshold_val], s=200, c='red',
                zorder=5, marker='X')

ax2.set_xlabel('الزمن (سنة)', fontsize=12)
ax2.set_ylabel(f'{prop_label} ({unit_display})', fontsize=12)
ax2.set_title(f'منحنى التقادم عند {T_storage_C:.0f}°C',
              fontsize=13, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)
st.pyplot(fig2)

# ============================================================
# جدول المقارنة
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

# ============================================================
# مقارنة أنواع الوقود
# ============================================================
st.header("🔥 مقارنة أنواع الوقود المختلفة")
st.caption(f"باستخدام Ea = {Ea_kJ:.0f} kJ/mol و معيار {threshold_pct:.0f}%")

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
# بيانات تجريبية
# ============================================================
if prop["has_real_data"]:
    with st.expander(f"📋 عرض البيانات التجريبية ({propellant_key})"):
        d = prop["experimental_data"][prop_key]
        df_display = pd.DataFrame({
            "الزمن (يوم)": d["t"],
            f"{d['label']} ({d['unit']})": d["y"],
        })
        st.dataframe(df_display, use_container_width=True)

# ============================================================
# تحذير
# ============================================================
st.warning(
    f"⚠️ **تنبيه:** النموذج معاير بـ {data_source}. "
    f"القيم المعروضة تقديرية. للدقة العالية، يُنصح ببيانات من 3 درجات حرارة على الأقل."
)
# ============================================================
# ميزة رفع CSV لتحليل بيانات جديدة
# ============================================================
st.markdown("---")
st.header("📤 رفع بيانات تجريبية جديدة (CSV)")
st.caption("ارفع ملف CSV فيه بيانات التقادم المعجل لتحليلها فورًا")

uploaded_file = st.file_uploader(
    "اختر ملف CSV",
    type=["csv"],
    help="الأعمدة المطلوبة: temperature_C, time_days, property_name"
)

if uploaded_file is not None:
    try:
        # قراءة الملف
        df_upload = pd.read_csv(uploaded_file)
        
        st.success("✅ تم رفع الملف بنجاح!")
        
        # عرض البيانات
        st.subheader("📋 البيانات المرفوعة")
        st.dataframe(df_upload, use_container_width=True)
        
        # التحقق من الأعمدة
        required_cols = ['temperature_C', 'time_days']
        if not all(col in df_upload.columns for col in required_cols):
            st.error(
                f"⚠️ الملف لازم يحتوي على الأعمدة: {required_cols}. "
                f"الأعمدة الموجودة: {list(df_upload.columns)}"
            )
        else:
            # اختيار الخاصية
            property_cols = [c for c in df_upload.columns 
                           if c not in ['temperature_C', 'time_days']]
            
            if len(property_cols) == 0:
                st.error("⚠️ لا توجد أعمدة خصائص للتحليل")
            else:
                selected_prop = st.selectbox(
                    "اختر الخاصية للتحليل",
                    property_cols
                )
                
                # حساب k لكل درجة حرارة
                st.subheader("🔬 تحليل البيانات")
                
                results = []
                for T in sorted(df_upload['temperature_C'].unique()):
                    sub = df_upload[df_upload['temperature_C'] == T]
                    sub = sub.dropna(subset=[selected_prop])
                    
                    if len(sub) < 2:
                        continue
                    
                    t_vals = sub['time_days'].values
                    y_vals = sub[selected_prop].values
                    y0 = y_vals[0]
                    
                    with np.errstate(divide='ignore', invalid='ignore'):
                        k_vals = (y_vals / y0 - 1) / t_vals
                    k_vals = k_vals[~np.isnan(k_vals) & ~np.isinf(k_vals)]
                    k_mean = float(np.mean(k_vals))
                    
                    results.append({
                        'T_C': T,
                        'T_K': T + 273.15,
                        'k': k_mean,
                        'k_std': float(np.std(k_vals)),
                        'n_points': len(sub),
                        'y0': y0,
                    })
                
                results_df = pd.DataFrame(results)
                st.dataframe(results_df, use_container_width=True)
                
                # حساب Ea من البيانات لو فيه 3 درجات حرارة
                if len(results_df) >= 3:
                    inv_T = 1 / results_df['T_K'].values
                    ln_k = np.log(np.abs(results_df['k'].values))
                    slope, intercept = np.polyfit(inv_T, ln_k, 1)
                    Ea_calc = -slope * R / 1000  # kJ/mol
                    A_calc = np.exp(intercept)
                    
                    st.success(f"✅ **طاقة التنشيط Ea = {Ea_calc:.2f} kJ/mol**")
                    st.info(f"**معامل Arrhenius A = {A_calc:.4e} /day**")
                    
                    # حساب العمر عند 25°C
                    k_25 = A_calc * np.exp(-Ea_calc * 1000 / (R * T_ref_K))
                    life_25 = (threshold_pct / 100) / k_25 / 365
                    
                    col1, col2 = st.columns(2)
                    col1.metric("Ea المحسوبة", f"{Ea_calc:.1f} kJ/mol")
                    col2.metric("العمر عند 25°C", f"{life_25:.2f} سنة")
                    
                    # رسم Arrhenius
                    fig_a, ax_a = plt.subplots(figsize=(10, 5))
                    fig_a.patch.set_facecolor('#f5f7fa')
                    ax_a.scatter(inv_T * 1000, ln_k, s=150, c='red', zorder=5)
                    t_line = np.linspace(inv_T.min(), inv_T.max(), 100)
                    ax_a.plot(t_line * 1000, slope * t_line + intercept, 
                             'b--', linewidth=2, 
                             label=f'Ea = {Ea_calc:.1f} kJ/mol')
                    ax_a.set_xlabel('1000/T (K⁻¹)')
                    ax_a.set_ylabel('ln(k)')
                    ax_a.set_title('Arrhenius Plot', fontweight='bold')
                    ax_a.legend()
                    ax_a.grid(True, alpha=0.3)
                    st.pyplot(fig_a)
                else:
                    st.warning(
                        f"⚠️ عندك {len(results_df)} درجة حرارة فقط. "
                        "لحساب Ea بدقة، محتاج 3 درجات على الأقل."
                    )
    
    except Exception as e:
        st.error(f"❌ خطأ في قراءة الملف: {str(e)}")
        # ============================================================
# ============================================================
# تصدير تقرير PDF
# ============================================================
st.markdown("---")
st.header("📄 تصدير تقرير PDF")
st.caption("حمّل تقرير شامل يحتوي على كل النتائج والتحليلات")


def clean_text_for_pdf(text):
    """إزالة أي حروف عربية من النص (fpdf2 مش بيدعم العربي)"""
    import re
    cleaned = re.sub(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+', '', text)
    return ' '.join(cleaned.split()).strip()


def generate_pdf_report():
    """إنشاء تقرير PDF احترافي بالنتائج"""

    pdf = FPDF()
    pdf.add_page()

    # ===== العنوان الرئيسي =====
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(30, 58, 138)  # أزرق غامق
    pdf.cell(0, 12, "Solid Rocket Motor - Aging Simulation Report",
             ln=True, align="C")
    pdf.ln(3)

    # خط فاصل
    pdf.set_draw_color(30, 58, 138)
    pdf.set_line_width(0.5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)

    # ===== التاريخ =====
    pdf.set_font("Arial", "I", 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 6, f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
             ln=True, align="R")
    pdf.ln(3)

    # ===== 1. معلومات الوقود =====
    pdf.set_font("Arial", "B", 13)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 9, "1. Propellant Information", ln=True)
    pdf.ln(2)

    pdf.set_font("Arial", "", 10)
    info_lines = [
                   f"Propellant Type: {clean_text_for_pdf(propellant_key).split(' - ')[0]}",
            f"Aging Mechanism: {prop.get('aging_mechanism_en', 'N/A')}",           
        f"Stabilizers: {prop.get('stabilizers_en', 'N/A')}",
            f"Reference: {prop.get('reference_en', prop.get('reference', 'N/A'))}",
    ]
    for line in info_lines:
        pdf.cell(0, 6, f"  - {line}", ln=True)
    pdf.ln(3)

    # ===== 2. Simulation Parameters =====
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 9, "2. Simulation Parameters", ln=True)
    pdf.ln(2)
    pdf.set_font("Arial", "", 10)
    prop_label_en = prop.get("properties_en", {}).get(prop_key, "Selected Property")
    param_lines = [
            f"Governing Property: {prop_label_en}",
            f"Activation Energy (Ea): {Ea_kJ:.1f} kJ/mol",
            f"  [Literature reference: {prop.get('Ea_default', 0):.0f} kJ/mol]",
            f"Arrhenius Constant (A): {A_arr:.4e} /day",
            f"Failure Criterion: {prop_label_en} change",
            f"Allowed Change: {threshold_pct:.1f} %",
            f"Storage Temperature: {T_storage_C:.1f} C",
            f"Reference Temperature: 25.0 C",
            f"Experimental Temperature: {T_exp_C:.1f} C",
        ]
    for line in param_lines:
        pdf.cell(0, 6, f"  - {line}", ln=True)
    pdf.ln(3)

    # ===== 3. Results =====
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 9, "3. Simulation Results", ln=True)
    pdf.ln(2)

    pdf.set_font("Arial", "", 10)
    result_lines = [
        f"Acceleration Factor (AF): {AF:.3f}",
        f"Rate Constant k at storage: {k_storage:.4e} /day",
        f"Rate Constant k at 25C: {k_ref:.4e} /day",
    ]
    for line in result_lines:
        pdf.cell(0, 6, f"  - {line}", ln=True)
    pdf.ln(2)

    # صندوق النتيجة الرئيسية
    pdf.set_fill_color(212, 237, 218)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"ESTIMATED SHELF LIFE: {t_fail_years:.2f} years "
                    f"({t_fail_days:.0f} days)",
             ln=True, align="C", fill=True)
    pdf.ln(5)

    # ===== 4. Life at Different Temperatures =====
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 9, "4. Shelf Life vs Storage Temperature", ln=True)
    pdf.ln(2)

    # رأس الجدول
    pdf.set_font("Arial", "B", 10)
    pdf.set_fill_color(230, 230, 230)
    pdf.cell(50, 8, "Temperature (C)", border=1, align="C", fill=True)
    pdf.cell(60, 8, "k (/day)", border=1, align="C", fill=True)
    pdf.cell(60, 8, "Life (years)", border=1, align="C", fill=True)
    pdf.ln()

    # بيانات الجدول
    pdf.set_font("Arial", "", 10)
    for T_C in [15, 20, 25, 30, 35, 40, 50, 60, 65]:
        T_K = T_C + 273.15
        k = k_at(T_K)
        t_y = (threshold_pct / 100) / k / 365
        life_str = f"{t_y:.2f}" if t_y < 1000 else "> 1000"
        pdf.cell(50, 7, f"{T_C}", border=1, align="C")
        pdf.cell(60, 7, f"{k:.4e}", border=1, align="C")
        pdf.cell(60, 7, life_str, border=1, align="C")
        pdf.ln()

    pdf.ln(5)

    # ===== 5. Notes =====
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 9, "5. Important Notes", ln=True)
    pdf.ln(2)

    pdf.set_font("Arial", "", 10)
    notes = [
        "- This report is generated by an estimation tool based on",
        "  Arrhenius kinetics and accelerated aging data.",
        "- Results are estimates and should be verified experimentally",
        "  before critical decisions.",
        "- For higher accuracy, experimental data at 3 or more",
        "  temperatures is recommended.",
        f"- Data source used: 65 c Experimental Data"
    ]
    for line in notes:
        pdf.cell(0, 6, line, ln=True)

    pdf.ln(10)

    # التوقيع
    pdf.set_font("Arial", "I", 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 6, "Generated by: Rocket Aging Simulation Platform",
             ln=True, align="C")
    pdf.cell(0, 6, "https://rocket-aging-sim.streamlit.app",
             ln=True, align="C")

    return bytes(pdf.output())


# زر تحميل التقرير
if st.button("📥 إنشاء التقرير PDF", type="primary"):
    try:
        pdf_bytes = generate_pdf_report()
        st.success("✅ التقرير جاهز للتحميل!")
        st.download_button(
            label="💾 تحميل التقرير PDF",
            data=pdf_bytes,
            file_name=f"aging_report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
            mime="application/pdf",
            key="pdf_download_btn"
        )
    except Exception as e:
        st.error(f"❌ خطأ في إنشاء التقرير: {str(e)}")
# ============================================================
# المقارنة التفصيلية بين نوعين من الوقود
# ============================================================
st.markdown("---")
st.header("⚔️ مقارنة تفصيلية بين نوعين من الوقود")
st.caption("قارن بين نوعين: k، Ea، والعمر الافتراضي عند درجات حرارة مختلفة")

col_a, col_b = st.columns(2)

with col_a:
    type_A = st.selectbox(
        "النوع الأول (A)",
        list(PROPELLANT_TYPES.keys()),
        index=0,
        key="compare_type_A",
    )

with col_b:
    type_B = st.selectbox(
        "النوع الثاني (B)",
        list(PROPELLANT_TYPES.keys()),
        index=2,
        key="compare_type_B",
    )

if st.button("🔍 قارن الآن", type="primary", key="compare_btn"):
    prop_A = PROPELLANT_TYPES[type_A]
    prop_B = PROPELLANT_TYPES[type_B]

    # حساب العمر لكل نوع
    results = []
    for name, p in [(type_A, prop_A), (type_B, prop_B)]:
        k_65 = p["k_exp_65C"]
        A_i = k_65 / np.exp(-Ea / (R * T_exp_K))
        k_25 = A_i * np.exp(-Ea / (R * T_ref_K))
        k_stor = A_i * np.exp(-Ea / (R * T_storage_K))

        life_25 = (threshold_pct / 100) / k_25 / 365
        life_stor = (threshold_pct / 100) / k_stor / 365

        results.append({
            "النوع": name.split(" - ")[0],
            "k عند 65°C": f"{k_65:.4e}",
            "Ea (kJ/mol)": f"{p['Ea_default']:.0f}",
            "العمر عند 25°C": f"{life_25:.2f}",
            f"العمر عند {T_storage_C:.0f}°C": f"{life_stor:.2f}",
        })

    # عرض الجدول
    df_compare = pd.DataFrame(results).T
    df_compare.columns = ["النوع A", "النوع B"]
    st.dataframe(df_compare, use_container_width=True)

    # رسم مقارن
    st.subheader("📈 منحنى العمر الافتراضي مقابل درجة الحرارة")
    fig_cmp, ax_cmp = plt.subplots(figsize=(11, 5))
    fig_cmp.patch.set_facecolor('#f5f7fa')
    ax_cmp.set_facecolor('#ffffff')

    temps_plot = np.linspace(15, 70, 50)
    colors = ['steelblue', 'crimson']

    for i, (name, p) in enumerate([(type_A, prop_A), (type_B, prop_B)]):
        k_65 = p["k_exp_65C"]
        A_i = k_65 / np.exp(-Ea / (R * T_exp_K))
        k_arr = A_i * np.exp(-Ea / (R * (temps_plot + 273.15)))
        life_arr = (threshold_pct / 100) / k_arr / 365
        ax_cmp.plot(temps_plot, life_arr, linewidth=2.5,
                    color=colors[i], label=name.split(" - ")[0])

    ax_cmp.set_xlabel("درجة الحرارة (°C)", fontsize=12)
    ax_cmp.set_ylabel("العمر الافتراضي (سنة)", fontsize=12)
    ax_cmp.set_title("مقارنة العمر بين النوعين", fontsize=13, fontweight='bold')
    ax_cmp.set_yscale('log')
    ax_cmp.legend(fontsize=11)
    ax_cmp.grid(True, alpha=0.3, which='both')
    st.pyplot(fig_cmp)

    # حساب فرق النسبة
    k_65_A = prop_A["k_exp_65C"]
    k_65_B = prop_B["k_exp_65C"]
    ratio = k_65_A / k_65_B

    st.info(
        f"**الفرق بين النوعين:**\n\n"
        f"- النوع **A** ({type_A.split(' - ')[0]}) له k = {k_65_A:.4e} /day\n"
        f"- النوع **B** ({type_B.split(' - ')[0]}) له k = {k_65_B:.4e} /day\n"
        f"- **النسبة**: {ratio:.2f}x  →  "
        f"النوع {'A' if ratio > 1 else 'B'} يتقادم أسرع بـ {abs(ratio - 1)*100:.1f}%"
    )
# ============================================================
# محاكاة Monte Carlo - توزيع احتمالي للعمر
# ============================================================
st.markdown("---")
st.header("🎲 محاكاة Monte Carlo - التوزيع الاحتمالي")
st.caption("بدل رقم واحد، هتطلعلك عيّنة احتمالية للعمر بناءً على عدم اليقين في Ea و k")

col_mc1, col_mc2, col_mc3 = st.columns(3)
with col_mc1:
    n_sim = st.number_input("عدد مرات المحاكاة", value=1000, 
                            min_value=100, max_value=10000, step=100,
                            key="mc_n_sim")
with col_mc2:
    Ea_uncertainty = st.slider("عدم اليقين في Ea (%)", 0, 30, 10,
                               key="mc_ea_unc")
with col_mc3:
    k_uncertainty = st.slider("عدم اليقين في k (%)", 0, 50, 20,
                              key="mc_k_unc")

if st.button("🎲 تشغيل Monte Carlo", type="primary", key="mc_run_btn"):
    np.random.seed(42)

    # توزيعات
    Ea_samples = np.random.normal(Ea_kJ, Ea_kJ * Ea_uncertainty / 100, n_sim)
    k_65_samples = np.random.normal(k_obs, k_obs * k_uncertainty / 100, n_sim)

    # ضمان قيم موجبة
    Ea_samples = np.abs(Ea_samples)
    k_65_samples = np.abs(k_65_samples)

    # حساب العمر لكل محاكاة
    life_samples = []
    for Ea_i, k_65_i in zip(Ea_samples, k_65_samples):
        A_i = k_65_i / np.exp(-Ea_i * 1000 / (R * T_exp_K))
        k_stor_i = A_i * np.exp(-Ea_i * 1000 / (R * T_storage_K))
        life_i = (threshold_pct / 100) / k_stor_i / 365
        life_samples.append(life_i)

    life_samples = np.array(life_samples)

    # إحصائيات
    st.subheader("📊 نتائج Monte Carlo")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("المتوسط", f"{np.mean(life_samples):.2f} سنة")
    c2.metric("الوسيط", f"{np.median(life_samples):.2f} سنة")
    c3.metric("P5 (تحفظي)", f"{np.percentile(life_samples, 5):.2f} سنة")
    c4.metric("P95 (متفائل)", f"{np.percentile(life_samples, 95):.2f} سنة")

    # Histogram
    fig_mc, ax_mc = plt.subplots(figsize=(11, 5))
    fig_mc.patch.set_facecolor('#f5f7fa')
    ax_mc.set_facecolor('#ffffff')

    ax_mc.hist(life_samples, bins=50, color='steelblue',
               edgecolor='white', alpha=0.8)
    ax_mc.axvline(np.mean(life_samples), color='red',
                  linestyle='--', linewidth=2, label='المتوسط')
    ax_mc.axvline(np.percentile(life_samples, 5), color='orange',
                  linestyle=':', linewidth=2, label='P5 (تحفظي)')
    ax_mc.axvline(np.percentile(life_samples, 95), color='green',
                  linestyle=':', linewidth=2, label='P95 (متفائل)')

    ax_mc.set_xlabel('العمر (سنة)', fontsize=12)
    ax_mc.set_ylabel('التكرار', fontsize=12)
    ax_mc.set_title(f'توزيع العمر الاحتمالي ({n_sim} محاكاة)',
                    fontsize=13, fontweight='bold')
    ax_mc.legend()
    ax_mc.grid(True, alpha=0.3)
    st.pyplot(fig_mc)

    # تفسير
    st.info(
        f"**التفسير:** بناءً على {n_sim} محاكاة، "
        f"العمر المتوقع بين **{np.percentile(life_samples, 5):.2f}** "
        f"و **{np.percentile(life_samples, 95):.2f} سنة** بثقة 90%. "
        f"القيمة الأكثر ترجيحًا (الوسيط) = **{np.median(life_samples):.2f} سنة**."
    )
# ============================================================
# تصدير البيانات لبرنامج Abaqus
# ============================================================
st.markdown("---")
st.header("🔧 تصدير البيانات لـ Abaqus")
st.caption("حمّل الملفات الجاهزة للتشغيل في برنامج Abaqus/CAE")

st.info(
    "**ملاحظة:** Abaqus مش بيشتغل على الإنترنت. الملفات دي هتحمّلها "
    "على جهازك وتشغّلها في Abaqus/CAE أو Abaqus Command."
)

col_abq1, col_abq2 = st.columns(2)

with col_abq1:
    if st.button("📄 تحميل ملف INP", type="primary", key="abq_inp_btn"):
        # توليد ملف INP
        inp_content = f"""*HEADING
Solid Rocket Motor Propellant - Aging Simulation
Propellant: {clean_text_for_pdf(propellant_key).split(' - ')[0]}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
**
*MATERIAL, NAME=PROPELLANT
*ELASTIC
{Ea_kJ * 10:.1f}, 0.4999
*HYPERELASTIC, NEO-HOOKE
0.5, 0.0
*VISCOELASTIC, TIME=PRONY
0.1, 0.05, 0.0
0.05, 0.5, 0.0
0.02, 2.0, 0.0
*DENSITY
{prop.get('density', 1700.0) / 1e6:.4e}
**
*SOLID SECTION, ELSET=PROP, MATERIAL=PROPELLANT
**
** Aging parameters
** Storage Temperature: {T_storage_C} C
** Humidity: {RH_storage if use_humidity else 50} %
** Shelf Life: {t_fail_years:.2f} years
** Ea: {Ea_kJ} kJ/mol
** k at 65C: {k_obs:.6f} /day
**
"""
        st.download_button(
            label="💾 تحميل ملف INP",
            data=inp_content.encode('utf-8'),
            file_name=f"propellant_aging_{datetime.now().strftime('%Y%m%d_%H%M')}.inp",
            mime="text/plain",
            key="abq_inp_dl",
        )

with col_abq2:
    if st.button("🐍 تحميل سكريبت Python", type="primary", key="abq_py_btn"):
        # توليد سكريبت Python لـ Abaqus
        py_content = f'''# -*- coding: utf-8 -*-
"""
Abaqus Python Script - Solid Rocket Motor Propellant Aging
Generated by Rocket Aging Simulation Platform
Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *

# ===== Model Parameters =====
propellant_name = "{clean_text_for_pdf(propellant_key).split(' - ')[0]}"
young_modulus = {Ea_kJ * 10:.2f}  # MPa (approx)
poisson_ratio = 0.4999
density = {prop.get('density', 1700.0) / 1e6:.4e}  # tonne/mm^3

# ===== Aging Parameters =====
storage_temp_C = {T_storage_C}
humidity_percent = {RH_storage if use_humidity else 50}
shelf_life_years = {t_fail_years:.2f}
Ea_kJ_per_mol = {Ea_kJ:.1f}
k_65C_per_day = {k_obs:.6f}

# ===== Create Model =====
model_name = 'PropellantAging'
mdb.Model(name=model_name)

# ===== Create Material =====
mat = mdb.models[model_name].Material(name='PROPELLANT')
mat.Elastic(table=((young_modulus, poisson_ratio), ))
mat.Density(table=((density, ), ))
mat.Hyperelastic(
    materialType=NEO_HOOKE,
    table=((0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), )
)
mat.Viscoelastic(
    domain=TIME,
    time=PRONY,
    table=((0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
           (0.05, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
           (0.02, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
)

# ===== Print Info =====
print("=" * 60)
print("Propellant Aging Model Created Successfully")
print("=" * 60)
print(f"Propellant: {{propellant_name}}")
print(f"Storage Temperature: {{storage_temp_C}} C")
print(f"Humidity: {{humidity_percent}} %")
print(f"Shelf Life: {{shelf_life_years:.2f}} years")
print(f"Ea: {{Ea_kJ_per_mol}} kJ/mol")
print(f"k at 65C: {{k_65C_per_day}} /day")
print("=" * 60)
print("Next Steps:")
print("1. Add geometry (part module)")
print("2. Assign section to geometry")
print("3. Create step and boundary conditions")
print("4. Submit job")
'''
        st.download_button(
            label="💾 تحميل السكريبت",
            data=py_content.encode('utf-8'),
            file_name=f"abaqus_script_{datetime.now().strftime('%Y%m%d_%H%M')}.py",
            mime="text/x-python",
            key="abq_py_dl",
        )

# ===== تصدير بيانات الإجهاد-الانفعال =====
st.subheader("📊 بيانات الإجهاد-الانفعال للتصدير")

# حساب بيانات تجريبية بناءً على الخاصية المختارة
strain_data = np.linspace(0, 0.1, 20)  # 0 to 10% strain
stress_data = []

for s in strain_data:
    # نموذج خطي بسيط: stress = E * strain
    stress_val = (Ea_kJ * 10) * s  # MPa
    stress_data.append(stress_val)

df_stress = pd.DataFrame({
    "Strain": strain_data,
    "Stress_MPa": stress_data,
    "Time_days": [0] * len(strain_data),
})

st.dataframe(df_stress.head(10), use_container_width=True)

if st.button("📥 تحميل بيانات الإجهاد-الانفعال (CSV)", key="abq_csv_btn"):
    csv_data = df_stress.to_csv(index=False)
    st.download_button(
        label="💾 تحميل CSV",
        data=csv_data.encode('utf-8'),
        file_name=f"stress_strain_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
        mime="text/csv",
        key="abq_csv_dl",
    )

# ===== دليل الاستخدام =====
with st.expander("📖 دليل استخدام ملفات Abaqus"):
    st.markdown("""
    ### خطوات تشغيل التحليل في Abaqus:
    
    **1. تحميل الملفات:**
    - حمّل ملف `INP` (خامات المادة)
    - حمّل سكريبت Python (للتحليل الكامل)
    - حمّل ملف CSV (بيانات الإجهاد-الانفعال)
    
    **2. تشغيل السكريبت:**
    - افتح Abaqus/CAE
    - من القائمة: File → Run Script
    - اختر السكريبت المحمّل
    - اضغط Open
    
    **3. بديل: تشغيل INP مباشرة:**
    - افتح Abaqus Command
    - اكتب: `abaqus job=model_name input=file.inp`
    
    **4. البيانات المتوفرة:**
    - **Material Properties:** E, ν, Density
    - **Hyperelastic:** Neo-Hookean (C10, D1)
    - **Viscoelastic:** Prony Series (3 terms)
    - **Aging Conditions:** Temperature, Humidity, Shelf Life
    
    **5. الخطوات التالية في Abaqus:**
    - إضافة الهندسة (Part Module)
    - تعيين القطاع (Section Assignment)
    - إضافة خطوات التحليل (Step Module)
    - شروط الحدود (Load Module)
    - الشبكة (Mesh Module)
    - تشغيل الوظيفة (Job Module)
    
    ### ⚠️ ملاحظة مهمة:
    - القيم الافتراضية للمعاملات تقريبية ومبنية على البيانات المتاحة
    - يُنصح بمعايرة القيم من اختبارات فعلية قبل الاستخدام
    - راجع وحدة القياسات (Units) في Abaqus
    """)
