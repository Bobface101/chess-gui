# Handles the moves of the user

import turtle, handlers, drawboard
from screen import screen
from board_state import board_state

def select(x, y):

    from drawboard import tiles

    selected_piece = handlers.find_piece_on(handlers.roughcoordtotile(x,y))
    
    tile = handlers.roughcoordtotile(x,y)

    print(f"{selected_piece} selected at tile {tile}")

    if selected_piece != None: # if there is a piece on the tile,

        # get moves for piece 

        # highlight tile
        tileTurtle = drawboard.tiles[tile]
        tileTurtle.shape("assets/highlight.gif")
        #tileTurtle.color(0,0,0,0.3)
        tileTurtle.st()
    
    screen.update()


def listen():
    screen.onclick(select)
    screen.mainloop()




