# implementation of card game - Memory

import simplegui
import random

global turn

# helper function to initialize globals
def new_game():
    global deck, turn, state, mem, exposed
    exposed = [False,False,False,False,False,False,False,False,
               False,False,False,False,False,False,False,False,]
    mem = [0, 0]
    state = 0
    turn = 0
    deck = range(0, 8) + range(0, 8)
    random.shuffle(deck)
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, mem, turn
    if state == 0:
        state = 1
        turn += 1
        i = pos[0] // 50
        mem[0] = i
        exposed[i] = True
    elif state == 1:
        i = pos[0] // 50
        if i != mem[0]:
            mem[1] = i
            exposed[i] = True
            state = 2
    else:
        i = pos[0] // 50
        if i != mem[0] and i != mem[1]:
            if deck[mem[0]] != deck[mem[1]]:
                exposed[mem[0]] = False
                exposed[mem[1]] = False
            mem[0] = i
            exposed[i] = True
            state = 1
            turn += 1
    label.set_text("Turns = " + str(turn))
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    i = 1
    for card in deck:
        if exposed[i - 1]:
            canvas.draw_text(str(card), [(i-1) * 50 + 10, 65], 50, 'White')
        else:
            canvas.draw_polygon([((i - 1) * 50, 0),
                             ((i - 1) * 50, 100),
                             (i * 50, 100),
                             (i * 50, 0)], 5, 'Red', 'Green')
        i += 1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label('Turns = 0')

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric