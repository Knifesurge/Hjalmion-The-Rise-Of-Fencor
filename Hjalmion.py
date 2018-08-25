#Nick Mills
"""Hjalmion: The Rise of Fencor"""
import time, random #Imports libraries for use
import chance, enemies, items, player #Imports other modules used to run the game

#Create the Player object and all of the Enemies *Most Common to Least Common*
player = player.Player() #Creates the Player object
rat = enemies.Rat()
snake = enemies.Snake()
bird = enemies.Bird()
spider = enemies.Spider()
giant_spider = enemies.GiantSpider()
skeleton = enemies.Skeleton()
skeleton_archer = enemies.SkeletonArcher()
skeleton_knight = enemies.SkeletonKnight()
skeleton_king = enemies.SkeletonKing()
skeletonKing_death = False #Variable to store whether or not the Skeleton King is dead (helps with checking events)
wolf = enemies.Wolf()
dire_wolf = enemies.DireWolf()
rabid_bunny = enemies.RabidBunny()
crazed_villager = enemies.CrazedVillager()
zombie = enemies.Zombie()
dragon = enemies.Dragon()
dragon_death = False
dragox = enemies.Dragox()
dragox_death = False
romox = enemies.Romox()
romox_death = False
fencor = enemies.Fencor()

#Create all Weapons *Highest Damage to Lowest Damage*
fencor_umari = items.UmariOfFencor()
umari_inventory = False #To help determine whether or not this item is in the inventory
romox_scepter = items.ScepterOfRomox()
scepter_inventory = False
dragox_sword = items.SwordOfDragox()
dSword_inventory = False
krambit = items.Krambit()
krambit_inventory = False
handcannon = items.Handcannon()
handcannon_inventory = False
crossbow = items.Crossbow()
crossbow_inventory = False
bow = items.Bow()
bow_inventory = False
heavy_sword = items.HeavySword()
heavySword_inventory = False
sword = items.Sword()
sword_inventory = False
dagger = items.Dagger()
dagger_inventory = False
rock = items.Rock()
rock_inventory = False

#Create all the Key Items in the game *In order of need*
cellarKey = items.CellarKey()
cellarKey_inventory = False
torch = items.Torch()
torch_inventory = False
book = items.Book()
book_inventory = False
great_oak_key = items.GreatOakKey()
greatOakKey_inventory = False
note = items.Note()
note_inventory = False
jewel_egg = items.JewelEgg()
jewelEgg_inventory = False
legendary_sword = items.LegendarySword()
legendarySword_inventory = False
triforce = items.TriForce()
triforce_inventory = False

#Create all the Items in the game
potion = items.Potion()
potion_inventory = 1 #Keeps track of how many Potions the player has
life_potion = items.LifePotion()
lifePotion_inventory = 0 #Keeps track of how many Life Potions the player has
full_potion = items.FullPotion()
fullPotion_inventory = 0 #Keeps track of how many Full Potions the player has

#Other variables
skeletonCaveRoom_active = False
best_weapon = None
counter = 0 #Used for Village to make sure the Player can pick up the gold only once
flag = True #Used for Forest
flag1 = True #Used for House
flag2 = True #Used for Cave
flag3 = True #Used for Marketplace
flag4 = True #Used for Church
flag5 = True #Used for Dead-End Valley
random_gold = random.randrange(10, 51) #Determines how much gold the Player finds when they search a room
gameOver = False #Tracks whether or not the game is over or still playing

#Counters to keep track of how many times the player has "looked" in each room
meadow_counter = 0
deadEndValley_counter = 0
dungeon_counter = 0
village_counter = 0
forest_counter = 0
cliffside_counter = 0
greatOak_counter = 0
cellar_counter = 0
skeletonCave_counter = 0
cave_counter = 0
secretPassage_counter = 0
dragonsLair_counter = 0
church_counter = 0
cemetary_counter = 0
market_counter = 0
castle_counter = 0

player_gold = 15 #Amount of gold the player has
active_room = None
blacksmith_buy = {"\nSword|Cost: 15g":sword, "\nHeavy Sword|Cost: 50g":heavy_sword, "\nBow|Cost: 20g":bow, "\nCrossbow|35g":crossbow} #Everything that is in the blacksmith's shop to buy

shop_buy = {"\nPotion| 20g":potion, "\nLife Potion| 100g":life_potion, "\nFull Potion| 40g":full_potion, "\nTorch|Cost: 5g":torch} #Everything that is in the shop to buy

def show_graphic():

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

def intro():
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
    meadow()

def meadow():
    #Allows use of global variables
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global cellarKey_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global random_gold
    global meadow_counter
    global gameOver
    global active_room
    active_room = "meadow"
    if (not rock_inventory):
        print("\nYou are in a beautiful meadow. You see a deer leap through the grass in the distance. You see a house to the North West, a forest to the South, the Great Oak to the West, a small village with a castle in the East, and a cliffside to the North. You see a rock on the ground.")
    elif (rock_inventory):
        print("\nYou are in a beautiful meadow. You see a deer leap through the grass in the distance.\nYou see a house to the North West, a forest to the South, the Great Oak to the West, a small village with a castle in the East,\nand a cliffside to the North.")
    if (chance.chance(50) and rock_inventory):
        print("\nA snake comes out and attacks you!")
        battle(player, snake)

    choice = 7
    while(choice != "y" and choice != "n" and not rock_inventory):
        choice = input("\n\tDo you want to pick up the rock?(Y/N)").lower()
        if (choice == "y"):
            print("\nYou pick up the rock")
            rock_inventory = True
        elif (choice == "n"):
            print("\nAre you sure? You will 110% need it in the future!")
            choice = 7
            while(choice != "y" and choice != "n"):
                choice = input("\n\tPick up the rock?").lower()
                if(choice == "y"):
                    print("\nYou pick up the rock")
                    rock_inventory = True
                elif(choice == "n"):
                    print("\nDon't say I didn't warn you! These lands are dangerous lands...")
    choice = 7
    while(choice != "n" and choice != "nw" and choice != "e" and choice != "w" and choice != "s"):
        choice = input("\nRoom: Meadow\n\nWill you go (N)orth, (N)orth (W)est, (W)est, (E)ast, or (S)outh?").lower()
        if (choice == "n"):
            cliffside()
        elif (choice == "nw"):
            house()
        elif (choice == "e"):
            village()
        elif (choice == "w"):
            great_oak()
        elif (choice == "s"):
            forest()
        elif (choice == "look" and meadow_counter == 0):
            print("You look around and find {} Gold!".format(random_gold))
            player_gold += random_gold
            meadow_counter += 1
        elif (choice == "look" and meadow_counter > 0):
            print("You look around and find nothing.")
        elif (choice == "p"):
            usePotion()
        elif (choice == "lp"):
            useLifePotion()
        elif (choice == "fp"):
            useFullPotion()
        elif (choice == "help"):
            help()
        elif (choice == "save"):
            save_game()
        elif (choice == "load"):
            load_game()
        elif (choice == "i"):
            view_inventory()
        else:
            print("\nPlease enter a valid input!")

def great_oak():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global cellarKey_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global random_gold
    global greatOak_counter
    global gameOver
    global active_room
    active_room = "great oak"
    if (greatOakKey_inventory):
        print("\nYou walk up to the Great Oak. It hums with energy.")
        time.sleep(3)
        print("\nYou notice a small, key shaped hole that you did not notice before. You go up to it and slide the key into the hole.")
        time.sleep(3)
        print("\nIt unlocks and the Great Oak opens. You walk inside and walk down a spiral staircase.")
        time.sleep(3)
        print("\nAt the bottom there is a long hallway with a pedestal at the end. You walk down and look at the pedestal.")
        time.sleep(3)
        print("\nOn the pedestal is the legendary TriForce!")
        choice = 7
        while (choice != "y" and choice != "n"):
            choice = input("\n\tDo you want to pick up the TriForce?(Y/N)").lower()
            if (choice == "y"):
                print("\nYou pick up the TriForce and leave the Great Oak. The tree closes behind you and everything returns to normal.")
                triforce_inventory = True
                great_oak()
            elif (choice =="n"):
                print("nAre you crazy?!?? This is the legendary TriForce! One of the keys to the magical land of Shangri-La!! You would be crazy to not take it!")
                choice = 7
                while (choice != "y" and choice != "n"):
                    choice = input("\nWill you pick up the TriForce now?(Y/N)").lower()
                    if (choice == "y"):
                        print("\nThats better. You pick up the TriForce and leave the Great Oak. The tree closes behind you and everything returns to normal.")
                        triforce_inventory = True
                    elif (choice == "n"):
                        print("\nI won't stand around here and wait for you to pick up the next key item in completing the game. You pick up the TriForce and leave the Great Oak. The tree closes behind you and everything returns to normal.")
                        triforce_inventory = True
    else:
        print("\nYou walk up to the Great Oak. It hums with energy. Birds chirp and you see a nest in one of the branches. There is a meadow to the East.")
        if(chance.chance(50)):
            print("\nA snake slithers up and attacks you!")
            battle(player, snake)
        elif(chance.chance(40)):
            print("\nA bird flies down and attacks you!")
            battle(player, bird)
        if(gameOver):
            raise SystemExit
        elif(not gameOver):  
            choice = 7
            while(choice != "e"):
                choice = input("\nRoom: Great Oak\n\nWill you go to the (E)ast?").lower()
                if (choice == "e"):
                    meadow()
                elif (choice == "i"):
                    view_inventory()
                elif (choice == "p"):
                    usePotion()
                elif (choice == "lp"):
                    useLifePotion()
                elif (choice == "help"):
                    help()
                elif (choice == "save"):
                    save_game()
                elif (choice == "load"):
                    load_game()
                elif (choice == "fp"):
                    useFullPotion()
                elif (choice == "look" and note_inventory):
                    print("\nYou look around and see a shiny object in the birds nest. You go up to it and find a jewel encrested egg.")
                    choice = 7
                    while (choice != "y" and choice != "n"):
                        choice = input("\nWill you take the egg?(Y/N)").lower()
                        if (choice == "y"):
                            print("\nYou take the egg.")
                            jewelEgg_inventory = True
                        elif (choice == "n"):
                            print("\nYou do not take the egg.")
                        else:
                            print("\nPlease enter a valid input!")
                elif (choice == "look" and greatOak_counter == 0):
                    print("You look around...")
                    find_potion()
                    greatOak_counter += 1
                elif (choice == "look" and greatOak_counter > 0):
                    print("You look around but find nothing.")
                else:
                    print("\nPlease enter a valid input!")

