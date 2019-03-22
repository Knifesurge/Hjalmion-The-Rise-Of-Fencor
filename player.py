#Nick Mills

class Player():
    def __init__(self, hp, max_hp, level, xp, xp_to_level):
        self.__hp = hp
        self.__max_hp = max_hp
        self.__level = level
        self.__xp = xp
        self.__xp_to_level = xp_to_level
        self.__victory = False
        self.__inventory = {"Gold": 15}
        
    def is_alive(self):
        return self.__hp > 0
    
    def health(self):
        return self.__hp

    def inventory(self):
        return self.__inventory

    def levelUp(self):
            self.__level += 1
            self.__hp = 100
            self.__max_hp = self.__hp * 1.10
            self.__xp_to_level *= 2
            print("You have reached level {}!".format(self.__level))
            return self.__level, self.__hp, self.__max_hp, self.__xp_to_level
