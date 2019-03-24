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