def house():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global cellarKey_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global flag1
    global gameOver
    global active_room
    active_room = "house"
    if(flag1):
        print("\nYou enter a small house. It is falling apart. You look around and see a small hatch to the East. You assume it leads to a cellar. There is a meadow to the South. You see some gold on the ground.")
        choice = 7
        while(choice != "y" and choice != "n"):
            choice = input("\n\tWill you pick up the gold?(Y/N)").lower()
            if(choice == "y"):
                print("\nYou pick up the 20 Gold!")
                player_gold += 20
                flag1 = False
            elif(choice == "n"):
                print("\nNot sure why, but you do not pick up the gold!")
        if(chance.chance(50)):
            print("\nA rat skitters across the floor and attacks you!")
            battle(player, rat)
        elif(chance.chance(40)):
            print("\nA spider crawls from it's web and attacks you!")
            battle(player, spider)
        if(gameOver):
            raise SystemExit
        elif(not gameOver):                    
            choice = 7
            while(choice != "e" and choice != "s"):
                choice = input("\nRoom: House\n\nWill you go (E)ast or (S)outh?").lower()
                if (choice == "e"):
                    cellar()
                elif (choice == "s"):
                    meadow()
                elif (choice == "p"):
                    usePotion()
                elif (choice == "lp"):
                    useLifePotion()
                elif (choice == "help"):
                    help()
                elif (choice == "save"):
                    save_game()
                elif (choice == "load"):
                    load_game()
                elif (choice == "fp"):
                    useFullPotion()
                elif (choice == "i"):
                    view_inventory()
                elif (choice == "look"):
                    if (not dagger_inventory):
                        print("\nYou look around the house and find a dagger.")
                        choice = 7
                        while(not dagger_inventory and choice != "y" and choice != "n"):
                            choice = input("\n\tDo you want to pick up the dagger?(Y/N)").lower()
                            if (choice == "y"):
                                print("\nYou pick up the dagger.")
                                dagger_inventory = True
                            elif (choice == "n"):
                                print("\nYou do not pick up the dagger.")
                        choice = 7
                        while(choice != "y" and choice != "n"):
                            choice = input("\n\tDo you want to keep looking around?(Y/N)").lower()
                            if (choice == "y" and not cellarKey_inventory):
                                print("\nYou continue looking around. You see a wooden table in the middle of the room that is falling apart. You look in the cupboards and see something shiny.")
                                choice = 7
                                while(not cellarKey_inventory and choice != "y" and choice != "n"):
                                    choice = input("\n\tDo you want to pick up the shiny object?(Y/N)").lower()
                                    if (choice == "y"):
                                        print("\nYou pick up the shiny object and you notice it is a key. It says {} on it.".format(cellarKey.name))
                                        cellarKey_inventory = True
                                    elif (choice == "n"):
                                        print("\nYou do not pick up the shiny object. You go back to the middle of the room.")
                                        house()
                            elif (choice == "y" and cellarKey_inventory):
                                print("\nYou already found the Cellar Key. There is no need for another one (though you wont find another one!)")
                                house()
                            elif (choice == "n"):
                                print("\nYou go back to the middle of the room")
                                house()
                    elif (dagger_inventory and cellarKey_inventory):
                        print("\nYou already found the dagger AND the key! Why are you still looking around?")
                    elif (dagger_inventory and not cellarKey_inventory):
                        print("\nYoulook around. You see a wooden table in the middle of the room that is falling apart. You look in the cupboards and see something shiny.")
                        choice = 7
                        while(not cellarKey_inventory and choice != "y" and choice != "n"):
                            choice = input("\n\tDo you want to pick up the shiny object?(Y/N)").lower()
                            if (choice == "y"):
                                print("\nYou pick up the shiny object and you notice it is a key. It says {} on it.".format(cellarKey.name))
                            elif (choice == "n"):
                                print("\nYou do not pick up the shiny object. You go back to the middle of the room.")
                                house()
                    elif (choice == "y" and cellarKey_inventory):
                        print("\nYou already found the Cellar Key. There is no need for another one (though you wont find another one!)")
                        house()
                    elif (choice == "n"):
                        print("\nYou go back to the middle of the room")
                        house()
                else:
                    print("\nPlease enter a valid input!")
    else:
        print("\nYou enter a small house. It is falling apart. You look around and see a small hatch to the East. You assume it leads to a cellar. There is a meadow to the South.")
    if(chance.chance(50)):
        print("\nA rat skitters across the floor and attacks you!")
        battle(player, rat)
    elif(chance.chance(40)):
        print("\nA spider crawls from it's web and attacks you!")
        battle(player, spider)
    if(gameOver):
        raise SystemExit
    elif(not gameOver):        
        choice = 7
        while(choice != "e" and choice != "s"):
            choice = input("\nRoom: House\n\nWill you go (E)ast or (S)outh?").lower()
            if (choice == "e"):
                cellar()
            elif (choice == "s"):
                meadow()
            elif (choice == "p"):
                usePotion()
            elif (choice == "lp"):
                useLifePotion()
            elif (choice == "help"):
                help()
            elif (choice == "save"):
                save_game()
            elif (choice == "load"):
                load_game()
            elif (choice == "i"):
                view_inventory()
            elif (choice == "fp"):
                useFullPotion()
            elif (choice == "look"):
                if (not dagger_inventory):
                    print("\nYou look around the house and find a dagger.")
                    choice = 7
                    while(not dagger_inventory and choice != "y" and choice != "n"):
                        choice = input("\n\tDo you want to pick up the dagger?(Y/N)").lower()
                        if (choice == "y"):
                            print("\nYou pick up the dagger.")
                            dagger_inventory = True
                        elif (choice == "n"):
                            print("\nYou do not pick up the dagger.")
                    choice = 7
                    while(choice != "y" and choice != "n"):
                        choice = input("\nDo you want to keep looking around?(Y/N)").lower()
                        if (choice == "y" and cellarKey_inventory == False):
                            print("\nYou continue looking around. You see a wooden table in the middle of the room that is falling apart. You look in the cupboards and see something shiny.")
                            choice = 7
                            while(not cellarKey_inventory and choice != "y" and choice != "n"):
                                choice = input("\n\tDo you want to pick up the shiny object?(Y/N)").lower()
                                if (choice == "y"):
                                    print("\nYou pick up the shiny object and you notice it is a key. It says {} on it.".format(cellarKey.name))
                                    cellarKey_inventory = True
                                elif (choice == "n"):
                                    print("\nYou do not pick up the shiny object. You go back to the middle of the room.")
                                    house()
                        elif (choice == "y" and cellarKey_inventory):
                            print("\nYou already found the Cellar Key. There is no need for another one (though you wont find another one!)")
                            house()
                        elif (choice == "n"):
                            print("\nYou go back to the middle of the room")
                            house()
                elif (dagger_inventory and cellarKey_inventory):
                    print("\nYou already found the dagger AND the key! Why are you still looking around?")
                elif (dagger_inventory and not cellarKey_inventory):
                    print("\nYoulook around. You see a wooden table in the middle of the room that is falling apart. You look in the cupboards and see something shiny.")
                    choice = 7
                    while(not cellarKey_inventory and choice != "y" and choice != "n"):
                        choice = input("\n\tDo you want to pick up the shiny object?(Y/N)").lower()
                        if (choice == "y"):
                            print("\n\tYou pick up the shiny object and you notice it is a key. It says {} on it.".format(cellarKey.name))
                        elif (choice == "n"):
                            print("\nYou do not pick up the shiny object. You go back to the middle of the room.")
                            house()
                elif (choice == "y" and cellarKey_inventory):
                    print("\nYou already found the Cellar Key. There is no need for another one (though you wont find another one!)")
                    house()
                elif (choice == "n"):
                    print("\nYou go back to the middle of the room")
                    house()

def cellar():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global cellarKey_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global cellar_counter
    global gameOver
    global active_rooom
    active_room = "cellar"
    if (cellarKey_inventory):
        print("\nYou enter a small dark room. You cannot see much. There are some stairs to the West leading up. You see a hole to the South East. It is big enough to climb through.")
    else:
        print("\nYou go up to the cellar, but it is locked. You will need to look around for a key.")
        house()
    if(chance.chance(50)):
        print("\nA giant spider leaps out and attacks you!")
        battle(player, giant_spider)
    elif(chance.chance(40)):
        print("\nA spider leaps from it's web and attacks you!")
        battle(player, spider)
    elif(chance.chance(60)):
        print("\nA rat skitters across the floor and attacks you!")
        battle(player, rat)
    if(gameOver):
        raise SystemExit
    elif(not gameOver):        
        choice = 7
        while(choice != "w" and choice != "se"):
            choice = input("\nRoom: Cellar\n\nWill you go (W)est or (S)outh (E)ast?").lower()
            if (choice == "w"):
                house()
            elif (choice == "se"):
                dungeon()
            elif (choice == "p"):
                usePotion()
            elif (choice == "lp"):
                useLifePotion()
            elif (choice == "help"):
                help()
            elif (choice == "save"):
                save_game()
            elif (choice == "load"):
                load_game()
            elif (choice == "fp"):
                useFullPotion()
            elif (choice == "look" and cellar_counter == 0):
                print("You look around...")
                find_potion()
                cellar_counter += 1
            elif (choice == "look" and cellar_counter > 0):
                print("You look around but find nothing.")
            elif (choice == "i"):
                view_inventory()
            else:
                print("\nPlease enter a valid input!")

def dungeon():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global dungeon_counter
    global gameOver
    global active_room
    active_room = "dungeon"
    if (torch_inventory):
        print("\nYou are in a large dungeon. You see bones scattered around the room carelessly. You should be careful. There is a small hole to the North West and a large hatch to the North.")
    elif (not torch_inventory):
        print("\nIt is too dark to see. You must go back.")
        cellar()
    if(chance.chance(50)):
        print("\nA skeleton comes out and attacks you!")
        time.sleep(1)
        battle(player, skeleton)
    elif (chance.chance(30)):
        print("\nAn arrow whizzes past your head. A skeleton archer attacks you!")
        time.sleep(1)
        battle(player, skeleton_archer)
    if(gameOver):
        raise SystemExit
    elif(not gameOver):    
        choice = 7
        while(choice != "n" and choice != "nw"):
            choice = input("\nRoom: Dungeon\n\nWill you go (N)orth (W)est or (N)orth?").lower()
            if (choice == "nw"):
                cellar()
            elif (choice == "n"):
                skeleton_cave()
            elif (choice == "p"):
                usePotion()
            elif (choice == "lp"):
                useLifePotion()
            elif (choice == "fp"):
                useFullPotion()
            elif (choice == "help"):
                help()
            elif (choice == "save"):
                save_game()
            elif (choice == "load"):
                load_game()
            elif (choice == "look" and dungeon_counter == 0):
                print("You look around and find {} gold!".format(random_gold))
                player_gold += random_gold
                dungeon_counter += 1
            elif (choice == "look" and dungeon_counter > 0):
                print("You look around but find nothing.")
            elif (choice == "i"):
                view_inventory()
            else:
                print("\nPlease enter a valid input!")

def skeleton_cave():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global skeletonKing_death
    global skeletonCaveRoom_active
    global skeletonCave_counter
    global gameOver
    global active_room
    active_room = "skeleton cave"
    skeletonCaveRoom_active = True
    print("\nYou walk in and see a throne straight ahead on the opposite of the room. It is filled with the Skeleton King. Skeleton soldiers are lined facing the middle of the room. They notice you. There is a hatch to the South.")
    if(gameOver):
        raise SystemExit
    elif(not gameOver):
        if(skeletonKing_death):
            choice = 7
            while(choice != "s"):
                choice = input("\nRoom: Skeleton Cave\n\nWill you go (S)outh?").lower()
                if (choice == "s"):
                    dungeon()
                elif (choice == "p"):
                    usePotion()
                elif (choice == "lp"):
                    useLifePotion()
                elif (choice == "fp"):
                    useFullPotion()
                elif (choice == "help"):
                    help()
                elif (choice == "save"):
                    save_game()
                elif (choice == "load"):
                    load_game()
                elif(choice == "look" and skeletonCave_counter == 0):
                    print("\nYou look around and see some items on the ground.")
                    choice = 7
                    while(choice != "y" and choice != "n"):
                        choice = input("\n\tYou see a handcannon on the ground. Will you pick it up?(Y/N) ").lower()
                        if(choice == "y"):
                            print("\nYou pick up the handcannon.")
                            handcannon_inventory = True
                            skeletonCave_counter += 1
                        elif(choice == "n"):
                            print("\nYou do not pick up the handcannon.")
                    choice = 7
                    while(choice != "y" and choice != "n"):
                        choice = input("\n\tYou see some gold on the ground. Will you pick it up?(Y/N) ").lower()
                        if(choice == "y"):
                            print("\nYou pick up the 50 Gold!")
                            player_gold += 50
                            skeletonCave_counter += 1
                        elif(choice == "n"):
                            print("\nNot sure why but you do not pick up the gold!")
        elif(not skeletonKing_death):
            choice = 7
            while(choice != "s" and choice != "n"):
                choice = input("\nRoom: Skeleton Cave\n\nWill you go (S)outh or go (N)orth and face the Skeleton King?").lower()
                if (choice == "s"):
                    dungeon()
                elif (choice == "p"):
                    usePotion()
                elif (choice == "lp"):
                    useLifePotion()
                elif (choice == "fp"):
                    useFullPotion()
                elif (choice == "help"):
                    help()
                elif (choice == "save"):
                    save_game()
                elif (choice == "load"):
                    load_game()
                elif (choice == "n"):
                    print("\n\"So, you think you can face me?\" The Skeleton King says. \"Well first you must prove yourself a worthy opponent!\"")
                    time.sleep(4)
                    print("\n\"First you must defeat my minions!\" the Skeleton King says.")
                    time.sleep(3)
                    battle(player, skeleton)
                    print("\n\"That was my weakest minion adventurer! Let's see how you face against my archers!\"")
                    time.sleep(4)
                    battle(player, skeleton_archer)
                    print("\n\"They are still nothing compared to my next minions!")
                    time.sleep(3)
                    battle(player, skeleton_knight)
                    print("\n\"Adventurer, you have crossed a line. Let's see how you fare against me! The Skeleton King!!\"")
                    time.sleep(3)
                    battle(player, skeleton_king)
                    print("\n\"Ugh!\" The Skeleton King says. \"How are you so strong! I thought I could defeat you as I am the most powerful skeleton in all of the land. Alas, you have bested me. Here, take this book. You will need it on your adventure.\"The Skeleton King says as he lies on the ground and dies.")
                    time.sleep(3)
                    skeletonKing_death = True
                    book_inventory = True
                    dungeon()
                elif (choice == "i"):
                    view_inventory()
                else:
                    print("\nPlease enter a valid input!")

