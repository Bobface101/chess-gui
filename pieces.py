import turtle, handlers
from screen import screen
from board_state import board_state

def initialise_pieces():

    global board_state

    # importing sprites for all pieces
    screen.addshape('assets/bp.gif')
    screen.addshape('assets/bn.gif')
    screen.addshape('assets/bb.gif')
    screen.addshape('assets/br.gif')
    screen.addshape('assets/bq.gif')
    screen.addshape('assets/bk.gif')

    screen.addshape('assets/wp.gif')
    screen.addshape('assets/wn.gif')
    screen.addshape('assets/wb.gif')
    screen.addshape('assets/wr.gif')
    screen.addshape('assets/wq.gif')
    screen.addshape('assets/wk.gif')

    # Initialising pieces

    # White

    wpa = turtle.Turtle()
    wpa.shape("assets/wp.gif")

    wpb = turtle.Turtle()
    wpb.shape("assets/wp.gif")

    wpc = turtle.Turtle()
    wpc.shape("assets/wp.gif")

    wpd = turtle.Turtle()
    wpd.shape("assets/wp.gif")

    wpe = turtle.Turtle()
    wpe.shape("assets/wp.gif")

    wpf = turtle.Turtle()
    wpf.shape("assets/wp.gif")

    wpg = turtle.Turtle()
    wpg.shape("assets/wp.gif")

    wph = turtle.Turtle()
    wph.shape("assets/wp.gif")

    wn1 = turtle.Turtle()
    wn1.shape("assets/wn.gif")

    wn2 = turtle.Turtle()
    wn2.shape("assets/wn.gif")

    wb1 = turtle.Turtle()
    wb1.shape("assets/wb.gif")

    wb2 = turtle.Turtle()
    wb2.shape("assets/wb.gif")

    wr1 = turtle.Turtle()
    wr1.shape("assets/wr.gif")

    wr2 = turtle.Turtle()
    wr2.shape("assets/wr.gif")

    wq = turtle.Turtle()
    wq.shape("assets/wq.gif")

    wk = turtle.Turtle()
    wk.shape("assets/wk.gif")

    # Black

    bpa = turtle.Turtle()
    bpa.shape("assets/bp.gif")

    bpb = turtle.Turtle()
    bpb.shape("assets/bp.gif")

    bpc = turtle.Turtle()
    bpc.shape("assets/bp.gif")

    bpd = turtle.Turtle()
    bpd.shape("assets/bp.gif")

    bpe = turtle.Turtle()
    bpe.shape("assets/bp.gif")

    bpf = turtle.Turtle()
    bpf.shape("assets/bp.gif")

    bpg = turtle.Turtle()
    bpg.shape("assets/bp.gif")

    bph = turtle.Turtle()
    bph.shape("assets/bp.gif")

    bn1 = turtle.Turtle()
    bn1.shape("assets/bn.gif")

    bn2 = turtle.Turtle()
    bn2.shape("assets/bn.gif")

    bb1 = turtle.Turtle()
    bb1.shape("assets/bb.gif")

    bb2 = turtle.Turtle()
    bb2.shape("assets/bb.gif")

    br1 = turtle.Turtle()
    br1.shape("assets/br.gif")

    br2 = turtle.Turtle()
    br2.shape("assets/br.gif")

    bq = turtle.Turtle()
    bq.shape("assets/bq.gif")

    bk = turtle.Turtle()
    bk.shape("assets/bk.gif")

    board_state = [[wpa, "a2"], [wpb, "b2"], [wpc, "c2"], [wpd, "d2"], [wpe, "e2"], [wpf, "f2"], [wpg, "g2"], [wph, "h2"],
                     [wn1, "b1"], [wn2, "g1"], [wb1, "c1"], [wb2, "f1"], [wr1, "a1"], [wr2, "h1"], [wq, "d1"], [wk, "e1"],
                     
                     [bpa, "a7"], [bpb, "b7"], [bpc, "c7"], [bpd, "d7"], [bpe, "e7"], [bpf, "f7"], [bpg, "g7"], [bph, "h7"],
                     [bn1, "b8"], [bn2, "g8"], [bb1, "c8"], [bb2, "f8"], [br1, "a8"], [br2, "h8"], [bq, "d8"], [bk, "e8"]]
    
    return board_state
