"""Experimental — Validation of the plating method reliability."""

from gaia.lang import claim, setting, support

from .motivation import experimental_system

# === Setting: experimental protocol ===

plating_protocol = setting(
    "Parallel platings are made from the same bacterial culture to test whether "
    "the plating method itself introduces variance. Multiple samples from a single "
    "culture are plated with excess virus on nutrient agar plates. Resistant "
    "colonies are counted after incubation. If the method is reliable, the only "
    "source of variation should be random sampling (Poisson), and variance should "
    "equal the mean.",
    title="Plating reliability test protocol",
)

# === Plating reliability results ===

plating_variance_equals_mean = claim(
    "In three plating reliability experiments (Table 1), parallel samples from the "
    "same culture were plated and resistant colonies counted:\n\n"
    "| Experiment | Mean | Variance | $\\chi^2$ | P |\n"
    "|-----------|------|----------|----------|---|\n"
    "| Exp. 10a  | 16.7 | 15       | 9        | 0.4 |\n"
    "| Exp. 11a  | 51.4 | 27       | 5.3      | 0.8 |\n"
    "| Exp. 3    | 3.3  | 3.8      | 12       | 0.2 |\n\n"
    "In all three cases, the variance and mean agree as expected for Poisson "
    "sampling. There is no evidence that the plating method introduces fluctuations "
    "beyond sampling error.",
    title="Plating reliability: variance equals mean",
    background=[plating_protocol],
    source_table="artifacts/paper.pdf, Table 1",
)

plating_method_reliable = claim(
    "The plating method is reliable: it does not introduce any unrecognized "
    "variables that cause the number of resistant colonies to vary from plate "
    "to plate or from sample to sample, beyond random sampling. Any excess "
    "variance observed in experiments comparing different cultures must therefore "
    "originate from the cultures themselves, not from the measurement process.",
    title="Plating method validated as reliable",
    background=[plating_protocol],
)

strat_plating_reliable = support(
    [plating_variance_equals_mean],
    plating_method_reliable,
    reason=(
        "@plating_variance_equals_mean shows that in all three experiments, "
        "the variance of colony counts from repeated platings of the same culture "
        "matches the mean (chi-squared tests give $P = 0.2$ to $0.8$), consistent "
        "with Poisson sampling. Since only sampling variance is observed, the "
        "plating method introduces no additional fluctuations, validating it as a "
        "reliable measurement tool."
    ),
    prior=0.9,
)