def cliffside():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global cliffside_counter
    global gameOver
    global active_room
    active_room = "cliffside"

    print("\nYou walk up to a cliffside. There is a sheer drop right in front of you. There is a small path leading to a valley in the West and a meadow to the South.")

    if (chance.chance(40)):
        print("\nA snake comes out and attacks you!")
        battle(player, snake)
    elif (chance.chance(50)):
        print("\nA bird flies down and attacks you!")
        battle(player, bird)
    if(gameOver):
        raise SystemExit
    elif(not gameOver):
        choice = 7
        while(choice != "w" and choice != "s"):
            choice = input("\nRoom: Cliffside\n\nWill you go (W)est or (S)outh?").lower()
            if (choice == "w"):
                dead_end_valley()
            elif (choice == "s"):
                meadow()
            elif (choice == "p"):
                usePotion()
            elif (choice == "lp"):
                useLifePotion()
            elif (choice == "fp"):
                useFullPotion()
            elif (choice == "help"):
                help()
            elif (choice == "save"):
                save_game()
            elif (choice == "load"):
                load_game()
            elif (choice == "look" and cliffside_counter == 0):
                print("You look around...")
                find_potion()
                cliffside_counter += 1
            elif (choice == "look" and cliffside_counter > 0):
                print("You look around but find nothing.")
            elif (choice == "i"):
                view_inventory()
            else:
                print("\nPlease enter a valid input!")

def dead_end_valley():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global flag5
    global deadEndValley_counter
    global gameOver
    global active_room
    active_room = "dead end valley"
    if(triforce_inventory and legendarySword_inventory):
        print("You enter a small valley. You see a sign reading \"Dead-End Valley\'. There is a path leading East. You notice something at the end of the valley.")
        choice = 7
        while (choice != "y" and choice != "n"):
            choice = input("Go to the end of the valley?").lower()
            if (choice == "y"):
                print("You walk to the end of the valley. \"This is it,\" you think, as you approach the cliff face.\"This is my destiny.\"")
                choice = 7
                while (choice != "y" and choice != "n"):
                    choice = input("Fufill your destiny?").lower()
                    if (choice == "y"):
                        print("You put the Legendary Sword through the hole in the Triforce, and enter it into a small hole on the cliff face. The cliff face slides apart and reveals a blue colored portal.")
                        choice = 7
                        while (choice != "y" and choice != "n"):
                            choice = input("Enter Shangri-La?").lower()
                            if (choice == "y"):
                                shangri_la()
                            elif (choice != "y" and choice != "n"):
                                print("Please enter a valid input!")
                            elif (choice == "n"):
                                choice = 7
                                while (choice != "y" and choice != "n"):
                                    choice = input("Are you sure you do not want to enter Shangri-La and fufill your destiny?").lower()
                                    if(choice == "y"):
                                        print("Okay, you can always come back later.")
                                        dead_end_valley()
                                    elif (choice == "n"):
                                        choice = 7
                                    else:
                                        print("Please enter a valid input!")
                                        while(choice != "y" and choice != "n"):
                                            choice = input("Enter Shangri-La?").lower()
                                            if(choice == "y"):
                                                choice = input("Save first?(Y/N) ").lower()
                                                if(choice == "y"):
                                                    save_game()
                                                    shangri_la()
                                                elif(choice == "n"):
                                                    shangri_la()
                                            else:
                                                dead_end_valley()

    elif(flag5):
        print("\nYou enter a small valley. You see a sign reading \"Dead-End Valley\". There is a path leading East. You see some gold on the ground.")
        choice = 7
        while(choice != "y" and choice != "n"):
            choice = input("\n\tDo you want to pick up the gold?").lower()
            if(choice == "y"):
                print("\nYou pick up the 15 Gold!")
                player_gold += 15
                flag5 = False
            elif(choice == "n"):
                print("\nNot sure why, but you do not pick up the gold!")
    else:
        print("\nYou enter a small valley. You see a sign reading \"Dead-End Valley\". There is a path leading East.")
    if (chance.chance(45)):
        print("\nA giant spider leaps out and attacks you!.")
        battle(player, giant_spider)
    if(gameOver):
        raise SystemExit
    elif(not gameOver):        
        choice = 7
        while(choice != "e"):
            choice = input("\nRoom: Dead-End Valley\n\nWill you go (E)ast?").lower()
            if (choice == "e"):
                cliffside()
            elif (choice == "p"):
                usePotion()
            elif (choice == "lp"):
                useLifePotion()
            elif (choice == "fp"):
                useFullPotion()
            elif (choice == "fp"):
                useFullPotion()
            elif (choice == "help"):
                help()
            elif (choice == "save"):
                save_game()
            elif (choice == "load"):
                load_game()
            elif (choice == "look" and deadEndValley_counter == 0):
                print("You look around...")
                find_potion()
                deadEndValley_counter += 1
            elif (choice == "look" and deadEndValley_counter > 0):
                print("You look around but find nothing.")
            elif (choice == "i"):
                view_inventory()
            else:
                print("Please enter a valid input!")

def forest():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global flag
    global forest_counter
    global gameOver
    global active_room
    active_room = "forest"
    if(flag):
        print("\nYou enter a dense forest. You hear a growling in the distance. You wander around and see a cave to the West. There is a meadow to the North. You see some gold on the ground!")
        choice = 7
        while(choice != "y" and choice != "n"):
            choice = input("\n\tWill you pick up the gold?").lower()
            if(choice == "y"):
                print("\nYou pick up the 15 Gold!")
                player_gold += 15
                flag = False
            elif(choice == "n"):
                print("\nNot sure why but you do not pick up the gold!")
    if(chance.chance(50)):
        print("\nA wolf lunges towards you and attacks you!")
        battle(player, wolf)
    elif(chance.chance(20)):
        print("\nA dire wolf sneaks up behind you and attacks you!")
        battle(player, dire_wolf)
    elif(chance.chance(50)):
        print("\nA spider crawls down a tree and attacks you!")
        battle(player, spider)
    if(gameOver):
        raise SystemExit
    elif(not gameOver):        
        choice = 7
        while(choice != "n" and choice != "w"):
            choice = input("\nRoom: Forest\n\nWill you go (N)orth or (W)est?").lower()
            if (choice == "n"):
                meadow()
            elif (choice == "w"):
                cave()
            elif (choice == "p"):
                usePotion()
            elif (choice == "lp"):
                useLifePotion()
            elif (choice == "fp"):
                useFullPotion()
            elif (choice == "help"):
                help()
            elif (choice == "save"):
                save_game()
            elif (choice == "load"):
                load_game()
            elif (choice == "look" and forest_counter == 0):
                print("You look around...")
                find_potion()
                forest_counter += 1
            elif(choice == "look" and forest_counter > 0):
                print("You look around but find nothing.")
            elif (choice == "i"):
                view_inventory()
            else:
                print("\nPlease enter a valid input!")

def cave():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global flag2
    global cave_counter
    global gameOver
    global active_room
    active_room = "cave"
    if(flag2 and not book_inventory):
        print("\nYou enter a large cave. You see spider webs in the corners. Bats fly over your head. Stagalimites cover the ceiling. There is the forest is to the East. You see some gold on the ground!")
        choice = 7
        while(choice != "y" and choice != "n"):
            choice = input("\n\tWill you pick up the gold?").lower()
            if(choice == "y"):
                print("\nYou pick up the 10 Gold!")
                player_gold += 10
                flag2 = False
            elif(choice == "n"):
                print("\nNot sure why but you do not pick up the gold!")
        if(chance.chance(50)):
            print("\nA spider leaps out and attacks you!")
            battle(player, spider)
        elif(chance.chance(40)):
            print("\nA snake slithers up and attacks you!")
            battle(player, snake)
        elif(chance.chance(49)):
            print("\nA rat scurries up and attacks you!")
            battle(player, rat)
        if(gameOver):
            raise SystemExit
        elif(not gameOver):            
            choice = 7
            while(choice != "e"):
                choice = input("\nRoom: Cave\n\nWill you go(E)ast?").lower()
                if (choice == "e"):
                    forest()
                elif (choice == "p"):
                    usePotion()
                elif (choice == "lp"):
                    useLifePotion()
                elif (choice == "fp"):
                    useFullPotion()
                elif (choice == "help"):
                    help()
                elif (choice == "save"):
                    save_game()
                elif (choice == "load"):
                    load_game()
                elif (choice == "look" and cave_counter == 0):
                    print("You look around and find {} gold!".format(random_gold))
                    player_gold += random_gold
                    cave_counter += 1
                elif (choice == "look" and cave_counter > 0):
                    print("You look around but find nothing.")
                elif (choice == "i"):
                    view_inventory()
                else:
                    print("\nPlease enter a valid input!")
    if(flag2 and book_inventory):
        print("\nYou enter a large cave. You see spider webs in the corners. Bats fly over your head. Stagalimites cover the ceiling. There is the forest is to the East and the secret passage is to the South, You see some gold on the ground!")
        choice = 7
        while(choice != "y" and choice != "n"):
            choice = input("\n\tWill you pick up the gold?").lower()
            if(choice == "y"):
                print("\nYou pick up the 10 Gold!")
                player_gold += 10
                flag2 = False
            elif(choice == "n"):
                print("\nNot sure why but you do not pick up the gold!")
        if(chance.chance(50)):
            print("\nA spider leaps out and attacks you!")
            battle(player, spider)
        elif(chance.chance(40)):
            print("\nA snake slithers up and attacks you!")
            battle(player, snake)
        elif(chance.chance(49)):
            print("\nA rat scurries up and attacks you!")
            battle(player, rat)
        if(gameOver):
            raise SystemExit
        elif(not gameOver):            
            choice = 7
            while(choice != "s" and choice != "e"):
                choice = input("\nRoom: Cave\n\nWill you go(S)outh or (E)ast?").lower()
                if (choice == "s"):
                    secret_passage()
                elif (choice == "e"):
                    forest()
                elif (choice == "p"):
                    usePotion()
                elif (choice == "lp"):
                    useLifePotion()
                elif (choice == "fp"):
                    useFullPotion()
                elif (choice == "help"):
                    help()
                elif (choice == "save"):
                    save_game()
                elif (choice == "load"):
                    load_game()
                elif (choice == "i"):
                    view_inventory()
                else:
                    print("\nPlease enter a valid input!")

        elif(not flag2 and not book_inventory):
            print("\nYou enter a large cave. You see spider webs in the corners. Bats fly over your head. Stagalimites cover the ceiling. There is the forest is to the East.")
            if(gameOver):
                raise SystemExit
            elif(not gameOver):            
                choice = 7
                while(choice != "e"):
                    choice = input("\Room: Cave\n\nWill you go(E)ast?").lower()
                    if (choice == "e"):
                        forest()
                    elif (choice == "p"):
                        usePotion()
                    elif (choice == "lp"):
                        useLifePotion()
                    elif (choice == "fp"):
                        useFullPotion()
                    elif (choice == "help"):
                        help()
                    elif (choice == "save"):
                        save_game()
                    elif (choice == "load"):
                        load_game()
                    elif (choice == "i"):
                        view_inventory()
                    else:
                        print("\nPlease enter a valid input!")
