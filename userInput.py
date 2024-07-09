# Handles the moves of the user

import turtle, handlers, drawboard
from screen import screen
from board_state import board_state

def select(x, y):

    from drawboard import tiles

    selected_piece = handlers.find_piece_on(handlers.roughcoordtotile(x,y))
    
    tile = handlers.roughcoordtotile(x,y)

    print(f"{selected_piece} selected at tile {tile}")

    tileList = [[pair[0], pair[1]] for pair in drawboard.tiles.items()]

    for k, turtle in tileList:
        print(f"{k} status: {turtle.shape()}")
        if turtle.shape() == "assets/highlight.gif": #clear old tiles
            turtle.shape("arrow")            
            turtle.ht()

    

    if selected_piece != None: # if there is a piece on the tile,

        # get moves for piece 

        # highlight tile
        tileTurtle = drawboard.tiles[tile]
        tileTurtle.shape("assets/highlight.gif")
        #tileTurtle.color(0,0,0,0.3)
        tileTurtle.st()
        screen.update()

        # bring turtle to front layer 
        handlers.bring_turtle_to_front(tile)
    
    screen.update()


def listen():
    screen.onclick(select)
    screen.mainloop()




