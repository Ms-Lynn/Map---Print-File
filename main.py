###############################################################################
# Title: Simple Text Adventure Game
# coder: Ms. Lynn
# version: 003
###############################################################################
''' Program creates a simple map using nested lists that a character
    can move around on through a simple menu.
    Character now has an inventory to collect 'objects' in.
    Program has two objects a key and a treasure chest.
    The key must be in the characters inventory in order to open the chest

    This program uses dictionaries to create characters and 
    Tile charateristics.
    '''
#------------------------------------------------------------------------------
# Current Location
row = 0
col = 0
max_row = 3
max_col = 2

inventory = []

playing = True

objects = {
          "Chest" : {"Description" : "You find a treasure chest.",
                     "Status" : "closed",
                     "Location": [2, 1], 
                     "Action" : ["Open","Inspect"],
                     "Requirement" : ["Key", None]},
          "Key" : {"Description" : "You find a key haning on the wall.",
                   "Status" : "lost",
                   "Location" : [0, 1],
                   "Action" : ["Take"],
                   "Requirement" : [None]}    }

tile = ["Start", "PlainSpace", "ThrownRoom", "SpookySpace"]
tiles = {
    tile[0] : {"Description" : "Your in the foyer of a castle."},
    tile[1] : {"Description" : "Your are in a boring room."},
    tile[2] : {"Description" : "Your in a beautifly thrown room."},
    tile[3] : {"Description" : "This room is very spooky!"},    }

map = [
     [tile[0], tile[1], tile[3]],
     [tile[1], tile[1], tile[1]],
     [tile[3], tile[2], tile[3]],
     [tile[1], tile[1], tile[1]]     ]


# Functions -------------------------------------------------------------------
def Movement():
    '''When player choosed 'walk' in the main menu it trigers this
       movement functions. This function will have a sub menu of
       directions for the user to choose from. When a valid choice
       is made the global variables row and col[umb] will be changed
       so that the players current location will update.'''
    global playing, row, col, max_row, max_col
    orientating = playing
    while orientating:
        print(f"Choose a direction: ")
        if not row==0:
            print(f"-North")
        if not row==max_row:
            print(f"-South")
        if not col==max_col:
            print(f"-East")
        if not col==0:
            print(f"-West")
        orientating = False
        dirchoice = input(f"Choice: ")
        if dirchoice == "North" and row > 0:
            row -= 1
        elif dirchoice == "South" and row < max_row:
            row += 1
        elif dirchoice == "East" and col < max_col:
            col += 1
        elif dirchoice == "West" and col > 0:
            col -= 1
        elif dirchoice == "Quit":
            playing = False
        else:
            print(f"Sorry you can not move in that direction.")
            orientating = True


def InspectRoom():
      '''When player choosed 'look' in the main menu it trigers this
       inspect room functions. This function will look through the 
       games object and see if any are located on the players current
       tile. If one is then a sub menu will populate from that object
       dictionary.'''
    global row, col, map, playing, inventory, objects
    found_object = False
    room_inventory = []
    location_description =  map[row][col]
    print(f"You look around the room.")
    for object in objects:
        object_row = objects[object]["Location"][0]
        object_col = objects[object]["Location"][1]
        if object_row == row and object_col == col:
            print(objects[object]["Description"])
            found_object = True
            room_inventory.append(object)
    if found_object == True:
        for item in room_inventory:
            if item == "Chest":
              ChestActions()
            elif item == "Key":
              KeyActions()
            else:
              print(f"There are no interactive objects in this room.")
    else:
        print(f"There are no objects in this room.")
    room_inventory = []


def MainMenu():
      '''When the game is activated these are all the players inital
         actions that are possible. This is the games main menu.'''
  global playing
  thinking = playing
  while thinking:
      print(f"Choose to move to another room or look around: ")
      print(f"-Walk")
      print(f"-Look")
      mainChoice = input(f"Choice: ")
      if mainChoice == "Walk":
          Movement()
          break
      elif mainChoice == "Look":
          InspectRoom()
          if playing == False:
              break
      elif mainChoice == "Quit":
          playing = False
          break
      else:
         print(f"Sorry that is not a valid choice.") 


def ChestActions():
    '''When the player choosed to inspect the chest object this function
       is triggered so that it can provided valid options pertaining to this
       object. Main game play goal is to find a key and then open this chest.'''
    global playing, objects, inventory
    deciding = playing
    while deciding:
        print(f"Choose an Actions: ")
        for action in objects["Chest"]["Action"]:
            print(f"-{action}")
        print(f"-Done")
        chest_choice = input("Actions: ")
        # Open the Treasure Chest--------------------------------------
        if chest_choice == objects["Chest"]["Action"][0]:  
            if objects["Chest"]["Status"] == "open":
                print(f"The cheat is already open.")
            else:
                itemfound = False
                for item in inventory:
                    if item == objects["Chest"]["Requirement"][0]:
                        inventory.remove("Key")
                        print(f"You opened the chest!")
                        objects["Chest"]["Status"] = "open"
                        itemfound = True
                if itemfound == False:
                    print(f"You need to find a key to open the chest.")
        # Inspect the Treasure Chest--------------------------------------
        elif chest_choice == objects["Chest"]["Action"][1]: 
            if objects["Chest"]["Status"] == "closed":
                print(f"The chest appears to be locked.")
            elif objects["Chest"]["Status"] == "open":
                print(f"The chest appears to be open.")
            else:
                print(f"Something has gone wrong with the chest.")
        elif chest_choice == "Done":
            deciding = False
        elif chest_choice == "Quit":
            playing = False
            deciding = False
        else:
            print(f"Sorry that is not a valid choice")
  

def KeyActions():
      '''When the player finds the key object this fuction will trigger to give
         the player options that are unique to this object. The play will be able
         to pick up the key and place it in their inventory. '''
    global playing, objects, inventory
    deciding = playing
    while deciding: 
        print(f"Choose an Actions: ")
        for action in objects["Key"]["Action"]:
            print(f"-{action}")
        print(f"-Done")
        key_choice = input("Actions: ")
        # Take Key  --------------------------------------
        if key_choice == objects["Key"]["Action"][0]:  
            objects["Key"]["Location"][0] = None
            objects["Key"]["Location"][1] = None
            objects["Key"]["Status"] = "found"
            print(f"Congrats the key is now in your inventory!")
            inventory.append("Key")
            deciding = False
        elif chest_choice == "Done":
            deciding = False
        elif chest_choice == "Quit":
            playing = False
            deciding = False
        else:
            print(f"Sorry that is not a valid choice.")
        
  
# Main Code --------------------------------------------------------------------
print(f"Welcome to my Castle!")
print(f"Goal is to find and open a treasure chest.")
while playing:
    location_description =  map[row][col]
    for tile in tiles:
      if tile == location_description:
        print(tiles[tile]["Description"])
    MainMenu()
print(f"Thanks for playing!!!!")