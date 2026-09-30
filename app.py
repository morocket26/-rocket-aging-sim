# -*- coding: utf-8 -*-
"""
حاسبة العمر الافتراضي - محرك صاروخي صلب
نموذج مبسط لتقدير Shelf Life بناءً على ظروف التخزين
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ==================== الإعدادات العامة ====================
st.set_page_config(page_title="حاسبة العمر الافتراضي", page_icon="🚀", layout="wide")
st.title("🚀 حاسبة العمر الافتراضي - محرك صاروخي صلب")
st.caption("نموذج مبسط لتقدير Shelf Life بناءً على ظروف التخزين ومعيار فشل")

R = 8.314          # ثابت الغازات العام J/mol.K
T_ref = 293.15     # درجة الحرارة المرجعية (20°C)

# ==================== الشريط الجانبي: المدخلات ====================
st.sidebar.header("🔧 بيانات المحرك")

D_out = st.sidebar.number_input("القطر الخارجي (m)", value=0.20, step=0.01)
d_in  = st.sidebar.number_input("القطر الداخلي (m)", value=0.08, step=0.01)
L     = st.sidebar.number_input("الطول (m)", value=0.50, step=0.05)
rho_p = st.sidebar.number_input("كثافة الوقود (kg/m³)", value=1700.0, step=10.0)
a     = st.sidebar.number_input("معامل معدل الاحتراق a", value=0.005, format="%.5f")
n     = st.sidebar.number_input("أس معدل الاحتراق n", value=0.35, step=0.01)
At    = st.sidebar.number_input("مساحة فتحة الخروج (m²)", value=0.002, format="%.5f")
Cf    = st.sidebar.number_input("معامل الدفع Cf", value=1.5, step=0.05)

st.sidebar.header("🌡️ ظروف التخزين والتقادم")
T_storage = st.sidebar.number_input("درجة حرارة التخزين (K)", value=323.0, step=1.0)
Ea        = st.sidebar.number_input("طاقة التنشيط Ea (J/mol)", value=80000.0, step=1000.0)
k_aging   = st.sidebar.number_input("ثابت معدل التقادم k (1/s)", value=1e-9, format="%.2e")

st.sidebar.header("⚠️ معيار الفشل")
criterion = st.sidebar.selectbox(
    "نوع معيار الفشل",
    ["زيادة الضغط بنسبة %", "زيادة معدل الاحتراق بنسبة %", "انخفاض إجمالي الدفع بنسبة %"]
)
threshold_pct = st.sidebar.number_input("نسبة التغير المسموحة (%)", value=15.0, step=1.0)

# ==================== دوال الحساب ====================
def simulate(aging_factor):
    """محاكاة الاحتراق وإرجاع (P_max, rb_avg, total_impulse)"""
    dt = 0.001
    r = d_in / 2
    r_out = D_out / 2
    web = r_out - r
    t = 0
    P_list, T_list, time_list = [], [], []

    while web > 0 and t < 200:
        Ab = 2 * np.pi * r * L
        # الضغط شبه الثابت
        Pc = (rho_p * Ab * a * aging_factor / At) ** (1 / (1 - n))
        rb = a * (Pc ** n) * aging_factor
        dr = rb * dt
        r += dr
        web -= dr
        thrust = Cf * Pc * At
        P_list.append(Pc)
        T_list.append(thrust)
        time_list.append(t)
        t += dt

    P_max = max(P_list)
    rb_avg = np.mean([a * (P ** n) * aging_factor for P in P_list])
    total_impulse = np.trapz(T_list, time_list)
    return P_max, rb_avg, total_impulse, time_list, P_list, T_list

# ==================== الحسابات ====================
# المرجع (بدون تقادم)
P0, rb0, I0, _, _, _ = simulate(1.0)

# معامل التسريع (Arrhenius)
AF = np.exp((Ea / R) * (1 / T_ref - 1 / T_storage))

# ==================== البحث عن العمر الافتراضي ====================
t_eq_max = 100 * 365 * 24 * 3600   # 100 سنة كحد أقصى
t_eq_arr = np.linspace(0, t_eq_max, 300)

life_found = False
life_equivalent = 0
P_curve = []

for te in t_eq_arr:
    af = 1 + k_aging * te
    P, rb, I, _, _, _ = simulate(af)
    P_curve.append(P)

    if criterion == "زيادة الضغط بنسبة %":
        fail = (P - P0) / P0 * 100 >= threshold_pct
    elif criterion == "زيادة معدل الاحتراق بنسبة %":
        fail = (rb - rb0) / rb0 * 100 >= threshold_pct
    else:
        fail = (I0 - I) / I0 * 100 >= threshold_pct

    if fail and not life_found:
        life_equivalent = te
        life_found = True
        break

life_real = life_equivalent / AF if life_found else 0

# ==================== عرض النتائج ====================
st.header("📊 النتائج")

col1, col2, col3 = st.columns(3)
col1.metric("معامل التسريع AF", f"{AF:.2f}")
col2.metric("الضغط الاسمي P0", f"{P0/1e6:.2f} MPa")
col3.metric("معدل الاحتراق الاسمي", f"{rb0*1000:.3f} mm/s")

if life_found:
    years_real = life_real / (365 * 24 * 3600)
    years_eq = life_equivalent / (365 * 24 * 3600)

    st.success(f"### ⏳ العمر الافتراضي عند {T_storage:.0f} K")

    c1, c2 = st.columns(2)
    c1.metric("بالسنوات الفعلية", f"{years_real:.2f} سنة")
    c2.metric("مكافئ عند 20°C", f"{years_eq:.2f} سنة")

    st.info(f"**معيار الفشل:** {criterion} ≥ {threshold_pct}%")
else:
    st.warning("⚠️ المحرك لم يصل لمعيار الفشل خلال 100 سنة مكافئة")

# ==================== الرسم البياني ====================
st.header("📈 تطور الضغط الأقصى مع الزمن")

fig, ax = plt.subplots(figsize=(10, 4))
x_years = t_eq_arr[:len(P_curve)] / (365 * 24 * 3600)
ax.plot(x_years, np.array(P_curve) / 1e6, label="الضغط الأقصى", color="blue")
ax.axhline(P0 * (1 + threshold_pct / 100) / 1e6, color="red",
           linestyle="--", label="حد الفشل")
if life_found:
    ax.axvline(life_equivalent / (365 * 24 * 3600), color="green",
               linestyle=":", label="العمر الافتراضي")
ax.set_xlabel("الزمن المكافئ عند 20°C (سنة)")
ax.set_ylabel("الضغط الأقصى (MPa)")
ax.legend()
ax.grid(True, alpha=0.3)
st.pyplot(fig)

# ==================== جدول مقارنة درجات الحرارة ====================
st.header("🌡️ مقارنة العمر عند درجات حرارة مختلفة")

temps = [293.15, 303.15, 313.15, 323.15, 333.15]
results = []

for T in temps:
    AF_i = np.exp((Ea / R) * (1 / T_ref - 1 / T))
    life_found_i = False
    for te in t_eq_arr:
        af = 1 + k_aging * te
        P, rb, I, _, _, _ = simulate(af)
        if criterion == "زيادة الضغط بنسبة %":
            fail = (P - P0) / P0 * 100 >= threshold_pct
        elif criterion == "زيادة معدل الاحتراق بنسبة %":
            fail = (rb - rb0) / rb0 * 100 >= threshold_pct
        else:
            fail = (I0 - I) / I0 * 100 >= threshold_pct
        if fail:
            life_found_i = True
            life_y = (te / AF_i) / (365 * 24 * 3600)
            break
    results.append({
        "درجة الحرارة (°C)": f"{T - 273.15:.0f}",
        "معامل التسريع": f"{AF_i:.2f}",
        "العمر (سنة)": f"{life_y:.2f}" if life_found_i else "> 100"
    })

st.table(results)

# ==================== تحذير ====================
st.warning(
    "⚠️ **تنبيه:** هذا النموذج تعليمي مبسط ولا يصلح للتصميم الفعلي أو "
    "قرارات السلامة. أي قرار حقيقي يحتاج معايرة ببيانات اختبار فعلية."
)