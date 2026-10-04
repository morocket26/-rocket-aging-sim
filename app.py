# -*- coding: utf-8 -*-
"""
منصة محاكاة اختبارات التقادم - محركات صاروخية صلبة
تدعم 5 أنواع وقود + تقادم معجل + رطوبة + Abaqus + لغتين
"""
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

# ============================================================
# قاموس الترجمات
# ============================================================
TRANSLATIONS = {
    "ar": {
        "title": "🚀 منصة محاكاة اختبارات التقادم",
        "caption": "وقود صاروخي صلب | 5 أنواع مدعومة | معايرة ببيانات تجريبية",
        "propellant_type": "🔥 نوع الوقود",
        "select_propellant": "اختر نوع الوقود",
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
        "comparison_header": "🌡️ مقارنة العمر عند درجات حرارة مختلفة",
        "temperature": "الحرارة (°C)",
        "k_per_day": "k (/day)",
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
        "comparison_types": "⚔️ مقارنة تفصيلية بين نوعين من الوقود",
        "comparison_caption": "قارن بين نوعين: k، Ea، والعمر الافتراضي",
        "type_a": "النوع الأول (A)",
        "type_b": "النوع الثاني (B)",
        "compare_btn": "🔍 قارن الآن",
        "comparison_curve": "📈 منحنى العمر الافتراضي مقابل درجة الحرارة",
        "mc_header": "🎲 محاكاة Monte Carlo - التوزيع الاحتمالي",
        "mc_caption": "بدل رقم واحد، هتطلعلك عيّنة احتمالية للعمر",
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
        "abaqus_guide": "📖 دليل استخدام ملفات Abaqus",
        "language": "🌐 اللغة / Language",
        "name": "الاسم",
        "aging_mech_label": "آلية التقادم",
        "stabilizers_label": "المُثبِّتات",
        "reference_label": "المرجع",
        "propellant_label": "الوقود",
        "validation_header": "🔬 التحقق: النموذج مقابل البيانات التجريبية",
        "model_label": "النموذج",
        "exp_data_label": "بيانات تجريبية",
        "report_ready": "✅ التقرير جاهز للتحميل!",
        "error": "خطأ",
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
        "comparison_header": "🌡️ Shelf Life at Different Temperatures",
        "temperature": "Temperature (°C)",
        "k_per_day": "k (/day)",
        "life_col": "Life (years)",
        "pdf_header": "📄 Export PDF Report",
        "pdf_caption": "Download a comprehensive report with all results",
        "pdf_generate": "📥 Generate PDF Report",
        "pdf_download": "💾 Download PDF Report",
        "csv_header": "📤 Upload New Experimental Data (CSV)",
        "csv_caption": "Upload CSV file with accelerated aging data",
        "csv_upload": "Choose CSV file",
        "csv_success": "✅ File uploaded successfully!",
        "csv_data": "📋 Uploaded Data",
        "csv_analysis": "🔬 Data Analysis",
        "select_property_analysis": "Select property for analysis",
        "comparison_types": "⚔️ Head-to-Head Comparison",
        "comparison_caption": "Compare two types: k, Ea, and shelf life",
        "type_a": "Type A",
        "type_b": "Type B",
        "compare_btn": "🔍 Compare Now",
        "comparison_curve": "📈 Shelf Life vs Temperature",
        "mc_header": "🎲 Monte Carlo Simulation",
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
        "abaqus_guide": "📖 Abaqus Usage Guide",
        "language": "🌐 اللغة / Language",
        "name": "Name",
        "aging_mech_label": "Aging Mechanism",
        "stabilizers_label": "Stabilizers",
        "reference_label": "Reference",
        "propellant_label": "Propellant",
        "validation_header": "🔬 Validation: Model vs Experimental Data",
        "model_label": "Model",
        "exp_data_label": "Experimental data",
        "report_ready": "✅ Report ready!",
        "error": "Error",
    },
}


def t(key):
    if "language" not in st.session_state:
        st.session_state.language = "ar"
    return TRANSLATIONS[st.session_state.language].get(key, key)


