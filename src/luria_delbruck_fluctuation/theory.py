"""Theory — Mathematical predictions under each hypothesis (treated as established derivations)."""

from gaia.lang import claim, setting

from .motivation import (
    experimental_system,
    hypothesis_mutation,
    hypothesis_acquired_immunity,
)

# === Settings: mathematical framework ===

exponential_growth_model = setting(
    "Bacteria grow exponentially. Choosing the average division time divided by "
    "ln 2 as the time unit, the number of bacteria $N_t$ at time $t$ follows "
    "$dN_t/dt = N_t$, hence $N_t = N_0 e^t$, where $N_0$ is the initial number.",
    title="Exponential growth model",
)

mutation_rate_definition = setting(
    "The mutation rate $a$ is defined as the chance of mutation per bacterium "
    "per time unit (where time is measured in units of the average division time "
    "divided by ln 2). During a time element $dt$, the chance of mutation for "
    "each bacterium is $a \\, dt$.",
    title="Mutation rate definition",
)

clone_size_age_relation = setting(
    "Resistant bacteria are grouped into clones. The 'age' of a clone is the "
    "time since its parent mutation occurred; the 'size' is the number of bacteria "
    "in the clone at time of observation. Assuming resistant bacteria grow at the "
    "same rate as sensitive bacteria (equation $N_t = N_0 e^t$), clone size "
    "increases exponentially with age.",
    title="Clone size-age relation",
)

# === Theoretical predictions ===
# These are treated as leaf claims (established theoretical derivations)
# that feed into the abduction. The derivations themselves are mathematical —
# their correctness is not in question; what's in question is which hypothesis
# is correct.

immunity_variance_equals_mean = claim(
    "Under the acquired immunity hypothesis, each bacterium independently survives "
    "virus attack with a fixed small probability. The number of survivors follows "
    "a Poisson distribution, so the variance equals the mean: "
    "$\\text{var}(\\rho) = \\bar{\\rho}$. Derivation: binomial distribution with "
    "small success probability → Poisson approximation → variance = mean.",
    title="Acquired immunity: variance equals mean (Poisson)",
    background=[experimental_system, hypothesis_acquired_immunity],
)

mutation_high_variance = claim(
    "Under the mutation hypothesis, the variance of the number of resistant "
    "bacteria across replicate cultures is much greater than the mean. The likely "
    "variance is $\\text{var}_r = C a^2 N_t^2$ (equation 11), giving a ratio "
    "$\\sqrt{\\text{var}_r}/r = \\sqrt{C}/\\ln(N_t C a)$ (equation 12), which "
    "is >> 1. Derivation: superposition of partial distributions for clones of "
    "each age, each Poisson-distributed, with clone size growing exponentially "
    "— the 'slot machine' effect where rare early mutations produce jackpots.",
    title="Mutation hypothesis: high variance (jackpot distribution)",
    background=[exponential_growth_model, mutation_rate_definition,
                clone_size_age_relation, hypothesis_mutation],
)

p0_mutation_rate_relation = claim(
    "Under the mutation hypothesis, the fraction $p_0$ of cultures with zero "
    "resistant bacteria equals $p_0 = e^{-m}$ where $m = a(N_t - N_0)$ is the "
    "average number of mutations per culture (equations 4-5). Derivation: "
    "mutations are Poisson-distributed in time, so zero mutations has probability "
    "$e^{-m}$. This provides a method to estimate $a$ from the fraction of "
    "cultures with no resistant bacteria.",
    title="p0 method for estimating mutation rate",
    background=[exponential_growth_model, mutation_rate_definition, hypothesis_mutation],
)

mean_method_mutation_rate = claim(
    "Under the mutation hypothesis, the average number of resistant bacteria per "
    "culture $r$ relates to the mutation rate $a$ via the transcendental equation "
    "$r = a N_t \\ln(N_t C a)$ (equation 8), solvable numerically for $a$ given "
    "observed $r$, $N_t$, and $C$. Derivation: the average $\\rho = t a N_t$ "
    "(equation 6), corrected for finite samples by excluding mutations before "
    "$t_0$ (chosen so on average one mutation occurred before $t_0$ across $C$ "
    "cultures).",
    title="Mean method for estimating mutation rate",
    background=[exponential_growth_model, mutation_rate_definition,
                clone_size_age_relation, hypothesis_mutation],
)
