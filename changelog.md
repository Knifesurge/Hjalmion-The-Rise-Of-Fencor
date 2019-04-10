# 2019-03-22:
1. Updated `README` to match project pursuits.
2. Created `Hjalmion_new.py` to keep original and rewrite files separate. At the end of the project, `Hjalmion_new` will become just `Hjalmion`, and `Hjalmion` will become `Hjalmion_old`.
3. Added `.gitignore` file
4. Rewrote `Player.py` to only include one class definition
5. Added inventory to Player class itself (dict)
6. Added some helper methods to retrieve now 'private' attributes
7. Exp needed to advance to next level now doubles each level
8. Started fleshing out `Hjalmion_new.py`
9. Added `Rooms.py` to describe the rooms in the game. ~~Will be implemented as a Linked List~~ __Does not make sense to use a linked list structure__. Each room has N,NE,E,SE,S,SW,W,NW pointers to its adjacent rooms, effectively creating a map of the game world. One note however, is that it will not be possible to easily iterate through the list. One way to traverse is by historical addition to the list. That is, `Rooms` maintains a list (which acts like a set) of it's nodes in the order at which they are added, which allows it to be traversed in some way. 
10. Rooms now hold what enemies are inside of the room. Added helper methods to get the list of Enemies themselves, as well as pick a random Enemy from the list.
11. Rooms when printed now show what Rooms are adjacent to it, and which direction.
12. Added a `Utils` module that holds various functions to read and write data from JSON files.
13. Added *Created:* amd *Updated:* Comments at the head of each file in order to help track which files are new (part of the rewrite) and which are the original files (anything pre-2019)
14. Added a `data` folder that will hold all the json files for the game.
15. Created a `Enemies.json` file that holds all of the Enemies currently in the game. The layout in the file is the current standard for how to lay out the file and each Enemy's values.

# 2019-03-23:
1. Finished `Enemy#create_from_filedata`. Correctly creates enemies based on filedata.
2. Moved `Tests.py` to the main folder (instead of inside a tests folder) to test various aspects of the rewrite. Also added to .gitignore
3. Renamed `enemies.py` to `Enemy.py`. Used same format for `chance`, `items`, and `player`.

# 2019-03-24
1. Finished `Item#create_from_filedata`. Correctly creates items based on filedata.
2. Removed all `Item` definitions. Items created from filedata and used from lists inside the `Hjalmion` class.
3. Added __all__ Items to `Items.json`.
4. `Tests.py` now loads and prints enemies and items from filedata.

# 2019-03-27
1. `Utils#read_json` appends `None` to the end of the data cache after reading a file to separate the data. Added this in a previous update but forgot to mention it.
2. Added `Rooms.json` and the general format that the Rooms will follow.
3. Adjusted some of the `_Room` constructor code to follow the `Rooms.json` format.
4. Fixed `Rooms#insert` after changing the `_Room` constructor parameters.

# 2019-03-29
1. Started adding the `Room` definitions into `Rooms.json`.
2. Added `Ideas.txt` to track ideas and possible TODOs.
3. Added *dependencies* to the `Room` definitions. This will be a `list` of `Items` or `Conditions` in order to *access* the `Room` or to get a different *description*.

# 2019-04-10
1. Removed `victory` variable from `Player` since its not used.
2. Room movement will be handled by the `Player` class via a method named `move_room(dir:str)`. `Player#move_room` takes a char (str) as an argument, `dir`, representing the direction the Player should move. If a `Room` doesn't exist in that direction, `False` is returned and the `Player` is not moved.
3. `Rooms` is no longer a `Linked List` under the hood; it doesn't need it. Now just maintains a Python `List` of `Rooms`.
4. `Room` now properly prints its adjacent `Rooms` in its `__str__` method.
5. Added a `get_room_in_dir` method to `Room`, which gets an adjacent `Room` in a specified `dir` (str). If an invalid direction is provided, just returns itself.
6. ~~Cleaned up `Room#north`, `Room#south`, etc. Since in `_Room#__init__` it only adds rooms if they are not empty in `Rooms.json`, there is no need to check if it exists in `Room#__adj`, since it most certainly does.~~ Still needs it.
7. `Room#this` created as a helper function to `Room#get_room_in_dir` since it returns a function call.
8. Made a `docs` folder to hold related documentation for the `JSON` files for `Rooms`, `Enemies`, and `Items`.