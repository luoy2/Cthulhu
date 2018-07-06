import logging

import old_ones
from map import Map
from card import SummoningCardDeck, SummoningCardDiscardDeck


class Game(object):
    def __init__(self, number_of_players):
        self.logger = logging.getLogger('Game log')
        self.logger.info('Game started!')
        self.number_of_players = number_of_players
        self.map = Map()
        self.old_ones = old_ones.get_initial_old_ones()
        self.summoning_discard_deck = SummoningCardDiscardDeck()
        self.summoning_deck = SummoningCardDeck(self.summoning_discard_deck)
        self.set_up_cultist()
        self.set_up_shoggoth()

    def summon_cultist(self, location_name, num):
        self.map.get_location_by_name(location_name).add_cultist(num)

    def summon_shoggoth(self, location_name, num):
        self.map.get_location_by_name(location_name).add_shoggoth(num)

    def set_up_cultist(self):
        for _ in [1, 2]:
            for num in [3, 2, 1]:
                location_name = self.summoning_deck.pop().name
                self.summon_cultist(location_name, num)

    def set_up_shoggoth(self):
        location_name = self.summoning_deck.pop().name
        self.summon_shoggoth(location_name, 1)

    # TODO: Continue!
