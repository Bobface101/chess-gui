import pieces, drawboard, userInput, handlers, turtle
from screen import screen

# set turtle.shape like different costumes from scratch for attacked tiles, selected tiles, check, etc. that way we dont need a million diff turtles


# set up the starting state of the board
handlers.generate_screen()
drawboard.initialise_board()
drawboard.draw_board(pieces.initialise_pieces())

# while game not over:
    # white move 
    # update 
    # black move 
    # update 

userInput.listen()

turtle.done()