def secret_passage():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global secretPassage_counter
    global gameOver
    global active_room
    active_room = "secret passage"
    if(book_inventory):
        print("\nYou crawl into a small tunnel. It is big enough to turn around in. There is a cave to the North and you see a light in the South.")
    else:
        print("\nYou do not see anything here.")
        cave()
    if(gameOver):
        raise SystemExit
    elif(not gameOver):        
        choice = 7
        while(choice != "n" and choice != "s"):
            choice = input("\nRoom: Secret Passage\n\nWill you go (N)orth or (S)outh?").lower()
            if (choice == "n"):
                cave()
            elif (choice == "s"):
                dragons_lair()
            elif (choice == "p"):
                usePotion()
            elif (choice == "lp"):
                useLifePotion()
            elif (choice == "fp"):
                useFullPotion()
            elif (choice == "help"):
                help()
            elif (choice == "save"):
                save_game()
            elif (choice == "load"):
                load_game()
            elif (choice == "look" and secretPassage_counter == 0):
                print("You look around and find {} gold!".format(random_gold))
                player_gold += random_gold
                secretPassage_counter += 1
            elif (choice == "look" and secretPassage_counter > 0):
                print("You look around but find nothing.")
            elif (choice == "i"):
                view_inventory()
            else:
                print("\nPlease enter a valid input!")

def dragons_lair():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global dragon_death
    global dragonsLair_counter
    global gameOver
    global active_room
    active_room = "dragons lair"
    if(not dragon_death):
        print("\nYou exit the secret passage and enter a very large room. You are very deep underground as you cannot see the top of the ceiling but see a light very far up. You look across the huge room and see a dragon sleeping on his treasure. The secret passage to the North is the only logical way out.")
        if(gameOver):
            raise SystemExit
        elif(not gameOver):    
            choice = 7
            while(choice != "n" and choice != "s"):
                choice = input("\nRoom: Dragon's Lair\n\n\tWill you go (N)orth or go (S)outh and fight the dragon to claim his treasure?").lower()
                if (choice == "n"):
                    secret_passage()
                elif(choice == "p"):
                    usePotion()
                elif (choice == "lp"):
                    useLifePotion()
                elif (choice == "fp"):
                    useFullPotion()
                elif (choice == "help"):
                    help()
                elif (choice == "save"):
                    save_game()
                elif (choice == "load"):
                    load_game()
                elif (choice == "s"):
                    print("\nYou sneak up to the dragon, thinking it has not taken notice of you. However, it has known you were there the whole time!")
                    time.sleep(3)
                    print("\nThe dragon wakes up and lunges at you. \"Vir krilon hi vopraan zey nol dii slumber! Rodraan wah dir bovitaan!\" He says in his own language, Dova. (This translated is \"How dare you wake me from my slumber! Prepare to die adventurer!\"")
                    time.sleep(7)
                    battle(player, dragon)
                    print("\nThe dragon falls down. \"You have bested me adventurer. Please, take what you want, I won't bother you anymore. Of interest to you is probably this Great Oak Key, 150 Gold and this Krambit. Take them, they are yours for defeating me.\"")
                    time.sleep(10)
                    krambit_inventory = True
                    greatOakKey_inventory = True
                    player_gold += 150
                    dragons_lair()
                elif (choice == "i"):
                    view_inventory()
                else:
                    print("\nPlease enter a valid input!")
    elif(dragon_death):
        print("\nYou exit the secret passage and enter a very large room. You are very deep underground as you cannot see the top of the ceiling but see a light very far up. The secret passage to the North is the only logical way out.")
        if(chance.chance(50)):
            print("\nA snake slithers up and attacks you!")
            time.sleep(2)
            battle(player, snake)
        if(gameOver):
            raise SystemExit
        elif(not gameOver):    
            choice = 7
            while(choice != "n"):
                choice = input("\nRoom: Dragon's Lair\n\nWill you go (N)orth?").lower()
                if (choice == "n"):
                    secret_passage()
                elif (choice == "i"):
                    view_inventory()
                elif (choice == "p"):
                    usePotion()
                elif (choice == "lp"):
                    useLifePotion()
                elif (choice == "fp"):
                    useFullPotion()
                elif (choice == "help"):
                    help()
                elif (choice == "save"):
                    save_game()
                elif (choice == "load"):
                    load_game()
                elif (choice == "look" and dragonsLair_counter == 0):
                    print("\nYou find 35 gold on the ground!")
                    player_gold += 35
                    dragonsLair_counter += 1
                elif (choice == "look" and dragonsLair_counter > 0):
                    print("You look around but find nothing.")
                else:
                    print("\nPlease enter a valid input!")

def village():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global counter
    global village_counter
    global gameOver
    global active_room
    active_room = "village"
    if(counter == 0):
        print("\nYou enter a small village. The people seem friendly, and all say \"hello\" to you, regardless of you being a stranger. You see a cemetary to the South, a church to the South East, the marketplace is to the East and the meadow to the West. You see some gold on the ground.")
        choice = 7
        while(choice != "y" and choice != "n"):
            choice = input("\n\tWill you pick up the gold?").lower()
            if(choice == "y"):
                print("You pick up the 10 Gold!")
                player_gold += 10
                counter += 1
            elif(choice == "n"):
                print("Not sure why, but you do not pick up the gold!")
            else:
                print("Please enter a valid input!")
    elif(counter >= 1):
        print("\nYou enter a small village. The people seem friendly, and all say \"hello\" to you, regardless of you being a stranger. You see a cemetary to the South, a church to the South East, the marketplace is to the East and the meadow to the West.")
    if(gameOver):
        raise SystemExit
    elif(not gameOver):    
        choice = 7
        while(choice != "s" and choice != "se" and choice != "s" and choice != "w"):
            choice = input("\nRoom: Village\n\nWill you go (S)outh, (S)outh (E)ast, (E)ast or (W)est?").lower()
            if (choice == "s"):
                cemetary()
            elif (choice == "se"):
                church()
            elif (choice == "e"):
                marketplace()
            elif (choice == "w"):
                meadow()
            elif (choice == "p"):
                usePotion()
            elif (choice == "lp"):
                useLifePotion()
            elif (choice == "fp"):
                useFullPotion()
            elif (choice == "look" and village_counter == 0):
                print("You look around...")
                find_potion()
                village_counter += 1
            elif (choice == "look" and village_counter > 0):
                print("You look around but find nothing")
            elif (choice == "help"):
                help()
            elif (choice == "save"):
                save_game()
            elif (choice == "load"):
                load_game()
            elif (choice == "i"):
                view_inventory()
            else:
                print("\nPlease enter a valid input!")

def church():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global flag4
    global church_counter
    global gameOver
    global active_room
    active_room = "church"
    if(not note_inventory):
        print("\nYou enter the church. Pews are lined facing the front of the church, where Father Henry is motioning for you to come to him. \"Hello, my son.\" Father Henry says, \"Your father left a note with me to give to you. It is very important that you have it so, here.\"")
        note_inventory = True
    elif(note_inventory and flag4):
        print("\nYou enter the church. Pews are lined facing the front of the church, where Father Henry nods a welcome to you. The village is to the North. You see some gold on the floor.")
        choice = 7
        while(choice != "y" and choice != "n"):
            choice = input("\n\tDo you want to pick up the gold?").lower()
            if(choice == "y"):
                print("\nYou pick up the 50 Gold!")
                player_gold += 50
                flag4 = False
            elif(choice == "n"):
                print("\nNot sure why, but you do not pick up the gold!")
    if(chance.chance(40)):
        print("\nA spider comes out and attacks you!")
        battle(player, spider)
    elif(chance.chance(50)):
        print("\nA rat scurries across the floor and attacks you!")
        battle(player, rat)
    if(gameOver):
        raise SystemExit
    elif(not gameOver):        
        choice = 7
        while(choice != "n"):
            choice = input("\nRoom: Church\n\nWill you go (N)orth?").lower()
            if (choice == "n"):
                village()
            elif (choice == "p"):
                usePotion()
            elif (choice == "lp"):
                useLifePotion()
            elif (choice == "fp"):
                useFullPotion()
            elif (choice == "help"):
                help()
            elif (choice == "save"):
                save_game()
            elif (choice == "load"):
                load_game()
            elif (choice == "look" and church_counter == 0):
                print("You find {} Gold!".format(random_gold))
                church_counter += 1
            elif (choice == "look" and church_counter > 0):
                print("You look around but find nothing")
            elif (choice == "i"):
                view_inventory()
            else:
                print("\nPlease enter a valid input!")

def cemetary():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global cemetary_counter
    global gameOver
    global active_room
    active_room = "cemetary"
    if(torch_inventory):
        print("\nYou open a black iron fence gate and walk into the cemetary. You see various different kinds of headstones with various markings on them, from \"RIP\" to loving quotes, and even one that says \"Here lie the party guy\". The village is to the North.")
    elif(not torch_inventory):
        print("\nYou open a black iron fence gate and walk into the cemetary. You see various different kinds of headstones with various markings on them, from \"RIP\" to loving quotes, and even one that says \"Here lie the party guy\". You see a torch on the ground.")
        choice = 7
        while (choice != "y" and choice != "n"):
            choice = input("\nDo you want to pick up the torch?")
            if (choice == "y"):
                print("\nYou pick up the torch.")
                torch_inventory = True
            elif (choice == "n"):
                print("\nYou do not pick up the torch.")
            else:
                print("\nPlease enter a valid input!")
    if (chance.chance(40)):
        print("\nA zombie comes up behind you and attacks you!")
        battle(player, zombie)
    elif (chance.chance(30)):
        print("\nA skeleton leaps in front of you and attacks you!")
        battle(player, skeleton)
    elif (chance.chance(10)):
        print("\nYou hear shuffling behind you. You turn around and see a villager sneaking up behind you! He attacks!")
        battle(player, crazed_villager)
    if(gameOver):
        raise SystemExit
    elif(not gameOver):
        choice = 7
        while(choice != "n"):
            choice = input("\nRoom: Cemetary\n\nWill you go (N)orth?").lower()
            if (choice == "n"):
                village()
            elif (choice == "p"):
                usePotion()
            elif (choice == "lp"):
                useLifePotion()
            elif (choice == "fp"):
                useFullPotion()
            elif (choice == "help"):
                help()
            elif (choice == "save"):
                save_game()
            elif (choice == "load"):
                load_game()
            elif (choice == "look" and cemetary_counter == 0):
                print("You find {} Gold!".format(random_gold))
                cemetary_counter += 1
            elif (choice == "look" and cemetary_counter > 0):
                print("You look around but find nothing")
            elif (choice == "i"):
                view_inventory()
            else:
                print("\nPlease enter a valid input!")

def marketplace():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global flag3
    global market_counter
    global gameOver
    global active_room
    active_room = "marketplace"
    if(flag3):
        print("\nYou walk into the marketplace, which is alive and buzzing with energy. You see many different stands, but the only ones of interest to you are the Blacksmith to the North, the shop to the East and a huge castle to the South. You see some gold on the ground.")
        choice = 7
        while(choice != "y" and choice != "n"):
            choice = input("\n\tDo you want to pick up the gold?").lower()
            if(choice == "y"):
                print("\nYou pick up the 20 Gold!")
                player_gold += 20
                flag3 = False
            elif (choice == "n"):
                print("\nNot sure why, but you do not pick up the gold!")
            else:
                print("\nPlease choose a valid option!")
    else:
        print("\nYou walk into the marketplace, which is alive and buzzing with energy. You see many different stands, but the only ones of interest to you are the Blacksmith to the North, the shop to the East and a huge castle to the South.")
    if(chance.chance(50)):
        print("\nA rat comes up and attacks you!")
        time.sleep(2)
        battle(player, rat)
    choice = 7
    while(choice != "n" and choice != "e" and choice != "s" and choice != "w"):
        choice = input("\nRoom: Marketplace\n\nWill you go (N)orth, (E)ast, (W)est or (S)outh?").lower()
        if (choice == "n"):
            blacksmith()
        elif (choice == "e"):
            shop()
        elif (choice == "s"):
            castle()
        elif (choice == "w"):
            village()
        elif (choice == "p"):
            usePotion()
        elif (choice == "lp"):
            useLifePotion()
        elif (choice == "fp"):
            useFullPotion()
        elif (choice == "help"):
            help()
        elif (choice == "save"):
            save_game()
        elif (choice == "load"):
            load_game()
        elif (choice == "look" and market_counter == 0):
            print("You look around...")
            find_potion()
            market_counter += 1
        elif (choice == "look" and market_counter > 0):
            print("You look around but find nothing")
        elif (choice == "i"):
            view_inventory()
        else:
            print("\nPlease enter a valid input!")

