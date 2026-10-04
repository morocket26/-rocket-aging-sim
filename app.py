# -*- coding: utf-8 -*-
"""Solid rocket propellant aging simulation platform (AR/EN)."""
import re
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from fpdf import FPDF  # requires fpdf2

from kinetics import (R, T_EXP_K, T_REF_K, arrhenius_k, fit_k, humidity_factor,
                      life_days, life_years, lognormal)

# ------------------------------------------------------------------ i18n
# key: (arabic, english)
TR = {
    "title": ("🚀 منصة محاكاة اختبارات التقادم", "🚀 Aging Simulation Platform"),
    "caption": ("وقود صاروخي صلب | معايرة ببيانات تجريبية", "Solid rocket propellant | Data-calibrated"),
    "propellant": ("🔥 نوع الوقود", "🔥 Propellant Type"),
    "prop_info": ("📌 معلومات النوع", "📌 Propellant Info"),
    "name": ("الاسم", "Name"), "aging": ("آلية التقادم", "Aging Mechanism"),
    "stab": ("المُثبِّتات", "Stabilizers"), "ref": ("المرجع", "Reference"),
    "gov_prop": ("🎯 الخاصية الحاكمة", "🎯 Governing Property"),
    "use_exp": ("استخدام البيانات التجريبية (65°C)", "Use Experimental Data (65°C)"),
    "ea_hdr": ("🌡️ طاقة التنشيط Ea", "🌡️ Activation Energy Ea"),
    "crit_hdr": ("⚠️ معيار الفشل", "⚠️ Failure Criterion"),
    "allowed": ("النسبة المسموحة (%)", "Allowed Change (%)"),
    "storage_hdr": ("📦 ظروف التخزين", "📦 Storage Conditions"),
    "storage_t": ("درجة حرارة التخزين (°C)", "Storage Temperature (°C)"),
    "hum_hdr": ("💧 ظروف الرطوبة", "💧 Humidity Conditions"),
    "use_hum": ("تفعيل تأثير الرطوبة (Peck)", "Enable Humidity Effect (Peck)"),
    "rh": ("الرطوبة النسبية (%)", "Relative Humidity (%)"),
    "rh_ref": ("الرطوبة المرجعية (%)", "Reference Humidity (%)"),
    "n_hum": ("معامل الرطوبة n", "Humidity exponent n"),
    "results": ("📊 النتائج", "📊 Results"),
    "af": ("⚡ معامل التسريع (65°C ÷ التخزين)", "⚡ Acceleration Factor (65°C ÷ storage)"),
    "k_stor": ("🌡️ k عند التخزين", "🌡️ k at storage"),
    "k25": ("📅 k عند 25°C", "📅 k at 25°C"),
    "life_hdr": ("⏳ العمر الافتراضي", "⏳ Estimated Shelf Life"),
    "years": ("سنة", "years"), "days": ("المدة بالأيام", "Duration in days"),
    "crit": ("معيار الفشل", "Failure criterion"),
    "extrap": ("⚠️ التقدير استقراء من نقطة حرارة واحدة (65°C) مع Ea من الأدبيات؛ قيمة Ea تحدد النتيجة تقريبًا بالكامل. راجع نطاق Monte Carlo أدناه.",
               "⚠️ This is an extrapolation from a single temperature (65°C) with a literature Ea; Ea almost fully determines the result. See the Monte Carlo range below."),
    "table_hdr": ("🌡️ العمر عند درجات حرارة مختلفة", "🌡️ Shelf Life at Different Temperatures"),
    "temp": ("الحرارة (°C)", "Temperature (°C)"), "life_col": ("العمر (سنة)", "Life (years)"),
    "valid_hdr": ("🔬 المعايرة: النموذج مقابل البيانات", "🔬 Calibration: model vs data"),
    "few_pts": ("عدد النقاط أقل من 3؛ الملاءمة غير موثوقة.", "Fewer than 3 points; the fit is not reliable."),
    "pdf_hdr": ("📄 تصدير تقرير PDF", "📄 Export PDF Report"),
    "pdf_gen": ("📥 إنشاء التقرير", "📥 Generate PDF"), "pdf_dl": ("💾 تحميل التقرير", "💾 Download PDF"),
    "csv_hdr": ("📤 رفع بيانات تجريبية (CSV)", "📤 Upload Experimental Data (CSV)"),
    "csv_cap": ("الأعمدة المطلوبة: temperature_C, time_days + عمود لكل خاصية. الصف t=0 مطلوب لكل درجة حرارة.",
                "Required columns: temperature_C, time_days + one column per property. A t=0 row is required for each temperature."),
    "csv_up": ("اختر ملف CSV", "Choose CSV file"), "csv_sel": ("اختر الخاصية", "Select property"),
    "csv_need": ("يلزم 3 درجات حرارة على الأقل لحساب Ea.", "Need at least 3 temperatures to compute Ea."),
    "csv_cols": ("الأعمدة المطلوبة غير موجودة.", "Required columns missing."),
    "cmp_hdr": ("⚔️ مقارنة بين نوعين", "⚔️ Compare Two Propellants"),
    "cmp_cap": ("كل نوع يستخدم Ea و k الخاصين به، مع درجة حرارة التخزين والرطوبة المختارة.",
                "Each type uses its own Ea and k, at the selected storage temperature and humidity."),
    "type_a": ("النوع A", "Type A"), "type_b": ("النوع B", "Type B"),
    "mc_hdr": ("🎲 Monte Carlo", "🎲 Monte Carlo"),
    "mc_cap": ("توزيع لوغاريتمي-طبيعي لـ Ea و k (مستقلان).", "Lognormal sampling of Ea and k (independent)."),
    "mc_n": ("عدد المحاكاة", "Simulations"), "mc_ea": ("عدم اليقين في Ea (%)", "Ea uncertainty (%)"),
    "mc_k": ("عدم اليقين في k (%)", "k uncertainty (%)"),
    "mc_mean": ("المتوسط", "Mean"), "mc_med": ("الوسيط", "Median"),
    "mc_p5": ("P5 (تحفظي)", "P5 (conservative)"), "mc_p95": ("P95 (متفائل)", "P95 (optimistic)"),
    "abq_hdr": ("🔧 تصدير إلى Abaqus", "🔧 Export to Abaqus"),
    "abq_cap": ("قالب مادة Neo-Hooke من معامل يونج التجريبي (غير مسن / مسن). سلسلة Prony مجرد قيم افتراضية يجب استبدالها.",
                "Neo-Hookean material template from the experimental Young's modulus (unaged / aged). The Prony series is a PLACEHOLDER you must replace."),
    "abq_inp": ("📄 تحميل INP", "📄 Download INP"), "abq_py": ("🐍 تحميل سكريبت Python", "🐍 Download Python script"),
    "abq_na": ("التصدير يتطلب بيانات معامل يونج تجريبية (اختر الخاصية واستخدم البيانات التجريبية).",
               "Export needs experimental Young's modulus data (select that property and enable experimental data)."),
    "abq_guide": ("📖 دليل Abaqus", "📖 Abaqus guide"),
    "abq_guide_txt": ("1. حمّل الملف. 2. استبدل سلسلة Prony ببيانات DMA/استرخاء. 3. تحقق من الوحدات (MPa, mm, tonne). 4. في CAE: File → Run Script.",
                      "1. Download the file. 2. Replace the Prony series with DMA/relaxation data. 3. Check units (MPa, mm, tonne). 4. In CAE: File → Run Script."),
    "err": ("خطأ", "Error"),
}

