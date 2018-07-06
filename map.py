import queue
import logging
from enum import Enum

from constants import Region
import awakening_rituals


class Location(object):
    _cultist_num = 0
    _shoggoth_num = 0
    connected_locations = []

    def __init__(self, name, region, gate=0, train_station=0):
        self.name = name
        self.region = region
        self.gate = gate
        self.train_station = train_station
        self.open = 1
        self.logger = logging.getLogger('Location log')

    def __repr__(self):
        return self.name

    def get_location_by_step(self, step=1):
        available_locations = []
        if step == 1:
            return self.connected_locations
        else:
            for i in self.connected_locations:
                available_locations += i.get_location_by_step(step-1)
            return list(set(available_locations))

    def calculate_distance(self, destination):
        return self.get_result_dict_to_destination(destination)['steps']

    def get_path_to_open_gate(self):
        return self.get_result_dict_to_destination(open_gate=True)['path']

    def get_result_dict_to_destination(self, destination=None, open_gate=False):
        frontier = queue.Queue()
        frontier.put(self)
        came_from = {self: None}

        while not frontier.empty():
            current = frontier.get()
            if destination and current.name == destination.name:
                break
            elif open_gate and current.open*current.gate:
                break
            else:
                self.logger.info('Incorrect setting. Could not find path.')

            for next_location in current.connected_locations:
                if next_location not in came_from:
                    frontier.put(next_location)
                    came_from[next_location] = current

        ordered_loc = [current]
        while came_from[current]:
            before = came_from[current]
            ordered_loc.append(before)
            current = before

        result_dict = {'steps':len(ordered_loc)-1,
                       'path':[i for i in reversed(ordered_loc)]}
        return result_dict

    def check_cult_status(self):
        if self._cultist_num > 3:
            awakening_rituals.start()

    def add_cultist(self, num):
        self._cultist_num += num
        self.check_cult_status()

    def add_shoggoth(self, num):
        self._shoggoth_num += num

    def get_cultist(self):
        return self._cultist_num

    def get_shoggoth(self):
        return self._shoggoth_num

    def clear_cultist(self):
        self._cultist_num = 0

    def seal_gate(self):
        if self.gate:
            self.open = 0


class Locations(Enum):
    # Green region
    Train_Station = Location(name='Train Station', region=Region.GREEN, train_station=1)
    University = Location(name='University', region=Region.GREEN)
    Park = Location(name='Park', region=Region.GREEN, gate=1)
    Police_Station = Location(name='Police Station', region=Region.GREEN)
    Secret_Lodge = Location(name='Secret Lodge', region=Region.GREEN)
    Diner = Location(name='Diner', region=Region.GREEN, train_station=1)

    # Yellow region
    Cafe = Location(name='Cafe', region=Region.YELLOW)
    Old_Mill = Location(name='Old Mill', region=Region.YELLOW, gate=1)
    Church = Location(name='Church', region=Region.YELLOW)
    Farmstead = Location(name='Farmstead', region=Region.YELLOW)
    Historic_Inn = Location(name='Historic Inn', region=Region.YELLOW, train_station=1)
    Swamp = Location(name='Swamp', region=Region.YELLOW)

    # Blue region
    Junkyard = Location(name='Junkyard', region=Region.BLUE)
    Pawn_Shop = Location(name='Pawn Shop', region=Region.BLUE)
    Hospital = Location(name='Hospital', region=Region.BLUE, gate=1)
    Factory = Location(name='Factory', region=Region.BLUE, train_station=1)
    Broadwalk = Location(name='Broadwalk', region=Region.BLUE)
    Docks = Location(name='Docks', region=Region.BLUE)

    # Red region
    Woods = Location(name='Woods', region=Region.RED)
    Market = Location(name='Market', region=Region.RED, train_station=1)
    Wharf = Location(name='Wharf', region=Region.RED)
    Theater = Location(name='Theater', region=Region.RED)
    Graveyard = Location(name='Graveyard', region=Region.RED, gate=1)
    Great_Hall = Location(name='Great Hall', region=Region.RED)


class Map(object):
    def __init__(self):
        self.locations = Locations
        self.logger = logging.getLogger('Map logger')

    def set_up_location_connections(self):
        self.locations.Train_Station.connected_locations = [self.locations.University, self.locations.Cafe]
        self.locations.University.connected_locations = \
            [self.locations.Park, self.locations.Train_Station, self.locations.Police_Station]
        self.locations.Park.connected_locations = \
            [self.locations.University, self.locations.Police_Station, self.locations.Secret_Lodge]
        self.locations.Police_Station.connected_locations = \
            [self.locations.University, self.locations.Park, self.locations.Secret_Lodge]
        self.locations.Secret_Lodge.connected_locations = \
            [self.locations.Park, self.locations.Police_Station, self.locations.Diner]
        self.locations.Diner.connected_locations = [self.locations.Secret_Lodge, self.locations.Junkyard]

        self.locations.Junkyard.connected_locations = [self.locations.Diner, self.locations.Pawn_Shop]
        self.locations.Pawn_Shop.connected_locations = \
            [self.locations.Junkyard, self.locations.Hospital, self.locations.Factory]
        self.locations.Hospital.connected_locations = [self.locations.Pawn_Shop, self.locations.Factory]
        self.locations.Factory.connected_locations = \
            [self.locations.Hospital, self.locations.Pawn_Shop, self.locations.Broadwalk, self.locations.Theater]
        self.locations.Broadwalk.connected_locations = [self.locations.Factory, self.locations.Docks]
        self.locations.Docks.connected_locations = [self.locations.Broadwalk, self.locations.Woods]

        self.locations.Woods.connected_locations = \
            [self.locations.Docks, self.locations.Market, self.locations.Great_Hall]
        self.locations.Market.connected_locations = \
            [self.locations.Woods, self.locations.Great_Hall, self.locations.Wharf]
        self.locations.Wharf.connected_locations = [self.locations.Market, self.locations.Graveyard]
        self.locations.Graveyard.connected_locations = [self.locations.Wharf]
        self.locations.Theater.connected_locations = [self.locations.Market]
        self.locations.Great_Hall.connected_locations = \
            [self.locations.Woods, self.locations.Market, self.locations.Swamp]

        self.locations.Swamp.connected_locations = [self.locations.Great_Hall, self.locations.Farmstead]
        self.locations.Farmstead.connected_locations = \
            [self.locations.Historic_Inn, self.locations.Church, self.locations.Swamp]
        self.locations.Historic_Inn.connected_locations = [self.locations.Church, self.locations.Farmstead]
        self.locations.Church.connected_locations = \
            [self.locations.Old_Mill, self.locations.Historic_Inn, self.locations.Farmstead]
        self.locations.Cafe.connected_locations = [self.locations.Church, self.locations.Train_Station]
        self.locations.Old_Mill.connected_locations = [self.locations.Church]

    def get_location_by_name(self, location_name):
        result_list = [loc for loc in self.locations if loc.name == location_name]
        if len(result_list) != 1:
            self.logger.info('Unable to get location.')
        else:
            return result_list[0].value