def blacksmith():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global active_room
    active_room = "blacksmith"
    print("\nYou walk into the blacksmith. Literally. He puts down what he is doing and asks what you want. You can buy and sell weapons. The marketplace is to the South.")

    choice = 7
    while(choice != "s" and choice != "b"):
        choice = input("\nRoom: Blacksmith\n\nWill you (B)uy something or leave and go (S)outh?").lower()
        if (choice == "s"):
            marketplace()
        elif (choice == "b"): #To buy stuff
            b_buy()
        elif (choice == "p"):
            usePotion()
        elif (choice == "lp"):
            useLifePotion()
        elif (choice == "fp"):
            useFullPotion()
        elif (choice == "help"):
            help()
        elif (choice == "save"):
            save_game()
        elif (choice == "load"):
            load_game()
        elif (choice == "look"):
            print("You look around but find nothing")
        elif (choice == "i"):
            view_inventory()
        else:
            print("\nPlease enter a valid input!")

def shop():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global potion_inventory
    global lifePotion_inventory
    global active_room
    active_room = "shop"
    print("\nYou enter the shop. The storekeeper warmly welcomes you. You look around and see items lining the shelves. There are other shoppers in here, buying various items. The shopkeeper asks if you will buy anything or are willing to sell some stuff. The marketplace is to the South.")

    choice = 7
    while(choice != "s" and choice != "b" and choice != "p" and choice != "lp"):
        choice = input("\nRoom: Shop\n\nWill you (B)uy something or leave and go (S)outh?").lower()
        if (choice == "s"):
            marketplace()
        elif (choice == "b"): #To buy stuff
            s_buy()
        elif (choice == "i"):
            view_inventory()
        elif (choice == "p"):
            usePotion()
        elif (choice == "lp"):
            useLifePotion()
        elif (choice == "fp"):
            useFullPotion()
        elif (choice == "save"):
            save_game()
        elif (choice == "load"):
            load_game()
        elif (choice == "look"):
            print("You look around but find nothing")        
        elif (choice == "help"):
            help()
        else:
            print("\nPlease enter a valid input!")

def castle():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global random_gold
    global castle_counter
    global active_room
    active_room = "castle"
    if(jewelEgg_inventory):
        print("\nYou enter a grand castle. You walk in and people start bowing. You had forgotten you were king! Someone walks up to you and asks if you had found an egg special to their family. You pull out the Jewel Egg you found at the Great Oak. \"Thats it!\" the person says as you hand it over. \"Here!\" they say, \"Take this sword my grandfather gave me, I have no use for it as it cannot be sharpened.\"")
        legendarySword_inventory = True
        jewelEgg_inventory = False
    elif(not jewelEgg_inventory):
        print("\nYou enter a grand castle. You walk in and people start bowing. You had forgotten that you were king! Someone walks up to you and says you need to take care of some business before you can retake the throne. The marketplace is to the North.")

    choice = 7
    while(choice != "n" and choice != "q"):
        choice = input("\nRoom: Castle\n\nWould you like to leave and go (N)orth?").lower()
        if (choice == "n"):
            marketplace()
        elif (choice == "p"):
            usePotion()
        elif (choice == "lp"):
            useLifePotion()
        elif (choice == "fp"):
            useFullPotion()
        elif (choice == "help"):
            help()
        elif (choice == "save"):
            save_game()
        elif (choice == "load"):
            load_game()
        elif (choice == "look" and castle_counter == 0):
            print("You look around...")
            find_potion()
            castle_counter += 1
        elif (choice == "look" and castle_counter > 0):
            print("You look around but find nothing")
        elif (choice == "i"):
            view_inventory()
        else:
            print("\nPlease enter a valid input!")

def shangri_la():
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global gameOver
    global active_room
    active_room = "shangri-la"
    print("\n\n\n\t\tYou have entered Shangri-La...")
    print("\nYou walk through and see an amazing view. You are standing at the start of a long winding path lined with beautiful cherry blossom trees.")
    time.sleep(3)
    print("\nYou hear birds chirping as you walk down the path...")
    time.sleep(3)
    print("\nYou see a temple at the end of the path. You walk towards it...")
    time.sleep(3)
    print("\nYou walk up the front steps of the temple and see a very large door, at least 30 feet tall and 20 feet wide.")
    time.sleep(3)
    print("\nYou walk up to the door and before you can knock, the large doors slowly swing open before you.")
    time.sleep(3)
    print("\nYou walk in with your" + " " + str(best_weapon.name), "drawn. You walk down ornately decorated halls, some lined with ceremonial armor with intricate designs on armor stands, others with weapon cases. Some even have trophies of animals on the walls.")
    time.sleep(7)
    print("\nYou walk into the heart of the temple and see three figures sitting in 3 thrones. The one closest to you stands up. \"Son, this is your destiny. Behind us is a door where your destiny lays. But, as tradition calls for, you must defeat us before you can have access.\"")
    time.sleep(10)
    print("\n\"Father?\" You say, stunned. \"That is right,\" Dragox says. \"I am your father, and I am prepared to keep you from your destiny, just like my father did! It is tradition. Only the best warriors fufill their destiny! Lets see if you have what it takes!\"")
    input("\n\nThis is the endgame! Beat Dragox, Romox and your evil uncle Fencor to fufill your destiny! Press Enter! ")
    active_room = "dragox battle"
    def dragox_battle():
        battle(player, dragox)
        print("\n\"Good. Good! You are stronger than we thought. But I am a mere weakling compared to my father! He is your next opponent! Take my sword, as you have earned it!\"")
        dSword_inventory = True
        time.sleep(5)
        if(not gameOver):
            active_room = "romox battle"
            choice = input("\nSave your game?(Y/N) ").lower()
            if(choice == "y"):
                save_game()
        elif(gameOver):
            raise SystemExit
    def romox_battle():
        battle(player, romox)
        print("\"Very good. Very good! Keep going! You now must defeat Fencor, your uncle! Take my Scepter, it is your only chance against the Great Fencor!\"")
        scepter_inventory = True
        time.sleep(5)
        if(not gameOver):
            active_room = "fencor battle"
            choice = input("\nSave your game?(Y/N) ").lower()
            if(choice == "y"):
                save_game()   
        elif(gameOver):
            raise SystemExit
    def fencor_battle():
        battle(player, fencor)
        if(not gameOver):
            print("\n\"You have bested me nephew.\" Fencor says. \"Take my Umari, as a gift of things to come...\"")
            time.sleep(3)
            print("\n\"So, it is true...\" Dragox says. \"You are the person the legend talks of.\" \"What legend?\" You say.")
            time.sleep(3)
            print("\n\"Legend speaks of a great warrior. I had a feeling it was you. This great warrior was born from a line of great warriors. The greatest warriors are always kings! Notice how our bloodline is all kings?\" Dragox says.")
            time.sleep(10)
            print("\n\"What your father says is true.\" Romox says. \"Our whole bloodline is filled with legendary warriors and iron hearted rulers. We knew that this great warrior would come from our bloodline, we just never knew when, or who!\"")
            time.sleep(7)
            print("\n\"You must fufill your destiny. Walk past us and into the portal. It will take you to a new land, where you must continue to forge ahead to fufill your destiny.\" Fencor says.")
            time.sleep(7)
            print("\nYou walk past the three thrones and up to the portal. You turn around to look at your family. \"Will I see any of you again?\" You ask. \"No, you will not\" Romox replies, \"As we are just an image, a physical being of the past, in our future.\" You look back at the portal, sigh, stand up straight, and walk through...")
            time.sleep(12)
            game_end()
        elif(gameOver):
            raise SystemExit
            
def b_buy(): #To buy weapons from the blacksmith
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    for key in blacksmith_buy:
        if (blacksmith_buy[key]):
            print(key)
    choice = 7
    while(choice != "back"):
        choice = str(input("\nWhat would you like to buy?(Type the name of the object or \"back\" to exit): ")).lower()
        if (choice == "sword"):
            if (player_gold < 15):
                print("\nYou do not have enough gold to buy that item!")
            elif (player_gold >= 15):
                print("\nYou buy the sword for 15 gold!")
                sword_inventory = True
                player_gold -= 15
            else:
                print("\nPlease enter a valid option")
        if (choice == "heavy sword"):
            if (player_gold < 50):
                print("\nYou do not have enough gold to buy that item!")
            elif (player_gold >= 50):
                print("\nYou buy the Heavy Sword for 50 gold!")
                heavySword_inventory = True
                player_gold -= 50
            else:
                print("\nPlease enter a valid option")
        if (choice == "bow"):
                    if (player_gold < 20):
                        print("\nYou do not have enough gold to buy that item!")
                    elif (player_gold >= 20):
                        print("\nYou buy the Bow for 20 gold!")
                        bow_inventory = True
                        player_gold -= 20
                    else:
                        print("\nPlease enter a valid option")
        if (choice == "crossbow"):
            if(player_gold < 35):
                print("\nYou do not have enough gold to buy that item!")
            elif(player_gold >= 35):
                print("\nYou buy the crossbow for 35 gold!")
                crossbow_inventory = True
                player_gold -= 35
            else:
                print("\nPlease enter a valid option")
        if (choice == "back"):
            blacksmith()
        if (choice == "help"):
            help()
        if (choice == "i"):
            view_inventory()
def s_buy(): #To buy items from the shop
    global player_gold
    global potion_inventory
    global lifePotion_inventory
    global torch_inventory
    global fullPotion_inventory
    for key in shop_buy:
        if (shop_buy[key]):
            print(key)
    choice = 7
    while(choice != "back"):
        choice = str(input("\nWhat would you like to buy?(Type the name of the object or \"back\" to exit): ")).lower()
        if (choice == "i"):
            view_inventory()
        if (choice == "potion"):
            if (player_gold < 20):
                print("\nYou do not have enough gold to buy that item!")
            elif (player_gold >= 20):
                print("\nYou buy the potion for 15 gold!")
                potion_inventory += 1
                player_gold -= 20
            else:
                print("\nPlease enter a valid option")
        if (choice == "life potion"):
            if (player_gold < 100):
                print("\nYou do not have enough gold to buy that item!")
            elif (player_gold >= 100):
                print("\nYou buy the Life Potion for 100 gold!")
                lifePotion_inventory += 1
                player_gold -= 100
            else:
                print("\nPlease enter a valid option")
        if (choice == "torch"):
            if (player_gold < 5):
                print("\nYou do not have enough gold to buy that item!")
            elif (player_gold >= 5):
                print("\nYou buy the Torch for 5 gold!")
                torch_inventory = True
                player_gold -= 5
            else:
                print("\nPlease enter a valid option")
        if (choice == "full potion"):
            if (player_gold < 40):
                print("\nYou do not have enough gold to buy that item!")
            elif (player_gold >= 40):
                print("\nYou buy the Full Potion for 40 Gold!")
                fullPotion_inventory += 1
                player_gold -= 40
            else:
                print("\nPlease enter a valid option")
        if (choice == "back"):
            shop()
        if (choice == "help"):
            help()

