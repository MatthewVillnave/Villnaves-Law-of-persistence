# Villnave’s Law of Persistence

Villnave’s Law is a minimal, falsifiable viability law describing the conditions under which structured systems persist or collapse under destabilizing pressure.

The law treats **persistence as a primitive**, not as an outcome of optimization, intelligence, or control.

It does not prescribe actions.  
It defines boundaries.

---

## Core Law

Villnave’s Law defines a persistence number:

\[
\Omega = \Lambda \chi
\]

where:

- **χ (chi)** is coherence: internal alignment, integrity, or consistency of the system  
- **Λ (Lambda)** is reinforcement capacity: structural support, redundancy, feedback, or coupling that sustains coherence  

The persistence condition is strict:

- **Ω > 1** → persistence is possible  
- **Ω < 1** → collapse is inevitable  

This is a viability boundary, not a performance metric.

---

## Existence (Persistence) Margin

To diagnose proximity to collapse, Villnave’s Law introduces the persistence margin:

\[
M = (\Omega - 1) - \Delta S
\]

where:

- **ΔS** is effective destabilizing pressure acting on the system

Interpretation:

- **M > 0** → surplus persistence capacity  
- **M < 0** → destabilization exceeds capacity; collapse is approaching  

The margin does not prevent collapse.  
It reports when persistence has become untenable.

---

## On ΔS (Destabilizing Pressure)

In Villnave’s Law, **ΔS denotes effective destabilizing pressure**, not literal thermodynamic entropy.

ΔS represents the total rate at which coherence χ is degraded by disordering forces acting on the system. These may include, depending on domain:

- stochastic noise  
- structural stress  
- resource depletion  
- semantic drift  
- fatigue or wear  
- adversarial interference  
- environmental volatility  

While thermodynamic entropy may contribute to ΔS in physical systems, **ΔS is not restricted to classical entropy measures** and should not be interpreted as a direct substitute for Boltzmann or Shannon entropy.

Villnave’s Law operates at the level of *viability dynamics*, not microphysical accounting. ΔS is therefore defined operationally: it is whatever pressure measurably reduces coherence χ over time.

This distinction is intentional and necessary for the law to apply across biological, computational, cognitive, and social systems.

---

## What This Law Is (and Is Not)

Villnave’s Law **is**:

- a viability boundary condition  
- a diagnostic tool for persistence and collapse  
- falsifiable and adversarially testable  
- domain-agnostic  

Villnave’s Law **is not**:

- a control policy  
- an optimization algorithm  
- a learning system  
- a guarantee of robustness or recovery  

The law does not “save” systems.  
It states when saving them is even possible.

---

## Falsification Philosophy

Villnave’s Law is designed to fail honestly.

Observed collapses in testing are **confirmations of violated viability**, not failures of the law. A persistence law that survived arbitrary mismeasurement, hidden coupling, or adversarial stress would be over-optimistic and therefore untrustworthy.

Failure under realistic stressors is expected and informative.

---

## Canonical Falsification Suite

This repository includes a canonical falsification suite that deliberately attempts to break the law under:

- parameter degeneracy  
- silent entropy accumulation  
- measurement noise  
- parasitic coupling  
- adversarial “gaming” of Ω  
- regime switching and hysteresis  
- competitor functional forms  

The base law is locked and untuned throughout.

See: `falsification_suite.py`

---

## Why Multiplicative Ω?

The multiplicative form Ω = Λχ is not arbitrary. It enforces key structural properties required of a viability scalar:

- **Zero-annihilation**: if coherence vanishes (χ → 0), persistence vanishes regardless of Λ  
- **Non-substitutability**: structure cannot fully compensate for incoherence, and vice versa  
- **Scale invariance**: equivalent persistence across aggregation levels yields equivalent Ω  
- **Predictable degradation**: proportional decay yields stable, interpretable collapse timing  

Alternative forms (additive, minimum, logarithmic) fail one or more of these properties under adversarial testing.

Formal justification and comparative tests are provided in the appendices of the paper.

---

## Status of This Release

This repository corresponds to **Release 1** of Villnave’s Law:

Included:
- the core law  
- the persistence margin  
- adversarial falsification tests  

Not included:
- control strategies  
- intervention policies  
- cryptobiosis or time-refusal mechanisms  
- application-specific implementations  

Those belong to subsequent layers built *on top of* the law, not inside it.

---

## Next: Engineered Persistence

Villnave’s Law diagnoses when collapse is inevitable.

Future work introduces **minimal control primitives**—intervention, cryptobiosis, and time refusal—that operate on top of the viability boundary, turning diagnosis into metered, costly persistence rather than guaranteed survival.

Control layers are intentionally excluded from this release.

---

## License and Use

Villnave’s Law is released for open examination, critique, and replication.

If you believe the law fails, the correct response is not dismissal—but falsification.  
If you believe it holds, the next step is not praise—but construction.

Either way, the boundary stands.