# ------------------------------------------------------------------ database
PROPELLANTS = {
    "CMDB": {
        "full": "CMDB - Composite Modified DB", "Ea": 125.0, "Ea_range": (110.0, 140.0), "k65": 0.0048,
        "aging": ("استهلاك المُثبِّت + أكسدة AP/Al", "Stabilizer depletion (2-NDPA, Carbamite) + AP/NG interaction"),
        "stab": ("2-NDPA + مضادات أكسدة", "2-NDPA, Carbamite (EC), MNA"),
        "ref": "HELL FIRE Motor Test (1998) + Asthana et al.",
        "props": {"young_modulus": ("معامل يونج", "Young Modulus"), "shore_A": ("الصلابة Shore A", "Shore A Hardness"),
                  "max_thrust": ("الدفع الأقصى", "Max Thrust")},
        "criteria": [("زيادة معامل يونج 20%", "Young Modulus increase by 20%", 20),
                     ("زيادة الدفع الأقصى 15%", "Max Thrust increase by 15%", 15),
                     ("زيادة الصلابة Shore A 10%", "Shore A increase by 10%", 10)],
        "exp": {"young_modulus": {"t": [0, 10, 20, 35], "y": [15.26, 17.05, 17.35, 17.83], "y0": 15.26, "unit": "kg/cm²"},
                "shore_A": {"t": [0, 10, 20, 35], "y": [45, 46, 46, 47], "y0": 45.0, "unit": "-"},
                "max_thrust": {"t": [0, 35], "y": [988, 1062], "y0": 988.0, "unit": "dan"}},
    },
    "DB": {
        "full": "DB - Double Base", "Ea": 115.0, "Ea_range": (100.0, 130.0), "k65": 0.0048,
        "aging": ("تحلل الإسترات النيتراتية", "Nitrate ester decomposition"),
        "stab": ("2-NDPA, Ethyl Centralite, Akardite II", "2-NDPA, Ethyl Centralite, Akardite II"),
        "ref": "NATO STO-MP-AVT-268 (2017)",
        "props": {"young_modulus": ("معامل يونج", "Young Modulus"), "shore_A": ("الصلابة Shore A", "Shore A Hardness")},
        "criteria": [("زيادة معامل يونج 20%", "Young Modulus increase by 20%", 20),
                     ("زيادة الصلابة Shore A 10%", "Shore A increase by 10%", 10)],
        "exp": None,
    },
    "HTPB/AP": {
        "full": "Composite - HTPB/AP", "Ea": 90.0, "Ea_range": (80.0, 100.0), "k65": 0.0035,
        "aging": ("أكسدة الـ binder + روابط عرضية", "Binder oxidation + crosslinking"),
        "stab": ("مضادات أكسدة", "Antioxidants"), "ref": "Shekhar, Prediction of Shelf Life (2014)",
        "props": {"young_modulus": ("معامل يونج", "Young Modulus"), "shore_A": ("الصلابة Shore A", "Shore A Hardness")},
        "criteria": [("زيادة الصلابة Shore A 15%", "Shore A increase by 15%", 15),
                     ("زيادة معامل يونج 25%", "Young Modulus increase by 25%", 25)],
        "exp": None,
    },
    "NEPE": {
        "full": "NEPE - Nitrate Ester Plasticized", "Ea": 135.0, "Ea_range": (120.0, 150.0), "k65": 0.0080,
        "aging": ("تحلل الإسترات + هجرة plasticizer", "Nitrate ester decomposition + plasticizer migration"),
        "stab": ("مُثبِّتات خاصة", "Special stabilizers"), "ref": "NATO STO-TR-AVT-171",
        "props": {"young_modulus": ("معامل يونج", "Young Modulus"), "shore_A": ("الصلابة Shore A", "Shore A Hardness")},
        "criteria": [("تغير معامل يونج 15%", "Young Modulus change by 15%", 15)],
        "exp": None,
    },
    "HTPE": {
        "full": "HTPE - High Performance", "Ea": 100.0, "Ea_range": (90.0, 110.0), "k65": 0.0040,
        "aging": ("أكسدة البوليمر", "Polymer oxidation"), "stab": ("مضادات أكسدة", "Antioxidants"),
        "ref": "Insensitive Munitions Program Reports",
        "props": {"young_modulus": ("معامل يونج", "Young Modulus"), "shore_A": ("الصلابة Shore A", "Shore A Hardness")},
        "criteria": [("زيادة معامل يونج 20%", "Young Modulus increase by 20%", 20)],
        "exp": None,
    },
}
TEMPS_C = [15, 20, 25, 30, 35, 40, 50, 60, 65]

