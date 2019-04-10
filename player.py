# Nick Mills
# Created:
# Updated: 2019-04-10

from Room import _Room as Room

class Player():
    def __init__(self, hp, max_hp, level, xp, xp_to_level, start_room):
        """
        """
        self.__hp = hp
        self.__max_hp = max_hp
        self.__level = level
        self.__xp = xp
        self.__xp_to_level = xp_to_level
        self.__inventory = {"Gold": 15}
        self.__curr_room = start_room
        
    def is_alive(self):
        """
        """
        return self.__hp > 0
    
    def health(self):
        """
        """
        return self.__hp

    def inventory(self):
        """
        """
        return self.__inventory

    def room(self) -> Room:
        """
        """
        return self.__curr_room

    def move_room(dir : str) -> bool:
        """
        """
        moved = False
        if dir in self.__curr_room.rooms():
            new_room = self.__curr_room.rooms[dir]
            

    def level_up(self):
        """
        """
        self.__level += 1
        self.__hp = 100
        self.__max_hp = self.__hp * 1.10
        self.__xp_to_level *= 2
        print("You have reached level {}!".format(self.__level))
        return self.__level, self.__hp, self.__max_hp, self.__xp_to_level
