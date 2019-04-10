# Nick Mills
# Created: 2019-03-22
# Updated: 2019-04-10

from random import randint
from Utils import Utils

class _Room():
    def __init__(self, name="Unnamed Room",\
        description="No description given",dependencies=[],\
        enemies=[],adj={}):
        """
        """
        self.__name = name
        self.__description = description
        self.__dependencies = dependencies
        self.__enemies = enemies
        # Dict of adjacent rooms
        self.__adj = {}
        for k,v in adj.items():
            if v != "":
                self.__adj[k] = v

    def description(self):
        return self.__description

    def rooms(self) -> dict:
        """
        """
        return self.__adj

    def get_room_in_dir(self, dir : str):
        """
        """
        room = self.this
        valid_dirs = {'n':self.north,'s':self.south,\
            'e':self.east,'w':self.west,'ne':self.north_east,\
                'nw':self.north_west,'se':self.south_east,\
                'sw':self.south_west}
        if dir in valid_dirs.keys():
            room = valid_dirs[dir]
        return room()

    def enemies(self):
        return self.__enemies
    
    def this(self):
        return self

    def north(self):
        if 'n' in self.__adj.keys():
            n = self.__adj['n']
        else:
            n = None
        return n

    def north_east(self):
        if 'ne' in self.__adj.keys():
            ne = self.__adj['ne']
        else:
            ne = None
        return ne

    def north_west(self):
        if 'nw' in self.__adj.keys():
            nw = self.__adj['nw']
        else:
            nw = None
        return nw

    def south(self):
        if 's' in self.__adj.keys():
            s = self.__adj['s']
        else:
            s = None
        return s

    def south_east(self):
        if 'se' in self.__adj.keys():
            se = self.__adj['se']
        else:
            se = None
        return se

    def south_west(self):
        if 'sw' in self.__adj.keys():
            sw = self.__adj['sw']
        else:
            sw = None
        return sw

    def east(self):
        if 'e' in self.__adj.keys():
            e = self.__adj['e']
        else:
            e = None
        return e

    def west(self):
        if 'w' in self.__adj.keys():
            w = self.__adj['w']
        else:
            w = None
        return w

    def __repr__(self):
        _str = "{}\n{}\n{}\n".format(self.__name,'-'*(len(self.__name) + 2),\
            self.__description)

        count = 0
        _str += "\nAdjacent Rooms:\n"
        for k,v in self.__adj.items():
            if count % 2 != 0:
                _str += "{}: {}\n".format(k,v)
            else:
                _str += "{}: {}\t".format(k,v)
            count += 1
        print()
        return _str

    def __str__(self):
        return "{}\n{}\n{}\n".format(self.__name,'-'*(len(self.__name) + 2),\
            self.__description)

class Rooms():
    def __init__(self):
        self.__values = []
        self.__count = 0

    @staticmethod
    def create_from_filedata(rooms) -> None:
        """
        """
        data = Utils.get_data()
        index = 0
        while data[index] is not None:
            index += 1
        index += 1
        while data[index] is not None:
            index += 1
        room_data_start = index + 1
        room_data = data[room_data_start:]
        dicts = room_data[0]
        for _dict in dicts:
            rooms.insert(_dict)
        return

    def insert(self, data: dict):
        """
        """
        new_node = _Room(data['name'], data['description'], \
                data['dependencies'], data['enemies'], \
                data['adjacent'])
        self.__values.append(new_node)
        return    

    def first(self):
        """
        Returns the first Room added
        """
        return self.__values[0]

    def __str__(self):
        return f"Num Rooms: {len(self.__values)}"

    def __iter__(self):
        for room in self.__values:
            yield room