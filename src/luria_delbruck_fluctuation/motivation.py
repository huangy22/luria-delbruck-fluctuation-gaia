"""Introduction and Motivation — Competing hypotheses for the origin of virus-resistant bacteria."""

from gaia.lang import claim, setting, question, contradiction

# === Settings: experimental context ===

experimental_system = setting(
    "A pure bacterial culture of *Escherichia coli* B is attacked by bacteriophage "
    "(bacterial virus) alpha. Sensitive cells are lysed (destroyed) within hours. "
    "After further incubation the culture becomes turbid again due to growth of a "
    "resistant variant that does not adsorb the virus. This variant retains resistance "
    "through many generations in the absence of virus.",
    title="Experimental system: bacterial virus resistance",
)

resistance_properties = setting(
    "The resistant variant's resistance is generally rather specific to the inciting "
    "virus strain. The variant may differ from the original strain in morphological or "
    "metabolic characteristics, or in serological type or colony type, but most often "
    "no correlated changes are apparent besides virus resistance.",
    title="Properties of resistant variants",
)

# === The central research question ===

central_question = question(
    "What is the origin of virus-resistant bacterial variants: do they arise by "
    "spontaneous heritable mutation prior to virus exposure, or by virus-induced "
    "acquired hereditary immunity?",
    title="Central question",
)

# === The two competing hypotheses ===

hypothesis_mutation = claim(
    "Hypothesis of mutation: There is a finite probability per time unit for any "
    "bacterium to mutate from 'sensitive' to 'resistant.' Every offspring of such a "
    "mutant will be resistant, unless reverse mutation occurs. The term 'resistant' "
    "means the bacterium will not be killed if exposed to virus, and the possibility "
    "of interaction with virus is left open. Mutations occur spontaneously, prior to "
    "and independently of virus exposure.",
    title="Hypothesis 1: Spontaneous mutation",
    background=[experimental_system],
)

hypothesis_acquired_immunity = claim(
    "Hypothesis of acquired hereditary immunity: There is a small finite probability "
    "for any bacterium to survive an attack by the virus. Survival confers immunity "
    "not only to the individual but also to its offspring. The probability of survival "
    "in the first instance does not run in clones; if we find that a bacterium survives "
    "an attack, we cannot from this information alone infer that close relatives are "
    "likely to survive the attack.",
    title="Hypothesis 2: Acquired hereditary immunity",
    background=[experimental_system],
)

# === Key distinguishing predictions (qualitative) ===

mutation_predicts_clonal_grouping = claim(
    "On the mutation hypothesis, resistant bacteria in a culture arise from mutations "
    "that may occur at any time prior to virus exposure. The culture therefore will "
    "contain 'clones of resistant bacteria' of various sizes: early mutations produce "
    "large clones, late mutations produce small clones. Consequently, the number of "
    "resistant bacteria in replicate cultures will show high variance — clonal grouping "
    "rather than random sampling.",
    title="Mutation hypothesis predicts clonal variance",
    background=[experimental_system],
)

immunity_predicts_poisson = claim(
    "On the hypothesis of acquired immunity, resistant bacteria represent a random "
    "sample of the population that survived virus attack. Each bacterium has an "
    "independent, equal probability of surviving. The number of resistant bacteria "
    "in replicate cultures should therefore follow a Poisson distribution, with "
    "variance equal to the mean.",
    title="Immunity hypothesis predicts Poisson distribution",
    background=[experimental_system],
)

# === Operator: the two hypotheses are mutually exclusive and exhaustive ===

hypotheses_exclusive = contradiction(
    hypothesis_mutation,
    hypothesis_acquired_immunity,
    reason=(
        "The mutation hypothesis and acquired immunity hypothesis are incompatible: "
        "if resistance arises by spontaneous mutation prior to virus contact, it "
        "cannot simultaneously arise by virus-induced hereditary change, and vice "
        "versa. Both cannot be true for the same system."
    ),
    prior=0.95,
)
