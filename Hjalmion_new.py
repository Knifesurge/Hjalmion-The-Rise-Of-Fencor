# Nick Mills
# Updated: 2019-03-22

""" Hjalmion: The Rise of Fencor """
import time, random

from Chance import chance
from Enemy import Enemy
from Item import Item
from Player import Player
from Room import Rooms
from Utils import Utils

class Hjalmion():
    DATA_REL_PATH = 'data/'
    ENEMY_REL_PATH = DATA_REL_PATH + 'Enemies.json'
    ITEM_REL_PATH = DATA_REL_PATH + 'Items.json'
    ROOM_REL_PATH = DATA_REL_PATH + 'Rooms.json'

    def __init__(self):
        """ Room creation """
        self.rooms = Rooms()
        
        """ Player and Enemy creation """
        self.player = Player(100, 100, 1, 0, 100)
        Utils.read_json(self.ENEMY_REL_PATH)
        self.enemies = Enemy.create_from_filedata()

        """ Item creation """
        Utils.read_json(self.ITEM_REL_PATH)
        self.items = Item.create_from_filedata()

        """ Room creation """
        Utils.read_json(self.ITEM_REL_PATH)
        self.rooms = Rooms()
        Rooms.create_from_filedata(self.rooms)

    def get_enemy(self, name : str) -> Enemy:
        """
        """

        return self.enemies[name]

    def show_graphic(self):

        print("\n\n")
        print("                                  ]=|==||==|=[")
        print("                                   \\\\__||__//                  ]=|==||==|=[")
        print("              ]=|==||==|=[          |.. ` *|                    \\\\__||__//")
        print("               \\\\--||--//           |. /\\ #|                     |-_ []#|")
        print("                | []   |            |  ## *|                     |      |")
        print("                |    ..|            | . , #|                   ]=|==||==|=[")
        print("___   ___  ___  |   .. |         __ |..__.*| __                 \\\\__||__//")
        print("] |---| |--| [  |..    |        |  ||-|  |-|| |                  |    _*|")
        print("]____________[  |    []|         \\--\\-|-|--/-//                  |   _ #|")
        print("\\_\\| |_| |/_/   |_   _ | _   _   _|       ' *|                   |`    *|")
        print(" |  .      |'-'-` '-` '-` '-` '-` | []      #|-|--|-_-_-_-_ _ _ _|_'   #|")
        print(" |     '   |=-=-=-=-=-=-=-=-=-=-=-|       []*|-----________` ` `   ]   *|")
        print(" |  ` ` [] |      _-_-_-_-_  '    |-        #|      ,    ' ```````['  _#|")
        print(" | '  `  ' |   [] | | | | |  []`  |   []    *|   `          . `   |'  |*|")
        print(" |      -  |    ` | | | | | `     |  ;  '   #|     .  |        '  |    #|")
        print("/_'_-_-____-\\__,__|_|_|_|_|_______|    `  , *|    _______+___,__,-/._.._.\\     ")
        print("             _,--'    __,-'       /,_,_v_Y_,_v\\\\-'")
        print("\nWelcome to Hjalmion: The Rise of Fencor...")
        input("\n\tPress enter: ")

    def intro(self):
        print("\n\nYou wake up in a meadow. You know nothing except your heritage: You are the son of Dragox, son of Romox.")
        time.sleep(4)
        print("\nYour father was a great king, the greatest of his generation. He ruled for 700 years. Your family has always been kings and queens of the land.")
        time.sleep(6)
        print("\nSince you were born 200 years into your father's rule; you know the land better than anyone else. The people know you and respect you.")
        time.sleep(5)
        print("\nWhen your father died you became king. You ruled for 2000 years, the longest anyone from your bloodline has ever ruled. Then, it happened.")
        time.sleep(5)
        print("\nThis is the story of what happened a mere 10,265,349 years ago...")
        time.sleep(3)
        print("\nNote: You can view your inventory at any time by typing \"i\" as a choice!\n\nAlso, type \"save\" to save your game while in a room, and \"load\" to load your game!\n\nAs well, you can type \"look\" to look around a room to find items you couldn't originally see!\n\nFor more help, type \"help\" while in a room! ")
        input("\n\tPress enter: ")
        self.rooms['meadow']()
