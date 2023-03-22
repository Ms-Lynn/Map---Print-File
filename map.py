# All of the information for the game board

# tile information
tile = ["Start", "PlainSpace", "ThrownRoom", "SpookySpace"]
tiles = {
    tile[0] : {"Description" : "Your in the foyer of a castle."},
    tile[1] : {"Description" : "Your are in a boring room."},
    tile[2] : {"Description" : "Your in a beautifly thrown room."},
    tile[3] : {"Description" : "This room is very spooky!"},    }

# games map made with an array
map = [
     [tile[0], tile[1], tile[3]],
     [tile[1], tile[1], tile[1]],
     [tile[3], tile[2], tile[3]],
     [tile[1], tile[1], tile[1]]     ]

# map size
max_row = 3
max_col = 2
