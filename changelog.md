# 2019-03-22:
1. Updated `README` to match project pursuits.
2. Created `Hjalmion_new.py` to keep original and rewrite files separate. At the end of the project, `Hjalmion_new` will become just `Hjalmion`, and `Hjalmion` will become `Hjalmion_old`.
3. Added `.gitignore` file
4. Rewrote `Player.py` to only include one class definition
5. Added inventory to Player class itself (dict)
6. Added some helper methods to retrieve now 'private' attributes
7. Exp needed to advance to next level now doubles each level
8. Started fleshing out `Hjalmion_new.py`
9. Added `Room.py` to describe the rooms in the game. Will be implemented as a Linked List, with N,E,S,W pointers to its adjacent rooms, effectively creating a map of the game world.
10. Rooms now hold what enemies are inside of the room. Added helper methods to get the list of Enemies themselves, as well as pick a random Enemy from the list.
11. Rooms when printed now show what Rooms are adjacent to it, and which direction.