# ============================================================
# دوال مساعدة
# ============================================================
def clean_text_for_pdf(text):
    import re
    cleaned = re.sub(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+', '', text)
    return ' '.join(cleaned.split()).strip()


def get_propellant_display_info(prop, key):
    if st.session_state.language == "en":
        return {
            "name": key.split(' - ')[0],
            "aging": prop.get('aging_mechanism_en', 'N/A'),
            "stabilizers": prop.get('stabilizers_en', 'N/A'),
            "reference": prop.get('reference_en', prop.get('reference', 'N/A')),
        }
    else:
        return {
            "name": prop.get('name_ar', key.split(' - ')[0]),
            "aging": prop.get('aging_mechanism', 'N/A'),
            "stabilizers": prop.get('stabilizers', 'N/A'),
            "reference": prop.get('reference', 'N/A'),
        }


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
        "failure_criteria_en": [
            "Young Modulus increase by 20%",
            "Max Thrust increase by 15%",
            "Shore A increase by 10%",
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
        "properties_ar": {
            "young_modulus": "معامل يونج",
            "shore_A": "الصلابة Shore A",
            "max_thrust": "الدفع الأقصى",
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
        "failure_criteria_en": [
            "Stabilizer depletion by 50%",
            "Young Modulus increase by 20%",
            "Shore A increase by 10%",
        ],
        "reference": "NATO STO-MP-AVT-268 (2017)",
        "aging_mechanism_en": "Nitrate ester decomposition → Stabilizer depletion",
        "stabilizers_en": "2-NDPA, Ethyl Centralite, Akardite II",
        "reference_en": "NATO STO-MP-AVT-268 (2017)",
        "properties_en": {
            "young_modulus": "Young Modulus",
            "shore_A": "Shore A Hardness",
        },
        "properties_ar": {
            "young_modulus": "معامل يونج",
            "shore_A": "الصلابة Shore A",
        },
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
        "failure_criteria_en": [
            "Elongation decrease by 30%",
            "Shore A increase by 15%",
            "Young Modulus increase by 25%",
        ],
        "reference": "Shekhar, Prediction of Shelf Life (2014)",
        "aging_mechanism_en": "Binder oxidation + crosslinking",
        "stabilizers_en": "Antioxidants",
        "reference_en": "Shekhar, Prediction of Shelf Life (2014)",
        "properties_en": {
            "young_modulus": "Young Modulus",
            "shore_A": "Shore A Hardness",
        },
        "properties_ar": {
            "young_modulus": "معامل يونج",
            "shore_A": "الصلابة Shore A",
        },
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
        "failure_criteria_en": [
            "Stabilizer depletion by 40%",
            "Young Modulus change by 15%",
            "Weight loss 2%",
        ],
        "reference": "NATO STO-TR-AVT-171",
        "aging_mechanism_en": "Nitrate ester decomposition + plasticizer migration",
        "stabilizers_en": "Special stabilizers",
        "reference_en": "NATO STO-TR-AVT-171",
        "properties_en": {
            "young_modulus": "Young Modulus",
            "shore_A": "Shore A Hardness",
        },
        "properties_ar": {
            "young_modulus": "معامل يونج",
            "shore_A": "الصلابة Shore A",
        },
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
        "failure_criteria_en": [
            "Elongation decrease by 25%",
            "Young Modulus increase by 20%",
        ],
        "reference": "Insensitive Munitions Program Reports",
        "aging_mechanism_en": "Polymer oxidation",
        "stabilizers_en": "Antioxidants",
        "reference_en": "Insensitive Munitions Program Reports",
        "properties_en": {
            "young_modulus": "Young Modulus",
            "shore_A": "Shore A Hardness",
        },
        "properties_ar": {
            "young_modulus": "معامل يونج",
            "shore_A": "الصلابة Shore A",
        },
        "k_exp_65C": 0.0040,
        "has_real_data": False,
        "experimental_data": None,
    },
}

# ============================================================
# إعدادات الصفحة
# ============================================================
st.set_page_config(page_title="Aging Simulation", page_icon="🚀", layout="wide")

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

# ============================================================
# اختيار اللغة + مسح الـ state لما اللغة تتغير
# ============================================================
if "language" not in st.session_state:
    st.session_state.language = "ar"

lang_choice = st.sidebar.radio(
    "🌐 اللغة / Language",
    ["العربية", "English"],
    horizontal=True,
    key="lang_selector_main",
)

new_lang = "ar" if lang_choice == "العربية" else "en"

if st.session_state.language != new_lang:
    widget_prefixes = [
        "propellant_selector_", "prop_label_selector_", "criterion_selector_",
        "use_real_data_checkbox_", "ea_slider_", "threshold_slider_",
        "storage_temp_input_", "use_humidity_check_", "rh_storage_slider_",
        "rh_ref_input_", "n_humidity_slider_", "compare_type_A_",
        "compare_type_B_", "csv_prop_selector_", "csv_uploader_main_",
        "mc_n_sim_", "mc_ea_unc_", "mc_k_unc_", "pdf_generate_btn_",
        "pdf_download_btn_", "abq_inp_btn_", "abq_py_btn_", "abq_inp_dl_",
        "abq_py_dl_", "compare_btn_key_", "mc_run_btn_",
    ]
    keys_to_delete = [k for k in list(st.session_state.keys())
                      if any(k.startswith(p) for p in widget_prefixes)]
    for k in keys_to_delete:
        del st.session_state[k]
    st.session_state.language = new_lang

st.sidebar.markdown("---")
lang_key = st.session_state.language

# ============================================================
# العنوان
# ============================================================
st.title(t("title"))
st.caption(t("caption"))

# ============================================================
# الشريط الجانبي: اختيار نوع الوقود
# ============================================================
st.sidebar.header(t("propellant_type"))
propellant_key = st.sidebar.selectbox(
    t("select_propellant"),
    list(PROPELLANT_TYPES.keys()),
    key=f"propellant_selector_{lang_key}",
)

if propellant_key not in PROPELLANT_TYPES:
    propellant_key = list(PROPELLANT_TYPES.keys())[0]

prop = PROPELLANT_TYPES[propellant_key]

prop_info = get_propellant_display_info(prop, propellant_key)
st.sidebar.markdown(f"""
**{t("prop_info")}:**
- **{t("name")}:** {prop_info['name']}
- **{t("aging_mech_label")}:** {prop_info['aging']}
- **{t("stabilizers_label")}:** {prop_info['stabilizers']}
- **{t("reference_label")}:** {prop_info['reference']}
""")

# ============================================================
# اختيار الخاصية الحاكمة (مع الحل النهائي)
# ============================================================
st.sidebar.header(t("governing_property"))

if st.session_state.language == "en":
    prop_options = prop.get("properties_en", {"young_modulus": "Young Modulus"})
else:
    prop_options = prop.get("properties_ar", {"young_modulus": "معامل يونج"})

# الحل النهائي: قاموس lookup معكوس (display -> key)
prop_options_lookup = {v: k for k, v in prop_options.items()}

if prop["has_real_data"]:
    use_real_data = st.sidebar.checkbox(
        t("use_exp_data"),
        value=True,
        key=f"use_real_data_checkbox_{lang_key}",
    )
else:
    use_real_data = False

prop_label = st.sidebar.selectbox(
    t("select_property"),
    list(prop_options_lookup.keys()),
    key=f"prop_label_selector_{lang_key}",
)

# فحص أمان
if prop_label not in prop_options_lookup:
    prop_label = list(prop_options_lookup.keys())[0]

prop_key = prop_options_lookup[prop_label]

# ============================================================
# طاقة التنشيط
# ============================================================
st.sidebar.header(t("ea_header"))

if prop["has_real_data"] and prop_key in prop["experimental_data"]:
    d = prop["experimental_data"][prop_key]
    t_data = np.array(d["t"], dtype=float)
    y_data = np.array(d["y"], dtype=float)
    y0_data = d["y0"]
    with np.errstate(divide='ignore', invalid='ignore'):
        k_vals = (y_data / y0_data - 1) / t_data
    k_vals = k_vals[~np.isnan(k_vals) & ~np.isinf(k_vals)]
    k_obs_calc = float(np.mean(k_vals))
    Ea_kJ = float(prop["Ea_default"])

    if st.session_state.language == "en":
        st.sidebar.info(
            f"**k (from data):** {k_obs_calc:.6f} /day\n\n"
            f"**Ea (from literature):** {Ea_kJ:.0f} kJ/mol"
        )
        st.sidebar.metric("Ea Used", f"{Ea_kJ:.0f} kJ/mol")
    else:
        st.sidebar.info(
            f"**k من بياناتك:** {k_obs_calc:.6f} /day\n\n"
            f"**Ea من الأدبيات:** {Ea_kJ:.0f} kJ/mol"
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
        key=f"ea_slider_{lang_key}",
    )

# ============================================================
# معيار الفشل
# ============================================================
st.sidebar.header(t("failure_criterion"))

if st.session_state.language == "en":
    criteria_list = prop.get("failure_criteria_en", prop["failure_criteria"])
else:
    criteria_list = prop["failure_criteria"]

criterion = st.sidebar.selectbox(
    t("select_criterion"),
    criteria_list,
    key=f"criterion_selector_{lang_key}",
)

if criterion not in criteria_list:
    criterion = criteria_list[0]

# ============================================================
# استخراج الخاصية والنسبة من نص معيار الفشل
# ============================================================
CRITERION_MAP = {
    # Arabic criteria
    "زيادة معامل يونج 20%": ("young_modulus", 20.0),
    "زيادة معامل يونج 25%": ("young_modulus", 25.0),
    "تغير معامل يونج 15%": ("young_modulus", 15.0),
    "زيادة الدفع الأقصى 15%": ("max_thrust", 15.0),
    "زيادة الصلابة Shore A 10%": ("shore_A", 10.0),
    "زيادة الصلابة Shore A 15%": ("shore_A", 15.0),
    "استهلاك 50% من المُثبِّت": ("young_modulus", 50.0),
    "استهلاك 40% من المُثبِّت": ("young_modulus", 40.0),
    "انخفاض Elongation 30%": ("young_modulus", 30.0),
    "انخفاض Elongation 25%": ("young_modulus", 25.0),
    "فقدان وزن 2%": ("young_modulus", 2.0),
    # English criteria
    "Young Modulus increase by 20%": ("young_modulus", 20.0),
    "Young Modulus increase by 25%": ("young_modulus", 25.0),
    "Young Modulus change by 15%": ("young_modulus", 15.0),
    "Max Thrust increase by 15%": ("max_thrust", 15.0),
    "Shore A increase by 10%": ("shore_A", 10.0),
    "Shore A increase by 15%": ("shore_A", 15.0),
    "Stabilizer depletion by 50%": ("young_modulus", 50.0),
    "Stabilizer depletion by 40%": ("young_modulus", 40.0),
    "Elongation decrease by 30%": ("young_modulus", 30.0),
    "Elongation decrease by 25%": ("young_modulus", 25.0),
    "Weight loss 2%": ("young_modulus", 2.0),
}

# تطبيق المعيار على الخاصية والنسبة
if criterion in CRITERION_MAP:
    criterion_prop_key, criterion_threshold = CRITERION_MAP[criterion]
    # التحقق إن الخاصية موجودة في بيانات النوع
    if criterion_prop_key in prop_options_lookup.values():
        prop_key = criterion_prop_key
        prop_label = [k for k, v in prop_options_lookup.items() if v == prop_key][0]
        threshold_pct = criterion_threshold

threshold_pct = st.sidebar.slider(
    t("allowed_change"),
    min_value=5.0, max_value=50.0, value=20.0, step=1.0,
    key=f"threshold_slider_{lang_key}",
)

# ============================================================
# ظروف التخزين
# ============================================================
st.sidebar.header(t("storage_header"))
T_storage_C = st.sidebar.number_input(
    t("storage_temp"),
    value=25.0, step=1.0,
    key=f"storage_temp_input_{lang_key}",
)

# ============================================================
# ظروف الرطوبة
# ============================================================
st.sidebar.header(t("humidity_header"))
use_humidity = st.sidebar.checkbox(
    t("use_humidity"),
    value=False,
    key=f"use_humidity_check_{lang_key}",
)

if use_humidity:
    RH_storage = st.sidebar.slider(
        t("rh_storage"), 0, 100, 50, 1,
        key=f"rh_storage_slider_{lang_key}",
    )
    RH_ref = st.sidebar.number_input(
        t("rh_ref"), value=50, min_value=1, max_value=100,
        key=f"rh_ref_input_{lang_key}",
    )
    n_humidity = st.sidebar.slider(
        t("n_humidity"), 0.5, 3.0, 1.5, 0.1,
        key=f"n_humidity_slider_{lang_key}",
    )
else:
    RH_storage = 50.0
    RH_ref = 50.0
    n_humidity = 1.0

# ============================================================
# الحسابات
# ============================================================
R = 8.314
T_ref_K = 298.15
T_exp_C = 65.0
T_exp_K = T_exp_C + 273.15

Ea = Ea_kJ * 1000
T_storage_K = T_storage_C + 273.15

if prop["has_real_data"] and use_real_data and prop_key in prop.get("experimental_data", {}):
    d = prop["experimental_data"][prop_key]
    t_data_arr = np.array(d["t"], dtype=float)
    y_data_arr = np.array(d["y"], dtype=float)
    y0_data = d["y0"]
    with np.errstate(divide='ignore', invalid='ignore'):
        k_vals = (y_data_arr / y0_data - 1) / t_data_arr
    k_vals = k_vals[~np.isnan(k_vals) & ~np.isinf(k_vals)]
    k_obs = float(np.mean(k_vals))
    data_source = "Experimental data (65°C)"
else:
    k_obs = prop["k_exp_65C"]
    data_source = f"Literature ({prop.get('reference_en', prop['reference'])})"

A_arr = k_obs / np.exp(-Ea / (R * T_exp_K))

def k_at(T_K):
    return A_arr * np.exp(-Ea / (R * T_K))

k_storage = k_at(T_storage_K)
k_ref = k_at(T_ref_K)

if use_humidity:
    RH_factor_storage = (RH_storage / RH_ref) ** n_humidity
    RH_factor_ref = 1.0
else:
    RH_factor_storage = 1.0
    RH_factor_ref = 1.0

AF = (k_storage * RH_factor_storage) / (k_ref * RH_factor_ref)

# ============================================================
# عرض معلومات المعايرة
# ============================================================
if st.session_state.language == "en":
    prop_display_name = prop.get("properties_en", {}).get(prop_key, "Property")
else:
    prop_display_name = prop.get("properties_ar", {}).get(prop_key, prop_label)

st.markdown(f"""
<div class="info-box">
<b>{t("prop_info")}:</b><br>
• <b>{t("propellant_label")}:</b> {propellant_key.split(' - ')[0]}<br>
• <b>{t("governing_property")}:</b> {prop_display_name}<br>
• <b>{t("csv_data")}:</b> {data_source}<br>
• <b>k at 65°C:</b> {k_obs:.6f} /day<br>
• <b>Arrhenius A:</b> {A_arr:.4e} /day
</div>
""", unsafe_allow_html=True)

# ============================================================
# المؤشرات
# ============================================================
st.header(t("results_header"))

col1, col2, col3 = st.columns(3)
col1.metric(t("af_label"), f"{AF:.3f}")
col2.metric(t("k_storage"), f"{k_storage:.4e} /day")
col3.metric(t("k_ref"), f"{k_ref:.4e} /day")

# ============================================================
# العمر الافتراضي
# ============================================================
st.header(t("life_header"))

k_effective = k_storage * RH_factor_storage
t_fail_days = (threshold_pct / 100) / k_effective
t_fail_years = t_fail_days / 365

st.markdown(f"""
<div class="success-box">
    <h2 style="color: #155724; margin: 0;">
    🎯 {t("life_header")}: {t_fail_years:.2f} {t("life_years")}
    </h2>
    <p style="margin: 10px 0 0 0; color: #155724;">
    <b>{t("failure_mode")}:</b> {criterion}<br>
    <b>{t("duration_days")}:</b> {t_fail_days:.0f}
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# رسم التحقق
# ============================================================
if prop["has_real_data"] and use_real_data and prop_key in prop.get("experimental_data", {}):
    st.header(t("validation_header"))
    d = prop["experimental_data"][prop_key]
    t_data_plot = np.array(d["t"], dtype=float)
    y_data_plot = np.array(d["y"], dtype=float)
    y0_plot = d["y0"]

    fig, ax = plt.subplots(figsize=(11, 4.5))
    fig.patch.set_facecolor('#f5f7fa')
    ax.set_facecolor('#ffffff')
    ax.scatter(t_data_plot, y_data_plot, s=120, c='red', zorder=5, label=t("exp_data_label"))
    t_smooth = np.linspace(0, max(t_data_plot) * 1.2, 100)
    y_smooth = y0_plot * (1 + k_obs * t_smooth)
    ax.plot(t_smooth, y_smooth, 'b-', linewidth=2.5, label=t("model_label"))
    ax.set_xlabel('Time (days)')
    ax.set_ylabel(prop_display_name)
    ax.set_title(t("validation_header"))
    ax.legend()
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

# ============================================================
# جدول المقارنة
# ============================================================
st.header(t("comparison_header"))

data_table = []
for T_C in [15, 20, 25, 30, 35, 40, 50, 60, 65]:
    T_K = T_C + 273.15
    k = k_at(T_K) * (RH_factor_storage if use_humidity else 1.0)
    t_y = (threshold_pct / 100) / k / 365
    data_table.append({
        t("temperature"): f"{T_C}",
        t("k_per_day"): f"{k:.4e}",
        t("life_col"): f"{t_y:.2f}" if t_y < 1000 else "> 1000",
    })

st.dataframe(pd.DataFrame(data_table), use_container_width=True)

# ============================================================
# تصدير PDF
# ============================================================
st.markdown("---")
st.header(t("pdf_header"))
st.caption(t("pdf_caption"))


def generate_pdf_report():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(30, 58, 138)
    pdf.cell(0, 12, "Solid Rocket Motor - Aging Simulation Report", ln=True, align="C")
    pdf.ln(3)
    pdf.set_draw_color(30, 58, 138)
    pdf.set_line_width(0.5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)

    pdf.set_font("Arial", "I", 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 6, f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True, align="R")
    pdf.ln(3)

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

    pdf.set_fill_color(212, 237, 218)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"ESTIMATED SHELF LIFE: {t_fail_years:.2f} years ({t_fail_days:.0f} days)",
             ln=True, align="C", fill=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 9, "4. Shelf Life vs Storage Temperature", ln=True)
    pdf.ln(2)
    pdf.set_font("Arial", "B", 10)
    pdf.set_fill_color(230, 230, 230)
    pdf.cell(50, 8, "Temperature (C)", border=1, align="C", fill=True)
    pdf.cell(60, 8, "k (/day)", border=1, align="C", fill=True)
    pdf.cell(60, 8, "Life (years)", border=1, align="C", fill=True)
    pdf.ln()
    pdf.set_font("Arial", "", 10)
    for T_C in [15, 20, 25, 30, 35, 40, 50, 60, 65]:
        T_K = T_C + 273.15
        k = k_at(T_K) * (RH_factor_storage if use_humidity else 1.0)
        t_y = (threshold_pct / 100) / k / 365
        life_str = f"{t_y:.2f}" if t_y < 1000 else "> 1000"
        pdf.cell(50, 7, f"{T_C}", border=1, align="C")
        pdf.cell(60, 7, f"{k:.4e}", border=1, align="C")
        pdf.cell(60, 7, life_str, border=1, align="C")
        pdf.ln()
    pdf.ln(5)

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
        "- Data source used: 65 C Experimental Data",
    ]
    for line in notes:
        pdf.cell(0, 6, line, ln=True)
    pdf.ln(10)

    pdf.set_font("Arial", "I", 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 6, "Generated by: Rocket Aging Simulation Platform", ln=True, align="C")
    pdf.cell(0, 6, "https://rocket-aging-sim.streamlit.app", ln=True, align="C")

    return bytes(pdf.output())


if st.button(t("pdf_generate"), type="primary", key=f"pdf_generate_btn_{lang_key}"):
    try:
        pdf_bytes = generate_pdf_report()
        st.success(t("report_ready"))
        st.download_button(
            label=t("pdf_download"),
            data=pdf_bytes,
            file_name=f"aging_report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
            mime="application/pdf",
            key=f"pdf_download_btn_{lang_key}",
        )
    except Exception as e:
        st.error(f"{t('error')}: {str(e)}")

# ============================================================
# رفع CSV
# ============================================================
st.markdown("---")
st.header(t("csv_header"))
st.caption(t("csv_caption"))

uploaded_file = st.file_uploader(
    t("csv_upload"),
    type=["csv"],
    key=f"csv_uploader_main_{lang_key}",
)

if uploaded_file is not None:
    try:
        df_upload = pd.read_csv(uploaded_file)
        st.success(t("csv_success"))
        st.subheader(t("csv_data"))
        st.dataframe(df_upload, use_container_width=True)

        required_cols = ['temperature_C', 'time_days']
        if all(col in df_upload.columns for col in required_cols):
            property_cols = [c for c in df_upload.columns if c not in required_cols]
            if property_cols:
                selected_prop = st.selectbox(
                    t("select_property_analysis"),
                    property_cols,
                    key=f"csv_prop_selector_{lang_key}",
                )
                st.subheader(t("csv_analysis"))
                results = []
                for T in sorted(df_upload['temperature_C'].unique()):
                    sub = df_upload[df_upload['temperature_C'] == T].dropna(subset=[selected_prop])
                    if len(sub) < 2:
                        continue
                    t_vals = sub['time_days'].values
                    y_vals = sub[selected_prop].values
                    y0 = y_vals[0]
                    with np.errstate(divide='ignore', invalid='ignore'):
                        k_vals = (y_vals / y0 - 1) / t_vals
                    k_vals = k_vals[~np.isnan(k_vals) & ~np.isinf(k_vals)]
                    results.append({
                        'T_C': T, 'T_K': T + 273.15,
                        'k': float(np.mean(k_vals)),
                        'n_points': len(sub),
                    })
                results_df = pd.DataFrame(results)
                st.dataframe(results_df, use_container_width=True)

                if len(results_df) >= 3:
                    inv_T = 1 / results_df['T_K'].values
                    ln_k = np.log(np.abs(results_df['k'].values))
                    slope, intercept = np.polyfit(inv_T, ln_k, 1)
                    Ea_calc = -slope * R / 1000
                    A_calc = np.exp(intercept)
                    st.success(f"Ea = {Ea_calc:.2f} kJ/mol")
                    st.info(f"A = {A_calc:.4e} /day")
                else:
                    st.warning("Need at least 3 temperatures for Ea calculation.")
    except Exception as e:
        st.error(f"{t('error')}: {str(e)}")

# ============================================================
# مقارنة نوعين
# ============================================================
st.markdown("---")
st.header(t("comparison_types"))
st.caption(t("comparison_caption"))

col_a, col_b = st.columns(2)
with col_a:
    type_A = st.selectbox(
        t("type_a"), list(PROPELLANT_TYPES.keys()), index=0,
        key=f"compare_type_A_{lang_key}",
    )
with col_b:
    type_B = st.selectbox(
        t("type_b"), list(PROPELLANT_TYPES.keys()), index=2,
        key=f"compare_type_B_{lang_key}",
    )

if type_A not in PROPELLANT_TYPES:
    type_A = list(PROPELLANT_TYPES.keys())[0]
if type_B not in PROPELLANT_TYPES:
    type_B = list(PROPELLANT_TYPES.keys())[0]

if st.button(t("compare_btn"), type="primary", key=f"compare_btn_key_{lang_key}"):
    prop_A = PROPELLANT_TYPES[type_A]
    prop_B = PROPELLANT_TYPES[type_B]

    results = []
    for name, p in [(type_A, prop_A), (type_B, prop_B)]:
        k_65 = p["k_exp_65C"]
        A_i = k_65 / np.exp(-Ea / (R * T_exp_K))
        k_25 = A_i * np.exp(-Ea / (R * T_ref_K))
        k_stor = A_i * np.exp(-Ea / (R * T_storage_K))
        life_25 = (threshold_pct / 100) / k_25 / 365
        life_stor = (threshold_pct / 100) / k_stor / 365
        results.append({
            "Type": name.split(" - ")[0],
            "k at 65°C": f"{k_65:.4e}",
            "Ea (kJ/mol)": f"{p['Ea_default']:.0f}",
            "Life at 25°C": f"{life_25:.2f}",
            f"Life at {T_storage_C:.0f}°C": f"{life_stor:.2f}",
        })
    df_compare = pd.DataFrame(results).T
    df_compare.columns = ["Type A", "Type B"]
    st.dataframe(df_compare, use_container_width=True)

    st.subheader(t("comparison_curve"))
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
        ax_cmp.plot(temps_plot, life_arr, linewidth=2.5, color=colors[i], label=name.split(" - ")[0])
    ax_cmp.set_xlabel("Temperature (°C)")
    ax_cmp.set_ylabel("Shelf Life (years)")
    ax_cmp.set_title("Shelf Life vs Temperature")
    ax_cmp.set_yscale('log')
    ax_cmp.legend()
    ax_cmp.grid(True, alpha=0.3, which='both')
    st.pyplot(fig_cmp)

# ============================================================
# Monte Carlo
# ============================================================
st.markdown("---")
st.header(t("mc_header"))
st.caption(t("mc_caption"))

col_mc1, col_mc2, col_mc3 = st.columns(3)
with col_mc1:
    n_sim = st.number_input(
        t("mc_n_sim"), value=1000, min_value=100, max_value=10000, step=100,
        key=f"mc_n_sim_{lang_key}",
    )
with col_mc2:
    Ea_uncertainty = st.slider(t("mc_ea_unc"), 0, 30, 10, key=f"mc_ea_unc_{lang_key}")
with col_mc3:
    k_uncertainty = st.slider(t("mc_k_unc"), 0, 50, 20, key=f"mc_k_unc_{lang_key}")

if st.button(t("mc_run"), type="primary", key=f"mc_run_btn_{lang_key}"):
    np.random.seed(42)
    Ea_samples = np.random.normal(Ea_kJ, Ea_kJ * Ea_uncertainty / 100, n_sim)
    k_65_samples = np.random.normal(k_obs, k_obs * k_uncertainty / 100, n_sim)
    Ea_samples = np.abs(Ea_samples)
    k_65_samples = np.abs(k_65_samples)
    life_samples = []
    for Ea_i, k_65_i in zip(Ea_samples, k_65_samples):
        A_i = k_65_i / np.exp(-Ea_i * 1000 / (R * T_exp_K))
        k_stor_i = A_i * np.exp(-Ea_i * 1000 / (R * T_storage_K))
        life_i = (threshold_pct / 100) / k_stor_i / 365
        life_samples.append(life_i)
    life_samples = np.array(life_samples)

    st.subheader(t("mc_results"))
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(t("mc_mean"), f"{np.mean(life_samples):.2f} {t('years')}")
    c2.metric(t("mc_median"), f"{np.median(life_samples):.2f} {t('years')}")
    c3.metric(t("mc_p5"), f"{np.percentile(life_samples, 5):.2f} {t('years')}")
    c4.metric(t("mc_p95"), f"{np.percentile(life_samples, 95):.2f} {t('years')}")

    fig_mc, ax_mc = plt.subplots(figsize=(11, 5))
    fig_mc.patch.set_facecolor('#f5f7fa')
    ax_mc.set_facecolor('#ffffff')
    ax_mc.hist(life_samples, bins=50, color='steelblue', edgecolor='white', alpha=0.8)
    ax_mc.axvline(np.mean(life_samples), color='red', linestyle='--', linewidth=2, label=t("mc_mean"))
    ax_mc.axvline(np.percentile(life_samples, 5), color='orange', linestyle=':', linewidth=2, label=t("mc_p5"))
    ax_mc.axvline(np.percentile(life_samples, 95), color='green', linestyle=':', linewidth=2, label=t("mc_p95"))
    ax_mc.set_xlabel("Shelf Life (years)")
    ax_mc.set_ylabel("Frequency")
    ax_mc.set_title(f"Monte Carlo Distribution ({n_sim} runs)")
    ax_mc.legend()
    ax_mc.grid(True, alpha=0.3)
    st.pyplot(fig_mc)

# ============================================================
# Abaqus Export
# ============================================================
st.markdown("---")
st.header(t("abaqus_header"))
st.caption(t("abaqus_caption"))

col_abq1, col_abq2 = st.columns(2)

with col_abq1:
    if st.button(t("abaqus_inp"), type="primary", key=f"abq_inp_btn_{lang_key}"):
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
** Storage Temperature: {T_storage_C} C
** Humidity: {RH_storage if use_humidity else 50} %
** Shelf Life: {t_fail_years:.2f} years
** Ea: {Ea_kJ} kJ/mol
** k at 65C: {k_obs:.6f} /day
"""
        st.download_button(
            label="Download INP",
            data=inp_content.encode('utf-8'),
            file_name=f"propellant_aging_{datetime.now().strftime('%Y%m%d_%H%M')}.inp",
            mime="text/plain",
            key=f"abq_inp_dl_{lang_key}",
        )

with col_abq2:
    if st.button(t("abaqus_py"), type="primary", key=f"abq_py_btn_{lang_key}"):
        py_content = f'''# Abaqus Python Script - Aging Simulation
from abaqus import *
from abaqusConstants import *
from caeModules import *

model_name = 'PropellantAging'
mdb.Model(name=model_name)
mat = mdb.models[model_name].Material(name='PROPELLANT')
mat.Elastic(table=(({Ea_kJ * 10:.2f}, 0.4999), ))
mat.Density(table=(({prop.get('density', 1700.0) / 1e6:.4e}, ), ))
mat.Hyperelastic(materialType=NEO_HOOKE, table=((0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), ))
mat.Viscoelastic(domain=TIME, time=PRONY, table=((0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
                                                 (0.05, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
                                                 (0.02, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)))
print("Material created successfully.")
'''
        st.download_button(
            label="Download Python Script",
            data=py_content.encode('utf-8'),
            file_name=f"abaqus_script_{datetime.now().strftime('%Y%m%d_%H%M')}.py",
            mime="text/x-python",
            key=f"abq_py_dl_{lang_key}",
        )

with st.expander(t("abaqus_guide")):
    st.markdown("""
    ### Steps to run in Abaqus:
    1. Download INP file and Python script.
    2. Open Abaqus/CAE → File → Run Script.
    3. Select the Python script.
    4. The material will be created automatically.
    
    ### Data provided:
    - Elastic modulus, Poisson's ratio
    - Density
    - Hyperelastic (Neo-Hookean)
    - Viscoelastic (Prony series)
    - Aging conditions
    """)

# ============================================================
# Footer
# ============================================================
st.markdown("---")
st.caption("Rocket Aging Simulation Platform | v2.3 | 2026")
