# shogan 需要找到最短的路径移动到下一个gate

class Gate(object):
    seal = False





class city(object):

    def __init__(self, name, region, cult_num=0, shogan_num=0, connected_city=[]):
        self.name = name
        self.region = region
        self.cult_num = cult_num
        self.shogan_num = shogan_num
        self.connected_city = connected_city


    def distance_to_gate(self):
        if 'GATE' in self.connected_city:
            return 1
        else:
            return min([i.distance_to_gate for i in self.connected_city])