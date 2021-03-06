import random

SANITY_DIE_EFFECT_BLANK='BLANK'
SANITY_DIE_EFFECT_DELUSIONAL='DELUSIONAL'
SANITY_DIE_EFFECT_PSYCHOTIC='PSYCHOTIC'
SANITY_DIE_EFFECT_PARANOID='PARANOID'


def roll_sanity_die():
    sanity_die_effects_dict = {
        1 : SANITY_DIE_EFFECT_BLANK,
        2 : SANITY_DIE_EFFECT_BLANK,
        3 : SANITY_DIE_EFFECT_DELUSIONAL,
        4 : SANITY_DIE_EFFECT_DELUSIONAL,
        5 : SANITY_DIE_EFFECT_PARANOID,
        6 : SANITY_DIE_EFFECT_PSYCHOTIC
    }

    return sanity_die_effects_dict[random.randint(1, 6)]

