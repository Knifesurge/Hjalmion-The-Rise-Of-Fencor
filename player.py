#Nick Mills

class player():
    def __init__(self, hp, max_hp, level, xp, xp_to_level, victory):
        self.hp = hp
        self.max_hp = max_hp
        self.level = level
        self.xp = xp
        self.xp_to_level = xp_to_level
        self.victory = victory
        
    def is_alive(self):
        return self.hp > 0 and not self.hp == 0 
        
    def levelUp(self):
            self.level += 1
            self.hp = 100
            self.max_hp = self.hp + 10
            self.xp_to_level = 100
            print("You have reached level {}!".format(self.level))
            return self.level, self.hp, self.max_hp, self.xp_to_level
    
class Player(player):
    def __init__(self):
        super().__init__(hp = 100,
                         max_hp = 100,
                         level = 1,
                         xp = 0,
                         xp_to_level = 100,
                         victory = 0)
