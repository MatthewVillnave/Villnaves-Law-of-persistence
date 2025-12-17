"""
Villnave’s Law — Canonical Falsification Suite
=============================================

This script is explicitly designed to attempt to BREAK Villnave’s Law.

Observed collapses are confirmations of violated viability,
not failures of the law.

Law under test:
Ω = Λχ
M = (Ω − 1) − ΔS

No tuning. No fitting. No mercy.
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(7)

# ======================================================
# CORE LAW (LOCKED)
# ======================================================

def Omega_villnave(L, chi):
    return L * chi

def M_margin(Omega, dS):
    return (Omega - 1.0) - dS

# ======================================================
# COMPETITOR FORMS
# ======================================================

def Omega_additive(L, chi):
    return L + chi - 1.0

def Omega_min(L, chi):
    return np.minimum(L, chi)

def Omega_log(L, chi):
    return np.log(L + 1e-6) * chi

OMEGA_FUNCS = {
    "Villnave": Omega_villnave,
    "Additive": Omega_additive,
    "Min": Omega_min,
    "Log": Omega_log
}

# ======================================================
# SYSTEM SIMULATOR
# ======================================================

def run_system(T, L_t, chi_t, dS_t, omega_func=Omega_villnave, damage=False):
    Omega = np.zeros(T)
    M = np.zeros(T)
    alive = True
    collapse_time = None

    L_eff = L_t.copy()

    for t in range(T):
        Omega[t] = omega_func(L_eff[t], chi_t[t])
        M[t] = M_margin(Omega[t], dS_t[t])

        if Omega[t] < 1.0 and alive:
            alive = False
            collapse_time = t
            if damage:
                L_eff[t:] *= 0.7  # irreversible structural loss

    return {
        "Omega": Omega,
        "M": M,
        "alive": alive,
        "collapse_time": collapse_time
    }

# ======================================================
# REPORTING
# ======================================================

def report(label, res):
    status = "ALIVE" if res["alive"] else f"COLLAPSED @ t={res['collapse_time']}"
    print(f"{label:45s} : {status}")

def plot(title, res):
    plt.figure(figsize=(10,4))
    plt.plot(res["Omega"], label="Ω")
    plt.plot(res["M"], label="M")
    plt.axhline(1.0, linestyle="--", alpha=0.4)
    plt.axhline(0.0, linestyle=":", alpha=0.4)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()

# ======================================================
# TESTS
# ======================================================

T = 200

print("\n=== TEST 1: PARAMETER DEGENERACY ===")
dS = np.ones(T) * 0.05
A = run_system(T, np.ones(T)*5.0, np.ones(T)*0.24, dS)
B = run_system(T, np.ones(T)*1.2, np.ones(T)*1.0, dS)
report("High Λ / Low χ", A)
report("Low Λ / High χ", B)

print("\n=== TEST 2: SLOW ENTROPY POISONING ===")
dS = np.linspace(0.0, 0.4, T)
silent = run_system(T, np.ones(T)*1.3, np.ones(T), dS)
report("Silent Entropy Accumulation", silent)

print("\n=== TEST 3: MEASUREMENT NOISE ===")
noise = np.random.normal(0, 0.1, T)
true = run_system(T, np.ones(T)*1.4, np.ones(T)*0.9, np.ones(T)*0.1)
noisy = run_system(T, np.ones(T)*1.4+noise, np.ones(T)*0.9+noise, np.ones(T)*0.1)
report("True System", true)
report("Noisy Observer", noisy)

print("\n=== TEST 4: PARASITIC COUPLING ===")
drain = 0.005
A = run_system(T, np.ones(T)*1.6 - np.arange(T)*drain, np.ones(T)*0.9, np.zeros(T))
B = run_system(T, np.ones(T)*0.6 + np.arange(T)*drain, np.ones(T)*0.9, np.zeros(T))
report("Rescuer Node", A)
report("Parasitic Node", B)

print("\n=== TEST 5: ADVERSARIAL Ω GAMING ===")
L = np.ones(T)
chi = np.linspace(1.0, 0.4, T)
for t in range(0, T, 20):
    L[t:t+3] += 1.0
res_game = run_system(T, L, chi, np.ones(T)*0.05)
report("Adversarial Gaming", res_game)

print("\n=== TEST 6: REGIME SWITCH + HYSTERESIS ===")
chi = np.ones(T)
chi[80:120] *= 0.6
dS = np.ones(T)*0.08
dS[80:120] = 0.25
no_damage = run_system(T, np.ones(T)*1.4, chi, dS, damage=False)
with_damage = run_system(T, np.ones(T)*1.4, chi, dS, damage=True)
report("Regime Switch (No Damage)", no_damage)
report("Regime Switch (With Damage)", with_damage)

print("\n=== TEST 7: COMPETITOR LAW TOURNAMENT ===")
L = np.ones(T)*1.25
chi = np.ones(T)
dS = np.linspace(0.0, 0.3, T)
for name, fn in OMEGA_FUNCS.items():
    res = run_system(T, L, chi, dS, omega_func=fn)
    report(f"Competitor: {name}", res)

print("\n=== END OF FALSIFICATION SUITE ===")
