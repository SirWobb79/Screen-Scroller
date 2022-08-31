import os
import numpy as np

# The world
map = [
    ["#","#","#","#","#"," "," "],
    ["#",".",".",".","#"," "," "],
    ["#",".",".",".","#"," "," "],
    ["#",".",".",".","#"," "," "],
    ["#",".",".",".","#"," "," "],
    ["#",".",".",".","#","#","#"],
    ["#",".",".",".",".",".","#"],
    ["#","#","#","#","#",".","#"],
    ["#",".",".",".",".",".","#"],
    ["#",".",".",".","#","#","#"],
    ["#",".",".",".","#"," "," "],
    ["#",".",".",".","#"," "," "],
    ["#",".",".",".","#"," "," "],
    ["#","#","#","#","#"," "," "]
]

# Spawn position. Remember that the 'y' is inverted but the 'x' isn't
player = {'y': 1, 'x': 1}

# Moving the player
moves = {"W": {'y': -1, 'x': 0},
         "A": {'y': 0, 'x': -1},
         "S": {'y': 1, 'x': 0},
         "D": {'y': 0, 'x': 1}
        }
        
# Changes the 2D list of 'map' to be a numpy array
map = np.array(map)

# Your player character
map[player['y']][player['x']] = "$"

# Keeping the shape of the map when moving (as a function)
def print_map(map):
    for row in map:
        print(" ".join(str(n) for n in row))

#Prints the map
print_map(map)

def walk(world):
    
    world = np.array(world)

    game = True
    while game:
    
        # Basic moving
        move = input("Move with WASD ")
    
        move = move.upper()
    
        pos = moves[move]
   
        x2 = player['x'] + pos['x']
        y2 = player['y'] + pos['y']
     
        map_pos = map[y2][x2]
    
        # Keeps the terminal clean
        os.system("clear")
    
        print("---------")
    
        # Collision and moving
        if map_pos != "#":
            world[player['y']][player['x']] = "."
            world[y2][x2] = "$"
            
            player['x'] = x2
            player['y'] = y2
            
        # Change the -2s and +3 for a bigger screen. Keep the -n 1 smaller then the +n.
        print_map(world[max(y2-2,0) : y2+3, max(x2-2,0) : x2+3])
    
walk(map)
