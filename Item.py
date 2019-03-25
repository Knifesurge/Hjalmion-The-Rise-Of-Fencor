#Nick Mills
# Created: 2015-05-18
# Updated: 2019-03-24

from Player import Player
from Chance import chance
from Enemy import Enemy
from Utils import Utils

class Item():
    """Base class for all Items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    @staticmethod
    def create_from_filedata() -> list:
        """
        ---------------------------------------------
        Creates a list of Items from the cached filedata 
        that was previously read.
        Use: items = Item.create_from_filedata()
        ---------------------------------------------
        Parameters:
            None
        Returns:
            items - list of Items created from cached 
                      filedata (list of Item)
        ---------------------------------------------
        """
        data = Utils.get_data()
        item_data_start = 0
        index = 0
        while data[index] is not None:
            index += 1
        item_data_start = index + 1
        items = []
        item_data = data[item_data_start:]
        dicts = item_data[0][0]
        list_weapons = dicts['Weapons']
        list_s_weapons = dicts['Super Weapons']
        list_healers = dicts['Healers']
        list_key_items = dicts['Key Items']
        for weapon in list_weapons:
            name = weapon['name']
            desc = weapon['description']
            val = weapon['value']
            dmg = weapon['damage']
            weapon = Weapon(name, desc, val, dmg)
            items.append(weapon)
        for s_weapon in list_s_weapons:
            name = s_weapon['name']
            desc = s_weapon['description']
            val = s_weapon['value']
            dmg = s_weapon['damage']
            b_dmg = s_weapon['bonus_damage']
            superweapon = SuperWeapon(name, desc, val, \
                dmg, b_dmg)
            items.append(superweapon)
        for healer in list_healers:
            name = healer['name']
            desc = healer['description']
            val = healer['value']
            healing = healer['healing']
            life_increase = healer['life_increase']
            heal = Healer(name, desc, val, healing, life_increase)
            items.append(heal)
        for key in list_key_items:
            name = key['name']
            desc = key['description']
            val = key['value']
            key_item = KeyItem(name, desc, val)
            items.append(key_item)
        return items

class KeyItem(Item):
    """Base class for all Key Items"""
    def __init__(self, name, description, value):
        super().__init__(name, description, value)
    
    def __str__(self):
        return "\n{}\n".format(self.name)+("*"*len(self.name))+"\n{}\nValue: {}".format(self.description, self.value)

class Weapon(Item):
    """Base class for all Weapons"""
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "\n{}\n".format(self.name)+("="*len(self.name))+"\n{}\nValue: {}\nDamage: {}\n".format(self.description, self.value, self.damage)

class SuperWeapon(Weapon):
    """Base class for all Legendary Weapons"""
    def __init__(self, name, description, value, damage, bonus_damage):
        super().__init__(name, description, value, damage + bonus_damage)

class Healer(Item):
    """Base class for Potions"""
    def __init__(self, name, description, value, healing, life_increase):
        self.healing = healing
        self.life_increase = life_increase
        super().__init__(name, description, value)

    def __str__(self):
        return "\n{}\n".format(self.name)+("="*len(self.name))+"\n{}\nValue: {}\nHealth Gained: {}\nLife Increase: {}".format(self.description, self.value, self.healing, self.life_increase)

    def heal(self, player, healing):
        player.hp += healing
        return player.hp

    def increase_life(self, player, life_increase):
        player.hp = player.max_hp
        player.max_hp += life_increase
        player.hp = player.max_hp
        return player.hp, player.max_hp
    
    def full_restore(self, player):
        player.hp = player.max_hp
        return player.hp, player.max_hp