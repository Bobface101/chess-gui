import turtle, handlers
from screen import screen

tiles = []

def initialise_board():

    global tiles

    # setting up the board
    
    screen.addshape('assets/board.gif')
    board = turtle.Turtle()
    board.shape('assets/board.gif')

    # add column and row labels 
    scribe = turtle.Turtle()
    scribe.ht()
    scribe.pu()
    scribe.speed(0)
    scribe.goto(-415, -395)
    labels = [ "1", "2", "3", "4", "5", "6", "7", "8", "a", "b", "c", "d", "e", "f", "g", "h"]
    i = 0
    while i < 8:
        scribe.write(labels[i], font=("Montserrat", 12, "bold"))
        scribe.goto(-415, scribe.position()[1]+100)
        i += 1

    scribe.goto(-395, -415)

    while i < 16:
        scribe.write(labels[i], font=("Montserrat", 12, "bold"))
        scribe.goto(scribe.position()[0]+100, -415)
        i += 1

def initialise_tiles(): # now im adding a sprite to each tile so I can change it depending on the tile's state during a game e.g. selected by user

    spots = ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
            "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
            "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
            "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",]
    
    sprites = []

    for spot in spots:
        sprite = turtle.Turtle()
        sprite.ht()
        sprites.append(sprite)
    
    tiles = dict(zip(spots, sprites))






def draw_board(board_state):
    
    # Tell all pieces to move to designated positions

    for i in range(len(board_state)):
        t = board_state[i][0]
        t.speed(0)
        t.pu()
        t.goto(handlers.tiletocoord(board_state[i][1]))