# ------------------------------------------------------------------ page + language
st.set_page_config(page_title="Aging Simulation", page_icon="🚀", layout="wide")
st.markdown("""<style>
h1{color:#1e3a8a;text-align:center}
.stMetric{background:white;padding:15px;border-radius:10px;box-shadow:0 2px 8px rgba(0,0,0,.1)}
.success-box{background:#d4edda;padding:20px;border-radius:10px;border-right:5px solid #28a745;color:#155724}
</style>""", unsafe_allow_html=True)

lang_choice = st.sidebar.radio("🌐 اللغة / Language", ["العربية", "English"], horizontal=True, key="lang")
EN = lang_choice == "English"


def t(key):
    return TR[key][1 if EN else 0]


def pick(pair):
    return pair[1 if EN else 0]


def show_fig(fig):
    st.pyplot(fig)
    plt.close(fig)


def ascii_safe(s):
    return re.sub(r"[^\x20-\x7E]", "", str(s))


# ------------------------------------------------------------------ sidebar
st.title(t("title"))
st.caption(t("caption"))

st.sidebar.header(t("propellant"))
pkey = st.sidebar.selectbox(t("propellant"), list(PROPELLANTS), format_func=lambda k: PROPELLANTS[k]["full"],
                            key="propellant", label_visibility="collapsed")
