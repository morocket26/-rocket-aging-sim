# -*- coding: utf-8 -*-
"""تحليل بيانات التقادم المعجل واستخراج Ea و A"""
import numpy as np
import pandas as pd

R = 8.314


def fit_arrhenius(df, property_name):
    """استخراج Ea و A من بيانات خاصية معينة"""
    results = []

    for T in sorted(df['temperature_C'].unique()):
        sub = df[df['temperature_C'] == T].dropna(subset=[property_name])
        if len(sub) < 2:
            continue
        t = sub['time_days'].values
        y = sub[property_name].values

        # نموذج خطي: y = y0 + k*t
        k, y0 = np.polyfit(t, y, 1)
        results.append({'T_C': T, 'T_K': T + 273.15, 'k': k})

    results_df = pd.DataFrame(results)

    if len(results_df) < 2:
        return None, None, results_df

    # Arrhenius: ln(k) = ln(A) - Ea/(R*T)
    inv_T = 1 / results_df['T_K'].values
    ln_k = np.log(np.abs(results_df['k'].values))

    slope, intercept = np.polyfit(inv_T, ln_k, 1)
    Ea = -slope * R
    A = np.exp(intercept)

    return Ea, A, results_df


if __name__ == "__main__":
    df = pd.read_csv('data.csv')

    print("=" * 60)
    print("تحليل بيانات التقادم المعجل")
    print("=" * 60)

    for prop in ['young_modulus', 'yield_stress', 'shore_A', 'max_thrust']:
        print(f"\n📊 الخاصية: {prop}")
        print("-" * 40)
        Ea, A, res = fit_arrhenius(df, prop)
        if Ea:
            print(f"  Ea = {Ea/1000:.2f} kJ/mol")
            print(f"  A  = {A:.4e}")
            print(res.to_string(index=False))
        else:
            print("  بيانات غير كافية")
