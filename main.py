import pieces, drawboard, userInput, handlers, turtle, board_state
from screen import screen

# set turtle.shape like different costumes from scratch for attacked tiles, selected tiles, check, etc. that way we dont need a million diff turtles


# set up the starting state of the board
drawboard.generate_screen()
drawboard.initialise_board()
drawboard.initialise_tiles()

initial_state = pieces.initialise_pieces()
handlers.send_board_state(initial_state)
drawboard.draw_board(board_state.board_state)
screen.update()


# while game not over:
    # white move 
    # update 
    # black move 
    # update 

userInput.listen()

turtle.done()