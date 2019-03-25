#Nick Mills
# Created: 2015-05-18
# Updated: 2019-03-24

import random
from Chance import chance
from Utils import Utils

class Enemy():
    """Base class for all Enemies"""
    def __init__(self, name:str, hp:int, \
        dmg:int, crit:float, xp:int, boss:bool):
        self.name = name
        self.max_hp = hp
        self.hp = self.max_hp
        self.damage = dmg
        self.crit_mult = crit
        self.xp = xp
        self.boss = boss

    def is_alive(self):
        """
        Returns whether this entity has more than 
        0 health
        Use: alive = enemy.is_alive()

        Parameters:
            None
        Returns:
            alive - Whether this entity has more than 
                    0 health (bool)
        """
        return self.hp > 0

    def __str__(self):
        return """Name: {}
        HP: {}/{}
        Base Dmg: {}
        Crit Mult: {}
        XP Worth: {}
        Boss? {}""".format(self.name, self.hp,\
            self.max_hp, self.damage, self.crit_mult,\
            self.xp, self.boss)

    def attack(self, other):
        """
        ---------------------------------------------
        Attacks another entity. This function directly
        modifies the other entity's health.
        Use dmg, crit = enemy.attack(other)
        ---------------------------------------------
        Parameters:
            other - The entity to attack
        Returns:
            damage - The damage dealt to the entity (float)
            crit - Whether the attack dealth crit dmg (bool)
        ---------------------------------------------
        """
        if self.crit_mult != 1:
            if chance(20):
                crit = True
                damage = self.damage * self.crit_mult
            crit = False
        else:
            crit = False
            damage = self.damage
        other.deal_damage(damage)
        return damage, crit

    @staticmethod
    def create_from_filedata() -> list:
        """
        ---------------------------------------------
        Creates a list of Enemies from the cached filedata 
        that was previously read.
        Use: enemies = Enemy.create_from_filedata()
        ---------------------------------------------
        Parameters:
            None
        Returns:
            enemies - list of Enemies created from cached 
                      filedata (list of Enemy)
        ---------------------------------------------
        """
        data = Utils.get_data()
        enemies = []
        for i in range(len(data)):
            # data is a list of dicts
            #print("D: {}".format(type(d)))
            _dict = data[i]
            if _dict is not None:
                for j in range(len(_dict)):
                        # l is each dict in data
                        l = _dict[j]
                        #print("L: {}".format(type(l)))
                        #print(l)
                        #print("Vals: {}".format(l.values()))
                        name = l['name']
                        health = l['max_health']
                        dmg = l['base_dmg']
                        crit = float(l['crit_mult'])
                        xp = l['xp_worth']
                        boss = l['boss'] == 'Y'
                        enemy = Enemy(name, health, dmg, \
                            crit, xp, boss)
                        enemies.append(enemy)
        return enemies

class Boss(Enemy):
    """Base class for all Bosses"""
    def critical_attack(self):
        critdmg = self.damage * 2
        if (chance(70)):
            return("{} hit you for a critical of {} damage!".format(self.name, self.critdmg))
        else:
            return("{} tried to critical hit you for {} damage, but failed".format(self.name, self.critdmg))

class Rat(Enemy):
    def __init__(self):
        super().__init__(name="Rat",
                         hp=5,
                         max_hp=5,
                         damage=5,
                         xp=3)
class Snake(Enemy):
    def __init__(self):
        super().__init__(name="Snake",
                         hp=5,
                         max_hp=5,
                         damage=5,
                         xp=5)
class Bird(Enemy):
    def __init__(self):
        super().__init__(name="Bird",
                         hp=12,
                         max_hp=12,
                         damage=6,
                         xp=7)
        
class Spider(Enemy):
    def __init__(self):
        super().__init__(name="Spider",
                         hp=10,
                         max_hp=10,
                         damage=5,
                         xp=10)
class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider",
                         hp=20,
                         max_hp=20,
                         damage=10,
                         xp=25)
class Skeleton(Enemy):
    def __init__(self):
        super().__init__(name="Skeleton",
                         hp=50,
                         max_hp=50,
                         damage=10,
                         xp=50)
class SkeletonArcher(Enemy):
    def __init__(self):
        super().__init__(name="Skeleton Archer",
                         hp=45,
                         max_hp=45,
                         damage=15,
                         xp=55)
class SkeletonKnight(Enemy):
    def __init__(self):
        super().__init__(name="Skeleton Knight",
                         hp=90,
                         max_hp=90,
                         damage=30,
                         xp=75)
class SkeletonKing(Boss):
    def __init__(self):
        super().__init__(name="Skeleton King",
                         hp=200,
                         max_hp=200,
                         damage=50,
                         xp=500)
class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf",
                         hp=30,
                         max_hp=30,
                         damage=10,
                         xp=20)
class DireWolf(Enemy):
    def __init__(self):
        super().__init__(name="Dire Wolf",
                         hp=50,
                         max_hp=50,
                         damage=20,
                         xp=50)
class RabidBunny(Enemy):
    def __init__(self):
        super().__init__(name="Rabid Bunny",
                        hp=10,
                        max_hp=10,
                        damage=10,
                        xp=10)
class CrazedVillager(Enemy):
    def __init__(self):
        super().__init__(name="Crazed Villager",
                         hp=50,
                         max_hp=50,
                         damage=10,
                         xp=30)
class Zombie(Enemy):
    def __init__(self):
        super().__init__(name="Zombie",
                         hp=40,
                         max_hp=40,
                         damage=30,
                         xp=40)
class Dragon(Boss):
    def __init__(self):
        super().__init__(name="Dragon",
                         hp=300,
                         max_hp=300,
                         damage=70,
                         xp=700)
class Dragox(Boss):
    def __init__(self):
        super().__init__(name="Dragox",
                         hp=500,
                         max_hp=500,
                         damage=100,
                         xp=1000)

class Romox(Boss):
    def __init__(self):
        super().__init__(name="Romox",
                         hp=1500,
                         max_hp=1500,
                         damage=200,
                         xp=1000)

class Fencor(Boss):
    def __init__(self):
        super().__init__(name="Fencor",
                         hp=2000,
                         max_hp=2000,
                         damage=500,
                         xp=2500)
