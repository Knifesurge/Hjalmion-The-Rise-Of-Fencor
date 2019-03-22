# Nick Mills
# Updated 2019-03-22

from random import randint

class Room():
    def __init__(self):
        self.__west = None
        self.__east = None
        self.__north = None
        self.__south = None
        self.__description = ""
        self.__enemies = []
    
    def west(self):
        return self.__west

    def east(self):
        return self.__east

    def north(self):
        return self.__north

    def south(self):
        return self.__south

    def enemies(self):
        return self.__enemies

    def get_enemy(self):
        rand = randint(0, len(self.__enemies))
        return self.__enemies[rand]

    def __str__(self):
        return """{}\n\nWest: {}\tEast: {}
            North: {}\tSouth: {}""".format(self.__description, \
                self.__west, self.__east, self.__north, self.__south)