prop = PROPELLANTS[pkey]
st.sidebar.markdown(
    f"**{t('prop_info')}**\n- **{t('name')}:** {pkey}\n- **{t('aging')}:** {pick(prop['aging'])}\n"
    f"- **{t('stab')}:** {pick(prop['stab'])}\n- **{t('ref')}:** {prop['ref']}")

st.sidebar.header(t("gov_prop"))
prop_key = st.sidebar.selectbox(t("gov_prop"), list(prop["props"]), format_func=lambda k: pick(prop["props"][k]),
                                key=f"prop_{pkey}", label_visibility="collapsed")
exp = (prop["exp"] or {}).get(prop_key)
use_exp = False
if exp:
    use_exp = st.sidebar.checkbox(t("use_exp"), value=True, key=f"useexp_{pkey}_{prop_key}")

st.sidebar.header(t("ea_hdr"))
lo, hi = prop["Ea_range"]
Ea_kJ = st.sidebar.slider("Ea (kJ/mol)", lo, hi, prop["Ea"], 1.0, key=f"ea_{pkey}")

st.sidebar.header(t("crit_hdr"))
ci = st.sidebar.selectbox(t("crit_hdr"), range(len(prop["criteria"])), format_func=lambda i: pick(prop["criteria"][i][:2]),
                          key=f"crit_{pkey}", label_visibility="collapsed")
criterion = pick(prop["criteria"][ci][:2])
threshold_pct = st.sidebar.slider(t("allowed"), 5.0, 50.0, float(prop["criteria"][ci][2]), 1.0, key=f"thr_{pkey}_{ci}")

st.sidebar.header(t("storage_hdr"))
T_storage_C = st.sidebar.number_input(t("storage_t"), value=25.0, min_value=-60.0, max_value=120.0, step=1.0, key="T_storage")

st.sidebar.header(t("hum_hdr"))
use_hum = st.sidebar.checkbox(t("use_hum"), value=False, key="use_hum")
if use_hum:
    RH = st.sidebar.slider(t("rh"), 1, 100, 50, 1, key="rh")
    RH_ref = st.sidebar.number_input(t("rh_ref"), value=50, min_value=1, max_value=100, key="rh_ref")
    n_hum = st.sidebar.slider(t("n_hum"), 0.5, 3.0, 1.5, 0.1, key="n_hum")
    rh_f = float(humidity_factor(RH, RH_ref, n_hum))
