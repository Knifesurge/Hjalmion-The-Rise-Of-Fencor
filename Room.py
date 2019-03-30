# Nick Mills
# Created: 2019-03-22
# Updated 2019-03-22

from random import randint

class _Room():
    def __init__(self, name="Unnamed Room",\
        description="No description given",dependencies=[],\
        enemies=[],adj={}):
        self.__description = description
        self.__dependencies = dependencies
        self.__enemies = enemies
        # Dict of adjacent rooms
        adjacent_rooms = adj['adjacent']
        keys = adjacent_rooms.keys()
        self.__north = adj['n'] if 'n' in keys else None
        self.__south = adj['s'] if 's' in keys else None
        self.__east = adj['e'] if 'e' in keys else None
        self.__west = adj['w'] if 'w' in keys else None
        self.__neast = adj['ne'] if 'ne' in keys else None
        self.__seast = adj['se'] if 'se' in keys else None
        self.__swest = adj['sw'] if 'sw' in keys else None
        self.__nwest = adj['nw'] if 'nw' in keys else None

    def description(self):
        return self.__description

    def enemies(self):
        return self.__enemies
    
    def north(self):
        return self.__north

    def south(self):
        return self.__south

    def east(self):
        return self.__east

    def west(self):
        return self.__west

    def __str__(self):
        return """{}
        {}\t{}
        {}\t{}""".format(self.__description, self.__north, \
            self.__east, self.__west, self.__south)

class Rooms():
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__values = []
        self.__count = 0

    def insert(self, data: dict):
        """
        """
        new_node = _Room(data['name'], data['desc'], \
                data['enem'], data['rooms'])
        if self.__first is None:
            self.__first = new_node
            self.__last = new_node
            self.__values.append(new_node)
        else:
            self.__last = new_node
            self.__values.append(new_node)
        self.__count += 1
        return    

    def first(self):
        """
        Returns the first Room added
        """
        return self.__first

    def __str__(self):
        return f"Num Rooms: {self.__count}"

    def __iter__(self):
        for room in self.__values:
            yield room