def battle(player, enemy): #Battle function
    global best_weapon
    global gameOver
    global potion_inventory
    global lifePotion_inventory
    global fullPotion_inventory
    global player_gold
    global random_gold
    flag = True
    damage = 0
    enemy.hp = enemy.max_hp
    """Checks the inventory for the best weapon and applies that to the variable best_weapon"""
    if(umari_inventory):
        best_weapon = fencor_umari
    elif(scepter_inventory):
        best_weapon = romox_scepter
    elif(dSword_inventory):
        best_weapon = dragox_sword
    elif(krambit_inventory):
        best_weapon = krambit
    elif(handcannon_inventory):
        best_weapon = handcannon
    elif(crossbow_inventory):
        best_weapon = crossbow
    elif(bow_inventory):
        best_weapon = bow
    elif(heavySword_inventory):
        best_weapon = heavy_sword
    elif(sword_inventory):
        best_weapon = sword
    elif(dagger_inventory):
        best_weapon = dagger
    elif(rock_inventory):
        best_weapon = rock
    else:
        print("\n\tYou do not have a weapon. You do not know how to fist fight so {} attacks you and kills you. Game over!".format(enemy.name))
        death()
    max_dmg = best_weapon.damage + int(best_weapon.damage)*2 #Specify how much damage a critical hit is

    if (enemy.name != "Skeleton King" or enemy.name != "Dragox" or enemy.name != "Romox" or enemy.name != "Dragon" or enemy.name != "Fencor" or not skeletonCaveRoom_active): #Allows fleeing if the enemy is not a boss and the Player is not in the Skeleton Cave Boss Battle
        while(flag):
            if(potion_inventory or lifePotion_inventory or fullPotion_inventory):
                choice = 7
                while (choice != "a" and choice != "f" and player.is_alive):
                    choice = input("\n\nDo you want to (A)ttack, use a (P)otion or (F)lee?(Enemy Hp: {})(Player HP: {}) ".format(enemy.hp, player.hp)).lower()
                    if (choice == "i"):
                        view_inventory()
                    if (choice == "a"):
                        if (chance.chance(50)): #Adds the chance to do a critical hit
                            damage = max_dmg
                        else: #Otherwise do regular damage
                            damage = best_weapon.damage
                        print("\nYou do {} damage with {} against {}!".format(damage, best_weapon.name, enemy.name))
                        if(not enemy.hp - damage < 0):
                            enemy.hp -= damage
                            print("\n{} HP is {}.".format(enemy.name, enemy.hp))
                            time.sleep(2)
                        elif((enemy.hp - damage) <= 0):
                            enemy.hp -= damage
                            print("\n{} Hp is 0.".format(enemy.name))
                            time.sleep(2)
                        if (not enemy.is_alive()): #Check to see if enemy is alive
                            if(not player.xp_to_level == 0 and not (player.xp_to_level - enemy.xp) <= 0): #If the amount of xp needed to level up is not 0 and the amount of xp needed to level up - the amount of xp the enemy gives...
                                player.xp_to_level -= enemy.xp #Subtract enemy xp worth from the amount of xp needed to level up
                                player.xp += enemy.xp #Add enemy xp worth to amount of xp
                                print("\nYou gained {} xp! You have {} xp left to level up!".format(enemy.xp, player.xp_to_level))
                                if(chance.chance(50)):
                                    print("{} dropped {} Gold!".format(enemy.name, int(random_gold) * 2))
                                    player_gold += random_gold
                                else:
                                    print("{} dropped {} Gold!".format(enemy.name, random_gold))
                                    player_gold += random_gold
                                flag = False
                            elif (player.xp_to_level <= 0 or (player.xp_to_level - enemy.xp) < 0): #Check if the player has enough xp to level up
                                print("\nYou gained {} xp!".format(enemy.xp))
                                player.levelUp() #Call the level up function
                                if(chance.chance(50)):
                                    print("{} dropped {} Gold!".format(enemy.name, int(random_gold) * 2))
                                else:
                                    print("{} dropped {} Gold!".format(enemy.name, random_gold))
                                flag = False
                        elif (enemy.is_alive()): #If the enemy is still alive
                            if(player.hp <= enemy.damage or player.hp - enemy.damage <= 0):
                                player.hp -= enemy.damage
                                print("{} hits you for {} damage! You fall to the ground.".format(enemy.name, enemy.damage))
                                flag = False
                                gameOver = True
                                death()
                            if(not player.hp <= 0):
                                player.hp -= enemy.damage #Enemy attacks (the amount of damage the enemy does is subtracted from the amount of hp the player has
                                print("\n{} hits you for {} damage! You have {} hp left!".format(enemy.name, enemy.damage, player.hp))


                    elif (choice == "f"):
                        print("\nYou attempt to flee like the coward you are.")
                        if(chance.chance(50)):
                            print("\nYou successfully flee from the battle against {}.".format(enemy.name))
                            time.sleep(2)
                            flag = False
                        else:
                            print("\nYour lame attempt to run from {} does not work. You trip over nothing and get eaten by {}!".format(enemy.name, enemy.name))
                            time.sleep(2)
                            flag = False
                            gameOver = True
                            death() #Calls the death function
                    elif (choice == "p"): #Below are all of the possible combinations of the potions you can have at any given point
                        if(potion_inventory >= 1 and fullPotion_inventory >= 1 and lifePotion_inventory >= 1):
                            choice = 7
                            while(choice != "p" and choice != "fp" and choice != "lp" and choice != "back"):
                                choice = input("Will you use a (P)otion, a (F)ull (P)otion or a (L)ife (P)otion? Type \"back\" to go back").lower()
                                if(choice == "p"):
                                    usePotion()
                                elif(choice == "fp"):
                                    useFullPotion()
                                elif(choice == "lp"):
                                    useLifePotion()
                                elif(choice == "back"):
                                    pass
                                else:
                                    print("Please enter a valid input!")
                        elif(potion_inventory == 0 and fullPotion_inventory >= 1 and lifePotion_inventory >= 1):
                            choice = 7
                            while(choice != "fp" and choice != "back" and choice != "lp"):
                                choice = input("Will you use a (F)ull (P)otion or a (L)ife (P)otion? Type \"back\" to go back").lower()
                                if(choice == "fp"):
                                    useFullPotion()
                                elif(choice == "lp"):
                                    useLifePotion()
                                elif(choice == "back"):
                                    pass
                                else:
                                    print("Please enter a valid input!")
                        elif(potion_inventory >= 1 and fullPotion_inventory == 0 and fullPotion_inventory >= 1):
                            choice = 7
                            while(choice != "p" and choice != "lp" and choice != "back"):
                                choice = input("Will you use a (P)otion or a (F)ull (P)otion? Type \"back\" to go back").lower()
                                if(choice == "p"):
                                    usePotion()
                                elif(choice == "lp"):
                                    useLifePotion()
                                elif(choice == "back"):
                                    pass
                                else:
                                    print("Please choose a valid input!")
                        elif(potion_inventory == 0 and fullPotion_inventory == 0 and fullPotion_inventory >= 1):
                            choice = 7
                            while(choice != "lp" and choice != "back"):
                                choice = input("Will you use a (L)ife (P)otion? Type \"back\" to go back").lower()
                                if(choice == "lp"):
                                    useLifePotion()
                                elif(choice == "back"):
                                    pass
                                else:
                                    print("Please choose a valid input!")
                        elif(potion_inventory >= 1 and fullPotion_inventory == 0 and fullPotion_inventory == 0):
                            choice = 7
                            while(choice != "p" and choice != "back"):
                                choice = input("Will you use a (P)otion? Type \"back\" to go back").lower()
                                if(choice == "p"):
                                    usePotion()
                                elif(choice == "back"):
                                    pass
                                else:
                                    print("Please choose a valid input!")
                        elif(potion_inventory >= 1 and fullPotion_inventory >= 1 and fullPotion_inventory == 0):
                            choice = 7
                            while(choice != "p" and choice != "fp" and choice != "back"):
                                choice = input("Will you use a (P)otion or a (F)ull (P)otion? Type \"back\" to go back").lower()
                                if(choice == "p"):
                                    usePotion()
                                elif(choice == "fp"):
                                    useFullPotion()
                                elif(choice == "back"):
                                    pass
                                else:
                                    print("Please choose a valid input!")
                        elif(potion_inventory == 0 and fullPotion_inventory >= 1 and fullPotion_inventory == 0):
                            choice = 7
                            while(choice != "fp" and choice != "back"):
                                choice = input("Will you use a (F)ull (P)otion? Type \"back\" to go back").lower()
                                if(choice == "fp"):
                                    useFullPotion()
                                elif(choice == "back"):
                                    pass
                                else:
                                    print("Please choose a valid input!")                    
                        
                        elif(potion_inventory == 0 and fullPotion_inventory == 0 and lifePotion_inventory == 0):
                            print("You do not have any Potions!")
                            
            elif(not potion_inventory and not lifePotion_inventory and not fullPotion_inventory):
                choice = 7
                while (choice != "a" and choice != "f" and player.is_alive):
                    choice = input("\n\nDo you want to (A)ttack or (F)lee?(Enemy Hp: {})(Player HP: {}) ".format(enemy.hp, player.hp)).lower()
                    if (choice == "i"):
                        view_inventory()
                    if (choice == "a"):
                        if (chance.chance(50)): #Adds the chance to do a critical hit
                            damage = max_dmg
                        else: #Otherwise do regular damage
                            damage = best_weapon.damage
                        print("\nYou do {} damage with {} against {}!".format(damage, best_weapon.name, enemy.name))
                        if(not(enemy.hp - damage) < 0):
                            enemy.hp -= damage
                            print("\n{} HP is {}.".format(enemy.name, enemy.hp))
                            time.sleep(2)
                        elif((enemy.hp - damage) <= 0):
                            enemy.hp -= damage
                            print("\n{} Hp is 0.".format(enemy.name))
                            time.sleep(2)
                        if (not enemy.is_alive()): #Check to see if enemy is alive
                            if(not player.xp_to_level == 0 and not (player.xp_to_level - enemy.xp) <= 0): #If the amount of xp needed to level up is not 0 and the amount of xp needed to level up - the amount of xp the enemy gives...
                                player.xp_to_level -= enemy.xp #Subtract enemy xp worth from the amount of xp needed to level up
                                player.xp += enemy.xp #Add enemy xp worth to amount of xp
                                print("\nYou gained {} xp! You have {} xp left to level up!".format(enemy.xp, player.xp_to_level))
                                if(chance.chance(50)):
                                    print("{} dropped {} Gold!".format(enemy.name, int(random_gold) * 2))
                                    player_gold += random_gold
                                else:
                                    print("{} dropped {} Gold!".format(enemy.name, random_gold))
                                    player_gold += random_gold
                                flag = False
                            elif (player.xp_to_level <= 0 or (player.xp_to_level - enemy.xp) < 0): #Check if the player has enough xp to level up
                                print("\nYou gained {} xp!".format(enemy.xp))
                                player.levelUp() #Call the level up function
                                if(chance.chance(50)):
                                    print("{} dropped {} Gold!".format(enemy.name, int(random_gold) * 2))
                                else:
                                    print("{} dropped {} Gold!".format(enemy.name, random_gold))
                                flag = False
                        elif (enemy.is_alive()): #If the enemy is still alive
                            if(player.hp <= enemy.damage or player.hp - enemy.damage <= 0):
                                player.hp -= enemy.damage
                                print("{} hits you for {} damage! You fall to the ground.".format(enemy.name, enemy.damage))
                                flag = False
                                gameOver = True
                                death()
                            if(not player.hp <= 0):
                                player.hp -= enemy.damage #Enemy attacks (the amount of damage the enemy does is subtracted from the amount of hp the player has
                                print("\n{} hits you for {} damage! You have {} hp left!".format(enemy.name, enemy.damage, player.hp))


                    elif (choice == "f"):
                        print("\nYou attempt to flee like the coward you are.")
                        if(chance.chance(50)):
                            print("\nYou successfully flee from the battle against {}.".format(enemy.name))
                            time.sleep(2)
                            flag = False
                        else:
                            print("\nYour lame attempt to run from {} does not work. You trip over nothing and get eaten by {}!".format(enemy.name, enemy.name))
                            time.sleep(2)
                            flag = False
                            gameOver = True
                            death() #Calls the death function
                            
    elif(skeletonCaveRoom_active or enemy.name == "Skeleton King" or enemy.name == "Dragox" or enemy.name == "Romox" or enemy.name == "Dragon" or enemy.name == "Fencor"): #Removes option for fleeing if the player is battling in the Skeleton Cave or is battling a Boss
        while(flag):
            if(potion_inventory or fullPotion_inventory or lifePotion_inventory):
                choice = 7
                while (choice != "a" and player.is_alive):
                    choice = input("\n\nDo you want to (A)ttack or use a (P)otion?(Enemy Hp: {})(Player HP: {}) ".format(enemy.hp, player.hp)).lower()
                    if (choice == "a"):
                        if (chance.chance(50)): #Adds the chance to do a critical hit
                            damage = max_dmg
                        else: #Otherwise do regular damage
                            damage = best_weapon.damage
                        print("\nYou do {} damage with {} against {}!".format(damage, best_weapon.name, enemy.name))
                        time.sleep(2)
                        if(not(enemy.hp - damage) < 0):
                            enemy.hp -= damage
                            print("\n{} HP is {}.".format(enemy.name, enemy.hp))
                            time.sleep(2)
                        elif((enemy.hp - damage) <= 0):
                            enemy.hp -= damage
                            print("\n{} Hp is 0.".format(enemy.name))
                            time.sleep(2)
                        if (not enemy.is_alive()): #Check to see if enemy is dead 
                            if(not player.xp_to_level == 0 and (player.xp_to_level - enemy.xp) != 0): #If the amount of xp needed to level up is not 0 and the amount of xp needed to level up - the amount of xp the enemy gives...
                                player.xp_to_level -= enemy.xp #Subtract enemy xp worth from the amount of xp needed to level up
                                player.xp += enemy.xp #Add enemy xp worth to amount of xp
                                print("\nYou gained {} xp! You have {} xp left to level up!".format(enemy.xp, player.xp_to_level))
                                if(chance.chance(50)):
                                    print("{} dropped {} Gold!".format(enemy.name, int(random_gold) * 2))
                                    player_gold += random_gold
                                else:
                                    print("{} dropped {} Gold!".format(enemy.name, random_gold))
                                    player_gold += random_gold
                                flag = False
                            elif (player.xp_to_level == 0 and (player.xp_to_level - enemy.xp) < 0): #Check if the player has enough xp to level up
                                print("\nYou gained {} xp!".format(enemy.xp))
                                player.levelUp() #Call the level up function
                        elif (enemy.is_alive()): #If the enemy is still alive
                            if(not player.hp <= 0):
                                player.hp -= enemy.damage #Enemy attacks (the amount of damage the enemy does is subtracted from the amount of hp the player has
                                print("\n{} hits you for {} damage! You have {} hp left!".format(enemy.name, enemy.damage, player.hp))
                            elif(player.hp <= 0):
                                print("\n{} hits you for {} damage! That is more than you can take!".format(enemy.name, enemy.damage))
                                flag = False
                                gameOver = True
                                death()
                            elif (choice == "p"): #Below are all of the possible combinations of the potions you can have at any given point
                                if(potion_inventory >= 1 and fullPotion_inventory >= 1 and lifePotion_inventory >= 1):
                                    choice = 7
                                    while(choice != "p" and choice != "fp" and choice != "lp" and choice != "back"):
                                        choice = input("Will you use a (P)otion, a (F)ull (P)otion or a (L)ife (P)otion? Type \"back\" to go back").lower()
                                        if(choice == "p"):
                                            usePotion()
                                        elif(choice == "fp"):
                                            useFullPotion()
                                        elif(choice == "lp"):
                                            useLifePotion()
                                        elif(choice == "back"):
                                            pass
                                        else:
                                            print("Please enter a valid input!")
                                elif(potion_inventory == 0 and fullPotion_inventory >= 1 and lifePotion_inventory >= 1):
                                    choice = 7
                                    while(choice != "fp" and choice != "back" and choice != "lp"):
                                        choice = input("Will you use a (F)ull (P)otion or a (L)ife (P)otion? Type \"back\" to go back").lower()
                                        if(choice == "fp"):
                                            useFullPotion()
                                        elif(choice == "lp"):
                                            useLifePotion()
                                        elif(choice == "back"):
                                            pass
                                        else:
                                            print("Please enter a valid input!")
                                elif(potion_inventory >= 1 and fullPotion_inventory == 0 and fullPotion_inventory >= 1):
                                    choice = 7
                                    while(choice != "p" and choice != "lp" and choice != "back"):
                                        choice = input("Will you use a (P)otion or a (F)ull (P)otion? Type \"back\" to go back").lower()
                                        if(choice == "p"):
                                            usePotion()
                                        elif(choice == "lp"):
                                            useLifePotion()
                                        elif(choice == "back"):
                                            pass
                                        else:
                                            print("Please choose a valid input!")
                                elif(potion_inventory == 0 and fullPotion_inventory == 0 and fullPotion_inventory >= 1):
                                    choice = 7
                                    while(choice != "lp" and choice != "back"):
                                        choice = input("Will you use a (L)ife (P)otion? Type \"back\" to go back").lower()
                                        if(choice == "lp"):
                                            useLifePotion()
                                        elif(choice == "back"):
                                            pass
                                        else:
                                            print("Please choose a valid input!")
                                elif(potion_inventory >= 1 and fullPotion_inventory == 0 and fullPotion_inventory == 0):
                                    choice = 7
                                    while(choice != "p" and choice != "back"):
                                        choice = input("Will you use a (P)otion? Type \"back\" to go back").lower()
                                        if(choice == "p"):
                                            usePotion()
                                        elif(choice == "back"):
                                            pass
                                        else:
                                            print("Please choose a valid input!")
                                elif(potion_inventory >= 1 and fullPotion_inventory >= 1 and fullPotion_inventory == 0):
                                    choice = 7
                                    while(choice != "p" and choice != "fp" and choice != "back"):
                                        choice = input("Will you use a (P)otion or a (F)ull (P)otion? Type \"back\" to go back").lower()
                                        if(choice == "p"):
                                            usePotion()
                                        elif(choice == "fp"):
                                            useFullPotion()
                                        elif(choice == "back"):
                                            pass
                                        else:
                                            print("Please choose a valid input!")
                                elif(potion_inventory == 0 and fullPotion_inventory >= 1 and fullPotion_inventory == 0):
                                    choice = 7
                                    while(choice != "fp" and choice != "back"):
                                        choice = input("Will you use a (F)ull (P)otion? Type \"back\" to go back").lower()
                                        if(choice == "fp"):
                                            useFullPotion()
                                        elif(choice == "back"):
                                            pass
                                        else:
                                            print("Please choose a valid input!")
                                elif(potion_inventory == 0 and fullPotion_inventory == 0 and lifePotion_inventory == 0):
                                    print("You do not have any Potions!")
                            elif (choice == "lp"):
                                useLifePotion()
                                
            elif(not potion_inventory and not lifePotion_inventory and not fullPotion_inventory):
                choice = 7
                while (choice != "a" and player.is_alive):
                    choice = input("\n\nDo you want to (A)ttack?(Enemy Hp: {})(Player HP: {}) ".format(enemy.hp, player.hp)).lower()
                    if (choice == "i"):
                        view_inventory()
                    if (choice == "a"):
                        if (chance.chance(50)): #Adds the chance to do a critical hit
                            damage = max_dmg
                        else: #Otherwise do regular damage
                            damage = best_weapon.damage
                        print("\nYou do {} damage with {} against {}!".format(damage, best_weapon.name, enemy.name))
                        time.sleep(2)
                        if(not(enemy.hp - damage) < 0):
                            enemy.hp -= damage
                            print("\n{} HP is {}.".format(enemy.name, enemy.hp))
                            time.sleep(2)
                        elif((enemy.hp - damage) <= 0):
                            enemy.hp -= damage
                            print("\n{} Hp is 0.".format(enemy.name))
                            time.sleep(2)
                        if (not enemy.is_alive()): #Check to see if enemy is alive
                            if(not player.xp_to_level == 0 and not (player.xp_to_level - enemy.xp) <= 0): #If the amount of xp needed to level up is not 0 and the amount of xp needed to level up - the amount of xp the enemy gives...
                                player.xp_to_level -= enemy.xp #Subtract enemy xp worth from the amount of xp needed to level up
                                player.xp += enemy.xp #Add enemy xp worth to amount of xp
                                print("\nYou gained {} xp! You have {} xp left to level up!".format(enemy.xp, player.xp_to_level))
                                if(chance.chance(50)):
                                    print("{} dropped {} Gold!".format(enemy.name, int(random_gold) * 2))
                                    player_gold += random_gold
                                else:
                                    print("{} dropped {} Gold!".format(enemy.name, random_gold))
                                    player_gold += random_gold
                                flag = False
                            elif (player.xp_to_level <= 0 or (player.xp_to_level - enemy.xp) < 0): #Check if the player has enough xp to level up
                                print("\nYou gained {} xp!".format(enemy.xp))
                                player.levelUp() #Call the level up function
                                if(chance.chance(50)):
                                    print("{} dropped {} Gold!".format(enemy.name, int(random_gold) * 2))
                                    player_gold += random_gold
                                else:
                                    print("{} dropped {} Gold!".format(enemy.name, random_gold))
                                    player_gold += random_gold
                                flag = False
                        elif (enemy.is_alive()): #If the enemy is still alive
                            if(player.hp <= enemy.damage or player.hp - enemy.damage <= 0):
                                player.hp -= enemy.damage
                                print("{} hits you for {} damage! You fall to the ground.".format(enemy.name, enemy.damage))
                                flag = False
                                gameOver = True
                                death()
                            if(not player.hp <= 0):
                                player.hp -= enemy.damage #Enemy attacks (the amount of damage the enemy does is subtracted from the amount of hp the player has
                                print("\n{} hits you for {} damage! You have {} hp left!".format(enemy.name, enemy.damage, player.hp))
        