else:
    RH, RH_ref, n_hum, rh_f = 50, 50, 1.0, 1.0

# ------------------------------------------------------------------ calculation
Ea_J = Ea_kJ * 1000.0
T_storage_K = T_storage_C + 273.15

r2_fit = None
if use_exp:
    k65, r2_fit = fit_k(exp["t"], exp["y"], exp["y0"])
    data_source = "Experimental data (65°C), LSQ fit"
else:
    k65 = prop["k65"]
    data_source = f"Literature ({prop['ref']}), same k for all properties"

k_stor = float(arrhenius_k(k65, T_EXP_K, Ea_J, T_storage_K)) * rh_f
k25 = float(arrhenius_k(k65, T_EXP_K, Ea_J, T_REF_K))
AF = k65 / k_stor
t_days = float(life_days(threshold_pct, k_stor))
t_years = t_days / 365.0

st.info(f"**{pkey}** | {pick(prop['props'][prop_key])} | {data_source} | k(65°C) = {k65:.5f} /day")

st.header(t("results"))
c1, c2, c3 = st.columns(3)
c1.metric(t("af"), f"{AF:.3g}")
c2.metric(t("k_stor"), f"{k_stor:.3e} /day")
c3.metric(t("k25"), f"{k25:.3e} /day")

st.header(t("life_hdr"))
life_txt = f"{t_years:.3g}" if t_years < 1000 else "> 1000"
st.markdown(f"""<div class="success-box"><h2 style="margin:0">🎯 {t('life_hdr')}: ~{life_txt} {t('years')}</h2>
<p style="margin:10px 0 0 0"><b>{t('crit')}:</b> {criterion}<br><b>{t('days')}:</b> {t_days:.0f}</p></div>""",
            unsafe_allow_html=True)
st.write("")
st.warning(t("extrap"))

if use_exp:
    st.header(t("valid_hdr"))
    if len(exp["t"]) < 3:
        st.warning(t("few_pts"))
    fig, ax = plt.subplots(figsize=(11, 4.5))
    ax.scatter(exp["t"], exp["y"], s=100, c="red", zorder=5, label="Experimental data")
    ts = np.linspace(0, max(exp["t"]) * 1.2, 100)
    ax.plot(ts, exp["y0"] * (1 + k65 * ts), "b-", lw=2.5, label="Linear model")
    ax.set_xlabel("Time (days)")
    ax.set_ylabel(f"{prop['props'][prop_key][1]} [{exp['unit']}]")
    ax.set_title(f"Calibration (R² = {r2_fit:.3f})" if np.isfinite(r2_fit) else "Calibration")
    ax.legend()
    ax.grid(alpha=0.3)
    show_fig(fig)

st.header(t("table_hdr"))
rows = []
for T_C in TEMPS_C:
    k = float(arrhenius_k(k65, T_EXP_K, Ea_J, T_C + 273.15)) * rh_f
    ty = float(life_years(threshold_pct, k))
    rows.append({t("temp"): T_C, "k (/day)": f"{k:.4e}", t("life_col"): f"{ty:.3g}" if ty < 1000 else "> 1000"})
st.dataframe(pd.DataFrame(rows), width="stretch")

# ------------------------------------------------------------------ Monte Carlo (live)
st.markdown("---")
st.header(t("mc_hdr"))
st.caption(t("mc_cap"))
m1, m2, m3 = st.columns(3)
n_sim = m1.number_input(t("mc_n"), value=2000, min_value=100, max_value=20000, step=100, key="mc_n")
ea_unc = m2.slider(t("mc_ea"), 0, 30, 10, key="mc_ea")
k_unc = m3.slider(t("mc_k"), 0, 50, 20, key="mc_k")

rng = np.random.default_rng(42)
Ea_s = lognormal(rng, Ea_J, ea_unc / 100, int(n_sim))
k65_s = lognormal(rng, k65, k_unc / 100, int(n_sim))
life_s = life_years(threshold_pct, arrhenius_k(k65_s, T_EXP_K, Ea_s, T_storage_K) * rh_f)
p5, p50, p95 = np.percentile(life_s, [5, 50, 95])

