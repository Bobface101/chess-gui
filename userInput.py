# Handles the moves of the user

import turtle, handlers, drawboard, pieces
from screen import screen
from board_state import board_state


def select(x, y):

    from drawboard import tiles

    piece_already_selected = False

    selected_piece = handlers.find_piece_on(handlers.roughcoordtotile(x,y))
    
    tile = handlers.roughcoordtotile(x,y)

    print(f"{selected_piece} selected at tile {tile}")

    tileList = [[pair[0], pair[1]] for pair in drawboard.tiles.items()]

    for spot, turtle in tileList:
        
        if turtle.shape() == "assets/highlight.gif": #clear old tiles

            piece_already_selected = True

            starting_piece = handlers.find_piece_on(spot)

            turtle.shape("arrow")    

            turtle.ht()

    

    if selected_piece != None and not piece_already_selected: # if there is a piece on the tile,

        # get moves for piece 

        # highlight tile
        tileTurtle = drawboard.tiles[tile]
        tileTurtle.shape("assets/highlight.gif")
        tileTurtle.color((0.2,0.2,0.2))
        tileTurtle.st()

        # bring turtle to front layer 
        handlers.bring_turtle_to_front(tile)

    if piece_already_selected and selected_piece != None:
        pieces.capture(starting_piece, selected_piece, tile)
    
    screen.update()


def listen():
    screen.onclick(select)
    screen.mainloop()