def romox_battle():
    pass

def dragox_battle():
    pass

def fencor_battle():
    pass

def view_inventory(): #When called prints whatever is in the player's inventory
    if(umari_inventory):
        print(fencor_umari)
    if(scepter_inventory):
        print(romox_scepter)
    if(dSword_inventory):
        print(dragox_sword)
    if(krambit_inventory):
        print(krambit)
    if(handcannon_inventory):
        print(handcannon)
    if(crossbow_inventory):
        print(crossbow)
    if(bow_inventory):
        print(bow)
    if(heavySword_inventory):
        print(heavy_sword)
    if(sword_inventory):
        print(sword)
    if(dagger_inventory):
        print(dagger)
    if(rock_inventory):
        print(rock)
    if(potion_inventory):
        print(potion)
        if(potion_inventory > 1):
            print("You have {} Potions!".format(potion_inventory))
        else:
            print("You have {} Potion!".format(potion_inventory))
    if(lifePotion_inventory):
        print(life_potion)
        if(lifePotion_inventory > 1):
            print("You have {} Life Potions!".format(lifePotion_inventory))
        else:
            print("You have {} Life Potion!".format(lifePotion_inventory))
    if(fullPotion_inventory):
        print(full_potion)
        if(fullPotion_inventory > 1):
            print("You have {} full Potions!".format(fullPotion_inventory))
        else:
            print("You have {} full Potion!".format(fullPotion_inventory))            
    if(cellarKey_inventory):
        print(cellarKey)
    if(torch_inventory):
        print(torch)
    if(jewelEgg_inventory):
        print(jewel_egg)
    if(book_inventory):
        print(book)
    if(greatOakKey_inventory):
        print(great_oak_key)
    if(note_inventory):
        print(note)
    if(legendarySword_inventory):
        print(legendary_sword)
    if(triforce_inventory):
        print(triforce)
    print("\n\tGold:",player_gold)
    print("\nHP:", player.hp)
    print("\nLevel:", player.level)
    print("\nXp:", player.xp)
    print("\nXp to next level:", player.xp_to_level)

def usePotion():
    global potion_inventory
    if(potion_inventory >= 1 and player.hp != player.max_hp):
        items.Healer.heal(player, 50)
        print("\n\tYou use the potion and regain 50 hp!")
        potion_inventory -= 1
    elif(potion_inventory == 0):
        print("\n\tYou do not have a Potion to use!")
    elif(player.hp == player.max_hp):
        print("\n\tUsing a Potion now is pointless, don't waste it!")

def useLifePotion():
    global lifePotion_inventory
    if(lifePotion_inventory >= 1):
        items.Healer.increase_life(player, 100)
        print("\n\tYou use the life potion and increase your hp by 100!")
        lifePotion_inventory -= 1
    elif(lifePotion_inventory == 0):
        print("\n\tYou do not have a Life Potion to use!")

def useFullPotion():
    global fullPotion_inventory
    if(fullPotion_inventory >= 1):
        items.Healer.full_restore(player)
        print("\n\tYou used the Full Potion and restore all of your hp!")
        fullPotion_inventory -= 1
    elif(fullPotion_inventory == 0):
        print("You do not have a Full Potion to use!")
    elif(player.hp == player.max_hp):
        print("\n\tUsing a Full Potion now is pointless, don't waste it!")

def death():
    global gameOver
    print("\n\n\tYou have died..")
    time.sleep(4)
    playAgain = input("\n\nWould you like to load your game?(Y/N): ").lower()
    while(playAgain != "y" and playAgain != "n"):
        if (playAgain == "y"):
            gameOver = False
            load_game()
        elif (playAgain == "n"):
            print("\nThanks for playing! Hope you enjoyed your time playing Hjalmion: The Rise Of Fencor. Please, play again sometime!")
            raise SystemExit
        else:
            print("\nPlease enter a valid input!")