q1, q2, q3, q4 = st.columns(4)
q1.metric(t("mc_mean"), f"{life_s.mean():.3g} {t('years')}")
q2.metric(t("mc_med"), f"{p50:.3g} {t('years')}")
q3.metric(t("mc_p5"), f"{p5:.3g} {t('years')}")
q4.metric(t("mc_p95"), f"{p95:.3g} {t('years')}")

fig, ax = plt.subplots(figsize=(11, 4.5))
ax.hist(np.clip(life_s, 0, np.percentile(life_s, 99)), bins=50, color="steelblue", edgecolor="white", alpha=0.85)
ax.axvline(p5, color="orange", ls=":", lw=2, label="P5")
ax.axvline(p50, color="red", ls="--", lw=2, label="Median")
ax.axvline(p95, color="green", ls=":", lw=2, label="P95")
ax.set_xlabel("Shelf life (years)")
ax.set_ylabel("Frequency")
ax.set_title(f"Monte Carlo ({int(n_sim)} runs)")
ax.legend()
ax.grid(alpha=0.3)
show_fig(fig)

# ------------------------------------------------------------------ comparison (live)
st.markdown("---")
st.header(t("cmp_hdr"))
st.caption(t("cmp_cap"))
ca, cb = st.columns(2)
type_A = ca.selectbox(t("type_a"), list(PROPELLANTS), index=0, key="cmp_A")
type_B = cb.selectbox(t("type_b"), list(PROPELLANTS), index=2, key="cmp_B")

cmp_rows, temps = {}, np.linspace(15, 70, 50)
fig, ax = plt.subplots(figsize=(11, 5))
for name, color in [(type_A, "steelblue"), (type_B, "crimson")]:
    p = PROPELLANTS[name]
    Ea_i = p["Ea"] * 1000.0
    k_25 = float(arrhenius_k(p["k65"], T_EXP_K, Ea_i, T_REF_K))
    k_st = float(arrhenius_k(p["k65"], T_EXP_K, Ea_i, T_storage_K)) * rh_f
    cmp_rows[name] = {
        "k at 65°C": f"{p['k65']:.4e}", "Ea (kJ/mol)": f"{p['Ea']:.0f}",
        "Life at 25°C (yr)": f"{float(life_years(threshold_pct, k_25)):.3g}",
        f"Life at {T_storage_C:.0f}°C (yr)": f"{float(life_years(threshold_pct, k_st)):.3g}",
    }
    ax.plot(temps, life_years(threshold_pct, arrhenius_k(p["k65"], T_EXP_K, Ea_i, temps + 273.15) * rh_f),
            lw=2.5, color=color, label=name)
st.dataframe(pd.DataFrame(cmp_rows), width="stretch")
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Shelf life (years)")
ax.set_yscale("log")
ax.set_title("Shelf life vs temperature")
ax.legend()
ax.grid(alpha=0.3, which="both")
show_fig(fig)

