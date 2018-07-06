# shogan 需要找到最短的路径移动到下一个gate
import constants
import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


class Gate(object):
    def __init__(self, region, seal):
        self.region = region
        self.seal = seal


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

    def __repr__(self):
        return self.name


    def get_location_by_step(self, step=1):
        avaliable_location = []
        if step == 1:
            return self.connected_locations
        else:
            for i in self.connected_locations:
                avaliable_location += i.get_location_by_step(step-1)
            return list(set(avaliable_location))


    def _calculate_distance(self, location):
        pass


    def get_path_to_open_gate(self):
        frontier = Queue()
        frontier.put(self)
        came_from = {}
        came_from[self] = None

        while not frontier.empty():
            current = frontier.get()
            # print(current)

            if current.open*current.gate:
                # print(current)
                break

            for next in current.connected_locations:
                # print(f'visiting connected location {next}')
                if next not in came_from:
                    frontier.put(next)
                    came_from[next] = current

        ordered_loc = []
        ordered_loc.append(current)
        while came_from[current]:
            before = came_from[current]
            ordered_loc.append(before)
            current = before

        result_dict = {'steps':len(ordered_loc)-1,
                       'path':[i for i in reversed(ordered_loc)]}
        return result_dict



    def add_cult(self, num):
        self._cultist_num += num


    def add_shog(self, num):
        self._shoggoth_num += num


    def get_cult(self):
        return self._cultist_num


    def get_shog(self):
        return self._shoggoth_num


    def seal_gate(self):
        if self.gate:
            self.open = 0


# class MapGraph(object):
#     def __init__(self):
#         self.edges = {}
#
#     def neighbors(self, location):
#         return self.edges[location]





# green region
Train_Station = Location(name='Train Station', region=constants.GREEN, train_station=1)
University = Location(name='University', region=constants.GREEN)
Park = Location(name='Park',region=constants.GREEN, gate=1)
Police_Station = Location(name='Police Station', region=constants.GREEN)
Secret_Lodge = Location(name='Secret Lodge', region=constants.GREEN)
Diner = Location(name='Diner', region=constants.GREEN, train_station=1)

#yellow region
Cafe = Location(name='Cafe', region=constants.YELLOW)
Old_Mill = Location(name='Old Mill', region=constants.YELLOW, gate=1)
Church = Location(name='Church', region=constants.YELLOW)
Farmstead = Location(name='Farmstead', region=constants.YELLOW)
Historic_Inn = Location(name='Historic Inn', region=constants.YELLOW, train_station=1)
Swamp = Location(name='Swamp', region=constants.YELLOW)


#blue region
Junkyard = Location(name='Junkyard', region=constants.BLUE)
Pawn_Shop = Location(name='Pawn Shop', region=constants.BLUE)
Hospital = Location(name='Hospital', region=constants.BLUE, gate=1)
Factory = Location(name='Factory', region=constants.BLUE, train_station=1)
Broadwalk = Location(name='Broadwalk', region=constants.BLUE)
Docks = Location(name='Docks', region=constants.BLUE)


#red region
Woods = Location(name='Woods', region=constants.RED)
Market = Location(name='Market', region=constants.RED, train_station=1)
Wharf = Location(name='Wharf', region=constants.RED)
Theater = Location(name='Theater', region=constants.RED)
Graveyard = Location(name='Graveyard', region=constants.RED, gate=1)
Great_Hall = Location(name='Great Hall', region=constants.RED)


# Main_Map = MapGraph()
# Main_Map.edges = {
#     Train_Station: [University, Park],
#     University: [Park, Train_Station, Police_Station],
#     Park: [University, Police_Station, Secret_Lodge],
#     Police_Station: [University, Park, Secret_Lodge],
#     Secret_Lodge: [Park, Police_Station, Diner],
#     Diner: [Secret_Lodge, Junkyard],
#     Junkyard: [Diner, Pawn_Shop],
#     Pawn_Shop: [Junkyard, Hospital, Factory],
#     Hospital: [Pawn_Shop, Factory],
#     Factory: [Hospital, Pawn_Shop, Broadwalk],
#     Broadwalk: [Factory, Docks],
#     Docks: [Broadwalk, Woods],
#     Woods: [Docks, Market, Great_Hall],
#     Market: [Woods, Great_Hall, Wharf, Theater],
#     Wharf: [Market, Graveyard],
#     Graveyard: [Wharf],
#     Theater: [Market],
#     Great_Hall: [Woods, Market, Swamp],
#     Swamp: [Great_Hall, Farmstead],
#     Farmstead: [Historic_Inn, Church, Swamp],
#     Historic_Inn: [Church, Farmstead],
#     Church: [Old_Mill, Historic_Inn, Farmstead, Cafe],
#     Cafe: [Church, Train_Station],
#     Old_Mill: [Church]
# }


Train_Station.connected_locations = [University, Cafe]
University.connected_locations = [Park, Train_Station, Police_Station]
Park.connected_locations = [University, Police_Station, Secret_Lodge]
Police_Station.connected_locations = [University, Park, Secret_Lodge]
Secret_Lodge.connected_locations = [Park, Police_Station, Diner]
Diner.connected_location = [Secret_Lodge, Junkyard]

Junkyard.connected_location = [Diner, Pawn_Shop]
Pawn_Shop.connected_location = [Junkyard, Hospital, Factory]
Hospital.connected_location = [Pawn_Shop, Factory]
Factory.connected_location = [Hospital, Pawn_Shop, Broadwalk, Theater]
Broadwalk.connected_location = [Factory, Docks]
Docks.connected_locations = [Broadwalk, Woods]

Woods.connected_location = [Docks, Market, Great_Hall]
Market.connected_location = [Woods, Great_Hall, Wharf]
Wharf.connected_location = [Market, Graveyard]
Graveyard.connected_location = [Wharf]
Theater.connected_location = [Market]
Great_Hall.connected_location = [Woods, Market, Swamp]

Swamp.connected_locations = [Great_Hall, Farmstead]
Farmstead.connected_locations = [Historic_Inn, Church, Swamp]
Historic_Inn.connected_locations = [Church, Farmstead]
Church.connected_locations = [Old_Mill, Historic_Inn, Farmstead]
Cafe.connected_locations = [Church, Train_Station]
Old_Mill.connected_locations = [Church]