def help():
    print("\nThis is a list of commands in alphabetical order that you can do. The words in the brackets specify where this action is used.")
    time.sleep(3)
    print("\n(A)ttack: (Letter typed: 'a', used in: Battle")
    time.sleep(0.5)
    print("\n(B)ack: (Letter typed: 'b', used in: Shop and Blacksmith to exit out of the shop.")
    time.sleep(0.5)
    print("\n(E)ast: (Letter typed: 'e', used to move East in a room.")
    time.sleep(0.5)
    print("\n(F)lee: (Letter typed: 'f', used to flee from a battle. 50% chance it will fail.")
    time.sleep(0.5)
    print("\n(F)ull (P)otion: (Letter typed: 'fp', uses a Full Potion on the Player if one is in their inventory.")
    time.sleep(0.5)
    print("\nHelp: (Letter typed: 'help', used to get to this menu!")
    time.sleep(0.5)
    print("\n(I)nventory: (Letter typed: 'i', used to look at the player's inventory.")
    time.sleep(0.5)
    print("\nLook: (Letter typed: 'look', used to get more information about a room. Good things come to people who use this command often!")
    time.sleep(0.5)
    print("\n(L)ife (P)otion: (Letter typed: 'lp', uses a Life Potion on the player if one is in their inventory.")
    time.sleep(0.5)
    print("\n(N): (Letter typed: 'n', used to decline actions.")
    time.sleep(0.5)
    print("\n(N)orth: (Letter typed: 'n', used to move North in a room.")
    time.sleep(0.5)
    print("\n(N)orth (W)est: (Letter typed: 'nw', used to move North West in a room.")
    time.sleep(0.5)
    print("\n(P): (Letter typed: 'p', uses a Potion on the player if one is in their inventory.")
    time.sleep(0.5)
    print("\n(S)outh: (Letter typed: 's', used to move South in a room.")
    time.sleep(0.5)
    print("\n(S)outh (E)ast: (Letter typed: 'se', used to move South East in a room.")
    time.sleep(0.5)
    print("\n(W)est: (Letter typed: 'w', used to move West in a room.")
    time.sleep(0.5)
    print("\n(Y): (Letter typed: 'y', used to approve of actions.")
    time.sleep(3)

def find_potion():
    global potion_inventory
    global lifePotion_inventory
    global fullPotion_inventory
    if(chance.chance(50)):
        print("You find a Potion!")
        potion_inventory += 1
    elif(chance.chance(5)):
        print("You find a Life Potion!")
        lifePotion_inventory += 1
    elif(chance.chance(10)):
        print("You find a Full Potion!")
        fullPotion_inventory += 1
    else:
        print("You do not find anything.")

def game_end():
    print("\n\n\n\n\nYou have (surprisingly) reached the end of Hjalmion: The Rise Of Fencor! Thank you so much for playing. I am thinking of making a sequel in the future (whenever that may be), so look for it! This game was coded, thought of, and spearheaded by Nick Mills. He was 16 when he finished this. Thank you goes out to Mr. Smith for teaching me Python, Nate Grobe for all of the funny moments, Tim Boyadjian for introducing me to programming, and last but not least, the Internet, for helping me to solve my problems! I spent about a day in total working on this. It was fun, frustrating, and rewarding. This has definitely been a good experience. Thank you for sharing it with me!")
    
def save_game(): #Saves the current game state to be loaded from a file later
    import pickle
    
    #All variables that could have been changed during the course of play
    global player
    global player_gold
    global skeletonKing_death
    global dragon_death
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global cellarKey_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global potion_inventory
    global lifePotion_inventory
    global fullPotion_inventory    
    global counter
    global flag
    global flag1
    global flag2
    global flag3
    global flag4
    global flag5
    global gameOver 
    global meadow_counter
    global deadEndValley_counter
    global dungeon_counter
    global village_counter
    global forest_counter
    global cliffside_counter
    global greatOak_counter
    global cellar_counter
    global skeletonCave_counter
    global cave_counter
    global secretPassage_counter
    global dragonsLair_counter
    global church_counte
    global cemetary_counter
    global market_counter
    global castle_counter
    global active_room
    ##The following is used for testing purposes
    #print(player)
    #print(player_gold)
    #print(skeletonKing_death)
    #print(dragon_death)
    #print(umari_inventory)
    #print(scepter_inventory)
    #print(dSword_inventory)
    #print(krambit_inventory)
    #print(handcannon_inventory)
    #print(crossbow_inventory)
    #print(bow_inventory)
    #print(heavySword_inventory)
    #print(sword_inventory)
    #print(dagger_inventory)
    #print(rock_inventory)
    
    with open("saves\save1.pkl", "wb") as outfile:
        pickle.dump(player, outfile)
        pickle.dump(player_gold, outfile)
        pickle.dump(skeletonKing_death, outfile)
        pickle.dump(dragon_death, outfile)
        pickle.dump(umari_inventory, outfile)
        pickle.dump(scepter_inventory, outfile)
        pickle.dump(dSword_inventory, outfile)
        pickle.dump(krambit_inventory, outfile)
        pickle.dump(handcannon_inventory, outfile)
        pickle.dump(crossbow_inventory, outfile)
        pickle.dump(bow_inventory, outfile)
        pickle.dump(heavySword_inventory, outfile)
        pickle.dump(sword_inventory, outfile)
        pickle.dump(dagger_inventory, outfile)
        pickle.dump(rock_inventory, outfile)
        pickle.dump(cellarKey_inventory, outfile)
        pickle.dump(torch_inventory, outfile)
        pickle.dump(book_inventory, outfile)
        pickle.dump(greatOakKey_inventory, outfile)
        pickle.dump(note_inventory, outfile)
        pickle.dump(jewelEgg_inventory, outfile)
        pickle.dump(legendarySword_inventory, outfile)
        pickle.dump(triforce_inventory, outfile)
        pickle.dump(potion_inventory, outfile)
        pickle.dump(lifePotion_inventory, outfile)
        pickle.dump(fullPotion_inventory, outfile)
        pickle.dump(counter, outfile)
        pickle.dump(flag, outfile)
        pickle.dump(flag1, outfile)
        pickle.dump(flag2, outfile)
        pickle.dump(flag3, outfile)
        pickle.dump(flag4, outfile)
        pickle.dump(flag5, outfile)
        pickle.dump(gameOver, outfile)
        pickle.dump(meadow_counter, outfile)
        pickle.dump(deadEndValley_counter, outfile)
        pickle.dump(dungeon_counter, outfile)
        pickle.dump(village_counter, outfile)
        pickle.dump(forest_counter, outfile)
        pickle.dump(cliffside_counter, outfile)
        pickle.dump(greatOak_counter, outfile)
        pickle.dump(cellar_counter, outfile)
        pickle.dump(skeletonCave_counter, outfile)
        pickle.dump(cave_counter, outfile)
        pickle.dump(secretPassage_counter, outfile)
        pickle.dump(dragonsLair_counter, outfile)
        pickle.dump(church_counter, outfile)
        pickle.dump(cemetary_counter, outfile)
        pickle.dump(market_counter, outfile)
        pickle.dump(castle_counter, outfile)
        pickle.dump(active_room, outfile)
    print("\n\tGame Saved...")
    
def load_game():
    import pickle
        
    #All variables that could have been changed during the course of play
    global player
    global dragox_death
    global romox_death
    global player_gold
    global skeletonKing_death
    global dragon_death
    global player_gold
    global umari_inventory
    global scepter_inventory
    global dSword_inventory
    global krambit_inventory
    global handcannon_inventory
    global crossbow_inventory
    global bow_inventory
    global heavySword_inventory
    global sword_inventory
    global dagger_inventory
    global rock_inventory
    global cellarKey_inventory
    global torch_inventory
    global book_inventory
    global greatOakKey_inventory
    global note_inventory
    global jewelEgg_inventory
    global legendarySword_inventory
    global triforce_inventory
    global potion_inventory
    global lifePotion_inventory
    global fullPotion_inventory    
    global counter
    global flag
    global flag1
    global flag2
    global flag3
    global flag4
    global flag5
    global gameOver 
    global meadow_counter
    global deadEndValley_counter
    global dungeon_counter
    global village_counter
    global forest_counter
    global cliffside_counter
    global greatOak_counter
    global cellar_counter
    global skeletonCave_counter
    global cave_counter
    global secretPassage_counter
    global dragonsLair_counter
    global church_counte
    global cemetary_counter
    global market_counter
    global castle_counter
    global active_room
    
    with open("saves\save1.pkl", "rb") as infile:
        """WARNING!! DO NOT CHANGE THE ORDER OF THESE VARIABLES AS IT LOADS EACH VARIABLE IN THE ORDER THEY WERE DUMPED!"""
        player = pickle.load(infile)
        player_gold = pickle.load(infile)
        skeletonKing_death = pickle.load(infile)
        dragon_death = pickle.load(infile)
        umari_inventory = pickle.load(infile)
        scepter_inventory = pickle.load(infile)
        dSword_inventory = pickle.load(infile)
        krambit_inventory = pickle.load(infile)
        handcannon_inventory = pickle.load(infile)
        crossbow_inventory = pickle.load(infile)
        bow_inventory = pickle.load(infile)
        heavySword_inventory = pickle.load(infile)
        sword_inventory = pickle.load(infile)
        dagger_inventory = pickle.load(infile)
        rock_inventory = pickle.load(infile)
        cellarKey_inventory = pickle.load(infile)
        torch_inventory = pickle.load(infile)
        book_inventory = pickle.load(infile)
        greatOakKey_inventory = pickle.load(infile)
        note_inventory = pickle.load(infile)
        jewelEgg_inventory = pickle.load(infile)
        legendarySword_inventory = pickle.load(infile)
        triforce_inventory = pickle.load(infile)
        potion_inventory = pickle.load(infile)
        lifePotion_inventory = pickle.load(infile)
        fullPotion_inventory = pickle.load(infile)
        counter = pickle.load(infile)
        flag = pickle.load(infile)
        flag1 = pickle.load(infile)
        flag2 = pickle.load(infile)
        flag3 = pickle.load(infile)
        flag4 = pickle.load(infile)
        flag5 = pickle.load(infile)
        gameOver = pickle.load(infile)
        meadow_counter = pickle.load(infile)
        deadEndValley_counter = pickle.load(infile)
        dungeon_counter = pickle.load(infile)
        village_counter = pickle.load(infile)
        forest_counter = pickle.load(infile)
        cliffside_counter = pickle.load(infile)
        greatOak_counter = pickle.load(infile)
        cellar_counter = pickle.load(infile)
        skeletonCave_counter = pickle.load(infile)
        cave_counter = pickle.load(infile)
        secretPassage_counter = pickle.load(infile)
        dragonsLair_counter = pickle.load(infile)
        church_counter = pickle.load(infile)
        cemetary_counter = pickle.load(infile)
        market_counter = pickle.load(infile)
        castle_counter = pickle.load(infile)
        active_room = pickle.load(infile)
        print("\n\tGame Loaded...")
        #Puts Player back into the room they saved in
        if(active_room == "meadow"):
            meadow()
        if(active_room == "great oak"):
            great_oak()
        if(active_room == "cliffside"):
            cliffside()
        if(active_room == "dead end valley"):
            dead_end_valley()
        if(active_room == "forest"):
            forest()
        if(active_room == "cave"):
            cave()
        if(active_room == "secret passage"):
            secret_passage()
        if(active_room == "dragons lair"):
            dragons_lair()
        if(active_room == "house"):
            house()
        if(active_room == "cellar"):
            cellar()
        if(active_room == "dungeon"):
            dungeon()
        if(active_room == "skeleton cave"):
            skeleton_cave()
        if(active_room == "village"):
            village()
        if(active_room == "cemetary"):
            cemetary()
        if(active_room == "church"):
            church()
        if(active_room == "marketplace"):
            marketplace()
        if(active_room == "blacksmith"):
            blacksmith()
        if(active_room == "shop"):
            shop()
        if(active_room == "castle"):
            castle()
        if(active_room == "shangri-la"):
            if(dragox_death):
                romox_battle()
            elif(romox_death):
                fencor_battle()
            else:
                shangri_la()
        
        ##The following is used for testing purposes
        #print(player)
        #print(player_gold)
        #print(skeletonKing_death)
        #print(dragon_death)
        #print(umari_inventory)
        #print(scepter_inventory)
        #print(dSword_inventory)
        #print(krambit_inventory)
        #print(handcannon_inventory)
        #print(crossbow_inventory)
        #print(bow_inventory)
        #print(heavySword_inventory)
        #print(sword_inventory)
        #print(dagger_inventory)
        #print(rock_inventory)     
