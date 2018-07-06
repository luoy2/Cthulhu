import random
from enum import Enum

from constants import Region


class Card(object):
    def __init__(self, name):
        self.name = name


class Deck(object):
    def __init__(self, name, current_cards):
        self.name = name
        self.current_cards = current_cards

    def shuffle(self):
        random.shuffle(self.current_cards)

    def pop(self):
        return self.current_cards.pop(0)

    def add(self, card):
        self.current_cards.append(card)


class SummoningCard(Card):
    def __init__(self, name, region, shoggoth_icon=0):
        Card.__init__(self, name)
        self.region = region
        self.shoggoth_icon = shoggoth_icon


class SummoningCards(Enum):
    # Green cards
    Train_Station = SummoningCard(name='Train Station', region=Region.GREEN)
    University = SummoningCard(name='University', region=Region.GREEN, shoggoth_icon=1)
    Park = SummoningCard(name='Park', region=Region.GREEN)
    Police_Station = SummoningCard(name='Police Station', region=Region.GREEN)
    Secret_Lodge = SummoningCard(name='Secret Lodge', region=Region.GREEN, shoggoth_icon=1)
    Diner = SummoningCard(name='Diner', region=Region.GREEN)

    # Yellow cards
    Cafe = SummoningCard(name='Cafe', region=Region.YELLOW)
    Old_Mill = SummoningCard(name='Old Mill', region=Region.YELLOW)
    Church = SummoningCard(name='Church', region=Region.YELLOW)
    Farmstead = SummoningCard(name='Farmstead', region=Region.YELLOW)
    Historic_Inn = SummoningCard(name='Historic Inn', region=Region.YELLOW, shoggoth_icon=1)
    Swamp = SummoningCard(name='Swamp', region=Region.YELLOW, shoggoth_icon=1)

    # Blue cards
    Junkyard = SummoningCard(name='Junkyard', region=Region.BLUE)
    Pawn_Shop = SummoningCard(name='Pawn Shop', region=Region.BLUE, shoggoth_icon=1)
    Hospital = SummoningCard(name='Hospital', region=Region.BLUE)
    Factory = SummoningCard(name='Factory', region=Region.BLUE)
    Broadwalk = SummoningCard(name='Broadwalk', region=Region.BLUE)
    Docks = SummoningCard(name='Docks', region=Region.BLUE, shoggoth_icon=1)

    # Red cards
    Woods = SummoningCard(name='Woods', region=Region.RED, shoggoth_icon=1)
    Market = SummoningCard(name='Market', region=Region.RED)
    Wharf = SummoningCard(name='Wharf', region=Region.RED)
    Theater = SummoningCard(name='Theater', region=Region.RED)
    Graveyard = SummoningCard(name='Graveyard', region=Region.RED)
    Great_Hall = SummoningCard(name='Great Hall', region=Region.RED, shoggoth_icon=1)


class SummoningCardDeck(Deck):
    def __init__(self, discard_deck):
        current_cards = list(SummoningCards)
        random.shuffle(current_cards)
        Deck.__init__(self, 'summoning_card_deck', current_cards)
        self.discard_deck = discard_deck

    def pop(self):
        card = self.current_cards.pop(0)
        self.discard_deck.add(card)
        return card


class SummoningCardDiscardDeck(Deck):
    def __init__(self):
        Deck.__init__(self, 'summoning_card_discard_deck', [])