# ------------------------------------------------------------------ CSV upload
st.markdown("---")
st.header(t("csv_hdr"))
st.caption(t("csv_cap"))
up = st.file_uploader(t("csv_up"), type=["csv"], key="csv_up")
if up is not None:
    try:
        df = pd.read_csv(up)
        st.dataframe(df, width="stretch")
        if not {"temperature_C", "time_days"} <= set(df.columns):
            st.error(t("csv_cols"))
        else:
            cols = [c for c in df.columns if c not in ("temperature_C", "time_days")]
            sel = st.selectbox(t("csv_sel"), cols, key="csv_prop") if cols else None
            if sel:
                res = []
                for T in sorted(df["temperature_C"].unique()):
                    sub = df[df["temperature_C"] == T].dropna(subset=[sel]).sort_values("time_days")
                    base = sub[sub["time_days"] == 0]
                    if len(sub) < 3 or base.empty or base[sel].iloc[0] == 0:
                        st.warning(f"{T}°C: need a t=0 row and ≥3 points; skipped.")
                        continue
                    k, r2 = fit_k(sub["time_days"], sub[sel], base[sel].iloc[0])
                    res.append({"T_C": T, "T_K": T + 273.15, "k": k, "R2": r2, "n_points": len(sub)})
                rdf = pd.DataFrame(res)
                st.dataframe(rdf, width="stretch")
                pos = rdf[rdf["k"] > 0] if not rdf.empty else rdf
                if len(pos) < len(rdf):
                    st.warning("Non-positive k values excluded from the Arrhenius fit.")
                if len(pos) >= 3:
                    x, y = 1 / pos["T_K"].values, np.log(pos["k"].values)
                    slope, icpt = np.polyfit(x, y, 1)
                    r2a = 1 - np.sum((y - (slope * x + icpt)) ** 2) / np.sum((y - y.mean()) ** 2)
                    st.success(f"Ea = {-slope * R / 1000:.2f} kJ/mol | R² = {r2a:.3f}")
                    st.info(f"A = {np.exp(icpt):.4e} /day")
                else:
                    st.warning(t("csv_need"))
    except Exception as e:  # noqa: BLE001
        st.error(f"{t('err')}: {e}")

# ------------------------------------------------------------------ PDF
st.markdown("---")
st.header(t("pdf_hdr"))


def generate_pdf():
    pdf = FPDF()
    pdf.add_page()

    def line(text, h=6, **kw):
        pdf.cell(0, h, ascii_safe(text), new_x="LMARGIN", new_y="NEXT", **kw)

    def head(text):
        pdf.set_font("Helvetica", "B", 13)
        line(text, 9)
        pdf.set_font("Helvetica", "", 10)

    pdf.set_font("Helvetica", "B", 18)
    line("Solid Rocket Motor - Aging Simulation Report", 12, align="C")
    pdf.set_font("Helvetica", "I", 10)
    line(f"Report date: {datetime.now():%Y-%m-%d %H:%M}", align="R")
    head("1. Propellant")
    for s in (f"Type: {prop['full']}", f"Aging mechanism: {prop['aging'][1]}",
              f"Stabilizers: {prop['stab'][1]}", f"Reference: {prop['ref']}"):
        line("  - " + s)
    head("2. Parameters")
    for s in (f"Governing property: {prop['props'][prop_key][1]}", f"Ea: {Ea_kJ:.1f} kJ/mol",
              f"k at 65 C: {k65:.5f} /day ({data_source})", f"Failure criterion: {prop['criteria'][ci][1]}",
              f"Allowed change: {threshold_pct:.1f} %", f"Storage temperature: {T_storage_C:.1f} C",
              "Humidity: " + (f"RH {RH}% (ref {RH_ref}%), n={n_hum}" if use_hum else "not applied")):
        line("  - " + s)
    head("3. Results")
    for s in (f"Acceleration factor (65 C / storage): {AF:.3g}", f"k at storage: {k_stor:.4e} /day",
              f"k at 25 C: {k25:.4e} /day", f"Monte Carlo life (P5 / median / P95): {p5:.3g} / {p50:.3g} / {p95:.3g} years"):
        line("  - " + s)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_fill_color(212, 237, 218)
    line(f"ESTIMATED SHELF LIFE: ~{life_txt} years ({t_days:.0f} days)", 10, align="C", fill=True)
    head("4. Shelf life vs storage temperature")
    pdf.set_font("Helvetica", "B", 10)
    for w, h in ((50, "Temperature (C)"), (60, "k (/day)"), (60, "Life (years)")):
        pdf.cell(w, 8, h, border=1, align="C")
    pdf.ln()
    pdf.set_font("Helvetica", "", 10)
    for r in rows:
        for w, v in zip((50, 60, 60), r.values()):
            pdf.cell(w, 7, str(v), border=1, align="C")
        pdf.ln()
    pdf.ln(4)
    head("5. Notes")
    for s in ("Estimate based on linear property growth and Arrhenius kinetics.",
              "Extrapolation from one temperature; verify experimentally before critical decisions.",
              "Experimental data at 3+ temperatures is recommended."):
        line("- " + s)
    return bytes(pdf.output())


