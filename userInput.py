# Handles the moves of the user

import turtle, handlers
from screen import screen
from board_state import board_state
from drawboard import tiles



def select(x, y):

    selected_piece = handlers.find_piece_on(handlers.roughcoordtotile(x,y))
    tile = handlers.roughcoordtotile(x,y)

    if selected_piece != None: # if there is a piece on the tile,

        # get moves for piece 

        # highlight tile
        tiles[tile].color(0,0,0,0.5)
        tiles[tile].shape("/assets/highlight.gif")


    print(f"You clicked at {x},{y} or tile {handlers.roughcoordtotile(x,y)}")

def listen():
    screen.onclick(select)
    screen.mainloop()




