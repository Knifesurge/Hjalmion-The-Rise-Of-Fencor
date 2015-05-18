#Nick Mills

import random, enemies, chance, player

class Item():
    """Base class for all Items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "\n{}\n=====\n{}\nValue: {}".format(self.name, self.description, self.value)

class KeyItems(Item):
    """Base class for all Key Items"""
    def __init__(self, name, description, value):
        super().__init__(name, description, value)
    
    def __str__(self):
        return "\n{}\n*****\n{}\nValue: {}".format(self.name, self.description, self.value)
    
class CellarKey(KeyItems):
    def __init__(self):
        super().__init__(name="Cellar Key",
                         description="A small key to unlock a cellar.",
                         value=0)

class Torch(KeyItems):
    def __init__(self):
        super().__init__(name="Torch",
                         description="A torch that lets you see in the dark. Somehow does not burn out.",
                         value=0)
        
class Book(KeyItems):
    def __init__(self):
        super().__init__(name="Book",
                         description="A book name \"The History of the Skeleton King\". Of no use to you.",
                         value=0)
        
class GreatOakKey(KeyItems):
    def __init__(self):
        super().__init__(name="Great Oak Key",
                         description="A large diamond key that has a picture of the Great Oak on it.",
                         value=0)
        
class Note(KeyItems):
    def __init__(self):
        super().__init__(name="Note",
                         description="A note from your father. Type in \"read note\" to read in any room.",
                         value=0)
        
class JewelEgg(KeyItems):
    def __init__(self):
        super().__init__(name="Jewel Egg",
                         description="A jewel-encrested egg. Surprisingly heavy for how small it is.",
                         value=0)
    
class LegendarySword(KeyItems):
    def __init__(self):
        super().__init__(name="Legendary Sword",
                         description="The sword of legend. Legend has it that when put through something into a hidden key hole, the passage to Shangri-La will be opened",
                         value=0)
        
class TriForce(KeyItems):
    def __init__(self):
        super().__init__(name="TriForce",
                         description="A triangle seperated by smaller triangles. The triangle in the middle is missing however, so there is a hole in it.",
                         value=0)
        
class Healer(Item):
    """Base class for Potions"""
    def __init__(self, name, description, value, healing, life_increase):
        self.healing = healing
        self.life_increase = life_increase
        super().__init__(name, description, value)

    def ___str___(self):
        return "\n{}\n=====\n{}\nValue: {}\nHealth Gained: {}\nLife Increase: {}".format(self.name, self.description, self.value, self.healing, self.life_increase)

    def heal(player, healing):
        player.hp += healing
        return player.hp

    def increase_life(player, life_increase):
        player.hp = player.max_hp
        player.max_hp += life_increase
        player.hp = player.max_hp
        return player.hp, player.max_hp
    
    def full_restore(player):
        player.hp = player.max_hp
        return player.hp, player.max_hp
    
class Potion(Healer):
    def __init__(self):
        super().__init__(name="Potion",
                         description="A red potion that heals 50 hp. Single-Use only.",
                         value=15,
                         healing=50,
                         life_increase=0)

class FullPotion(Healer):
        def __init__(self):
            super().__init__(name="Full Potion",
                             description="A orange potion that heals you to max hp! Single-Use only.",
                             value=40,
                             healing=0, #0 is used as a placeholder, the healing is actually Player.max_hp but the full_restore function in Healer handles that
                             life_increase=0)

class LifePotion(Healer):
    def __init__(self):
        super().__init__(name="Life Potion",
                         description="A potion with a gold color. Increases HP by 100.",
                         value=50,
                         healing=0,
                         life_increase=100)


class Weapon(Item):
    """Base class for all Weapons"""
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "\n{}\n=====\n{}\nValue: {}\nDamage: {}\n".format(self.name, self.description, self.value, self.damage)

class SuperWeapon(Weapon):
    """Base class for all Legendary Weapons"""
    def __init__(self, name, description, value, damage, magic_dmg, poison_dmg, bleed_dmg):
        self.magic_dmg = magic_dmg
        self.poison_dmg = poison_dmg
        self.bleed_dmg = bleed_dmg
        super().__init__(name, description, value, damage)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A sizeable rock that can easily smash someone's skull in.",
                         value=0,
                         damage=5)
    def accuracy():
        if (chance(95)):
            damage = damage
            return damage
        else:
            damage = 0
            return damage

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                       description="A shiny dagger with some rust. Somewhat more dangerous than a rock.",
                       value=10,
                       damage=10)
    def accuracy():
        if (chance(95)):
            damage = damage
            return damage
        else:
            damage = 0
            return damage

class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="An average sized sword. Deadly in the hands of a swordsman.",
                         value=15,
                         damage=20)
    def accuracy():
        if (chance(95)):
            damage = damage
            return damage
        else:
            damage = 0
            return damage

class HeavySword(Weapon):
    def __init__(self):
        super().__init__(name="Heavy Sword",
                         description="A large sword that requires two hands to swing",
                         value=20,
                         damage=25)
    def accuracy():
        if (chance(80)):
            damage = damage
            return damage
        else:
            damage = 0
            return damage

class Bow(Weapon):
    def __init__(self):
        super().__init__(name="Bow",
                         description="A huntsman's bow. Deadly at a range, useless at point blank.",
                         value=15,
                         damage=25)
    def accuracy():
        if (chance(85)):
            damage = damage
            return damage
        else:
            damage = 0
            return damage

class Crossbow(Weapon):
    def __init__(self):
        super().__init__(name="Crossbow",
                         description="Two handed crossbow. Deadly at all ranges. More effective at a larger range than a huntsman's bow.",
                         value=20,
                         damage=30)
    def accuracy():
        if (chance(70)):
            damage = damage
            return damage
        else:
            damage = 0
            return damage

class Handcannon(Weapon):
    def __init__(self):
        super().__init__(name="Handcannon",
                         description="A cannon that fits in your hand. Deadly. End. Of. Story.",
                         value=50,
                         damage=50)
    def accuracy():
        if (chance(75)):
            damage = damage
            return damage
        else:
            damage = 0
            return damage

class Krambit(Weapon):
    def __init__(self):
        super().__init__(name="Krambit",
                         description="Small knife with a curved edge. Worth $262 with no skins. Lots of skins available. \"Such skins, very wow\"",
                         value=262,
                         damage=70)
    def accuracy():
        if (chance(99)):
            damage = damage
            return damage
        else:
            damage = 0
            return damage

class SwordOfDragox(SuperWeapon):
    def __init__(self):
        super().__init__(name="Sword Of Dragox",
                       description="The sword of your father, Dragox. It hums with a mystical energy.",
                       value=1000,
                       damage=100,
                       magic_dmg=50,
                       poison_dmg=0,
                       bleed_dmg=0)
    def accuracy():
        if (chance(75)):
            damage = damage + magic_dmg
            return damage
        else:
            damage = 0
            return damage

class ScepterOfRomox(SuperWeapon):
    def __init__(self):
        super().__init__(name="Scepter of Romox",
                         description="The scepter of your father's father, Romox. Drips with poison.",
                         value=2500,
                         damage=200,
                         magic_dmg=0,
                         poison_dmg=150,
                         bleed_dmg=0)
    def accuracy():
        if (chance(60)):
            damage = damage + poison_dmg
            return damage
        else:
            damage = 0
            return damage

class UmariOfFencor(SuperWeapon):
    def __init__(self):
        super().__init__(name="Umari of Fencor",
                         description="The umari of your uncle, Fencor. It is a whip with small daggers at the ends that is covered in blood. Hard to master.",
                         value=10000,
                         damage=500,
                         magic_dmg=0,
                         poison_dmg=0,
                         bleed_dmg=400)
    def accuracy():
        if (chance(50)):
            damage = damage + bleed_dmg
            return damage
        else:
            damage = 0
            return damage