if st.button(t("pdf_gen"), type="primary", key="pdf_btn"):
    try:
        st.session_state["pdf_bytes"] = generate_pdf()
    except Exception as e:  # noqa: BLE001
        st.error(f"{t('err')}: {e}")
if "pdf_bytes" in st.session_state:
    st.download_button(t("pdf_dl"), st.session_state["pdf_bytes"],
                       file_name=f"aging_report_{datetime.now():%Y%m%d_%H%M}.pdf", mime="application/pdf", key="pdf_dl")

# ------------------------------------------------------------------ Abaqus
st.markdown("---")
st.header(t("abq_hdr"))
st.caption(t("abq_cap"))

NU, DENSITY = 0.495, 1.7e-9   # tonne/mm^3 (= 1700 kg/m^3); ASSUMED, replace with measured density


def neo_hooke(E_mpa):
    c10 = E_mpa / 6.0
    d1 = 2.0 / (E_mpa / (3.0 * (1 - 2 * NU)))
    return c10, d1


PRONY = ((0.1, 0.0, 1.0), (0.05, 0.0, 10.0), (0.02, 0.0, 100.0))   # PLACEHOLDER (g_i, k_i, tau_i)

if use_exp and prop_key == "young_modulus" and exp["unit"] == "kg/cm²":
    E0 = exp["y0"] * 0.0980665                     # kg/cm² -> MPa
    E1 = E0 * (1 + threshold_pct / 100.0)
    mats = {"PROPELLANT_UNAGED": E0, "PROPELLANT_AGED": E1}

    inp = ["*HEADING", f"Propellant: {pkey} | storage {T_storage_C} C | shelf life ~{life_txt} yr",
           "** Units: MPa, mm, tonne. Prony series is a PLACEHOLDER - replace with measured data.", "**"]
    for name, E in mats.items():
        c10, d1 = neo_hooke(E)
        inp += [f"*MATERIAL, NAME={name}", "*DENSITY", f"{DENSITY:.4e},", "*HYPERELASTIC, NEO HOOKE", f"{c10:.5f}, {d1:.5f}",
                "*VISCOELASTIC, TIME=PRONY"] + [f"{g}, {k}, {tau}" for g, k, tau in PRONY] + ["**"]
    inp_text = "\n".join(inp) + "\n"

    py = ["# Abaqus/CAE script - propellant materials (Prony series is a PLACEHOLDER)",
          "from abaqus import *", "from abaqusConstants import *", "from caeModules import *", "",
          "m = mdb.Model(name='PropellantAging')"]
    for name, E in mats.items():
        c10, d1 = neo_hooke(E)
        py += [f"mat = m.Material(name='{name}')", f"mat.Density(table=(({DENSITY:.4e},),))",
               f"mat.Hyperelastic(type=NEO_HOOKE, testData=OFF, table=(({c10:.5f}, {d1:.5f}),))",
               f"mat.Viscoelastic(domain=TIME, time=PRONY, table={PRONY!r})"]
    py_text = "\n".join(py) + "\n"

    d1c, d2c = st.columns(2)
    d1c.download_button(t("abq_inp"), inp_text.encode(), file_name=f"propellant_{datetime.now():%Y%m%d_%H%M}.inp",
                        mime="text/plain", key="abq_inp")
    d2c.download_button(t("abq_py"), py_text.encode(), file_name=f"abaqus_script_{datetime.now():%Y%m%d_%H%M}.py",
                        mime="text/x-python", key="abq_py")
else:
    st.info(t("abq_na"))

with st.expander(t("abq_guide")):
    st.markdown(t("abq_guide_txt"))

st.markdown("---")
st.caption("Rocket Aging Simulation Platform | v3.0")
