import sanity_roll
from constants import SaneState


class Skill(object):
    def __init__(self, investigator):
        self.investigator = investigator


class HunterSkill(Skill):
    def __init__(self, investigator):
        Skill.__init__(self, investigator)

    def upon_entry(self, current_location):
        if SaneState.SANE == self.investigator.sanity_state and 0 == current_location.get_cultist():
            sanity_roll_effect = sanity_roll.roll_sanity_die()
            if sanity_roll_effect == sanity_roll.SANITY_DIE_EFFECT_DELUSIONAL or \
                    sanity_roll_effect == sanity_roll.SANITY_DIE_EFFECT_PSYCHOTIC:
                current_location.add_cultist(1)

    @staticmethod
    def upon_defeat_cultist(current_location):
        current_location.clear_cultists()


class DoctorSkill(Skill):
    def __init__(self, investigator):
        Skill.__init__(self, investigator)


class DriverSkill(Skill):
    def __init__(self, investigator):
        Skill.__init__(self, investigator)


class MagicianSkill(Skill):
    def __init__(self, investigator):
        Skill.__init__(self, investigator)


