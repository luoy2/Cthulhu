import logging

import constants
import map
import skills
import sanity_roll


class Investigator(object):
    logger = logging.getLogger('Investigator log')

    def __init__(self, name, current_relic_cards, current_clue_cards, skill=None, card_limit=7, sanity=4,
                 current_action_points=4, sealing_gate_card_consumption=5, trade_cards_action_consumption=1,
                 defeat_shoggoth_action_consumption=3, sanity_state=constants.SANE_STATE,
                 current_location=map.Train_Station, action_limit=4, available_step=[1], able_to_take_bus=True,
                 bus_travel_skill=False):
        self.name = name
        self.current_relic_cards = current_relic_cards
        self.current_clue_cards = current_clue_cards
        self.skill = skill
        self.card_limit = card_limit
        self.sanity = sanity
        self.current_action_points = current_action_points
        self.sealing_gate_card_consumption = sealing_gate_card_consumption
        self.trade_card_action_consumption = trade_cards_action_consumption
        self.defeat_shoggoth_action_consumption = defeat_shoggoth_action_consumption
        self.sanity_state = sanity_state
        self.current_location = current_location
        self.action_limit = action_limit
        self.available_step = available_step
        self.able_to_take_bus = able_to_take_bus
        self.bus_travel_skill = bus_travel_skill

    def defeat_cultist(self):
        if self.current_action_points > 1 and self.current_location.get_cult() > 0:
            self.current_location.add_cult(-1)
            self.current_action_points = self.current_action_points - 1
        else:
            self.logger.info('Unable to defeat cultist!')

    def defeat_shoggoth(self, invoke_skill=False):
        if self.current_action_points > self.defeat_shoggoth_action_consumption and \
                        self.current_location.get_shog() > 0:
            self.current_location.add_shog(-1)
            self.current_action_points = self.current_action_points - self.defeat_shoggoth_action_consumption

        else:
            self.logger.info('Unable to defeat Shoggoth!')

    def move_to(self, destination):
        if self.current_location.get_location_by_step(destination) in self.available_step and \
                        self.current_action_points > 0:
            self.current_location = destination
            self.current_action_points = self.current_action_points - 1
        else:
            self.logger.info(f'Unable to move to move to {destination.name}')

    def check_sanity(self):
        if self.sanity <= 0 and self.sanity_state != constants.INSANE_STATE:
            self.become_insane()
        elif self.sanity > 0 and self.sanity_state != constants.SANE_STATE:
            self.become_same()

    def become_insane(self):
        self.sanity = 0
        self.sanity_state = constants.INSANE_STATE

    def become_same(self):
        self.sanity = 4
        self.sanity_state = constants.SANE_STATE

    def add_relic_card(self, card):
        self.current_relic_cards.append(card)

    def add_clue_card(self, card):
        self.current_clue_cards.append(card)

    def play_relic_card(self, card):
        if card in self.current_relic_cards:
            sanity_roll_effect = sanity_roll.roll_sanity_die()
            if sanity_roll.SANITY_DIE_EFFECT_DELUSIONAL == sanity_roll_effect:
                self.sanity = self.sanity - 1
                self.check_sanity()
            elif sanity_roll.SANITY_DIE_EFFECT_PSYCHOTIC == sanity_roll_effect:
                self.sanity = self.sanity - 2
            elif sanity_roll.SANITY_DIE_EFFECT_PARANOID ==  sanity_roll_effect:
                self.current_location.add_cult(2)


class Hunter(Investigator):
    def __init__(self):
        Investigator.__init__(self, 'HUNTER', [], [], skills.HunterSkill(self))

    def defeat_cultist(self):
        if self.current_action_points > 1 and self.current_location.get_cult() > 0:
            self.current_location.add_cult(-1)
            self.current_action_points = self.current_action_points - 1
            self.skill.upon_defeat_cultist(self.current_location)
        else:
            self.logger.info('Unable to defeat cultist!')


class Doctor(Investigator):
    def __init__(self):
        Investigator.__init__(self, 'DOCTOR', [], [], skills.DoctorSkill(self))


class Driver(Investigator):
    def __init__(self):
        Investigator.__init__(self, 'DRIVER', [], [], skills.DriverSkill(self))
        self.ignore_ithaqua_effect = True


class Magician(Investigator):
    def __init__(self):
        Investigator.__init__(self, 'MAGICIAN', [], [], )





















