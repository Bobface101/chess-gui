import turtle
from screen import screen

# misc. functions which make everything run well

def get_board_state():

    from board_state import board_state
    return board_state

def send_board_state(new_state):

    import board_state
    board_state.board_state = new_state

def find_piece_on(tile):
    
    board_state = dict([[pair[1], pair[0]] for pair in get_board_state()])

    try:
        return board_state[tile]
    
    except:
        return None


def tiletocoord(tilecoord):

    # translates a tile name "h6" into coordinates for the piece to move to x,y

    columns = {"a":-350,"b":-250,"c":-150,"d":-50,"e":50,"f":150,"g":250,"h":350}
    
    return (columns[tilecoord[0]],(100*int(tilecoord[1])-450))

def roughcoordtotile(x,y):

    # translates the rough click of the player x,y into a tile name "e4"

    columns = {-400:"a", -300:"b", -200:"c", -100:"d", 0:"e", 100:"f", 200:"g", 300:"h"}

    column = columns[round(x-50, -2)]
    row = round((y+450)/100)

    return str(column)+str(row)

