#Nick Mills
# Created: 2015-05-18
# Updated: 2015-10-13

import random, chance, items

class Enemy():
    """Base class for all Enemies"""
    def __init__(self, name, hp, max_hp, damage, xp):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.damage = damage
        self.xp = xp

    def is_alive(self):
        return self.hp > 0

class Boss(Enemy):
    """Base class for all Bosses"""
    def critical_attack(self):
        critdmg = self.damage * 2
        chance()
        if (chance <= 70):
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
