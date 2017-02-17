# template for "Stopwatch: The Game"

import simplegui

# define global variables
global integer, A, B, C, D, x, y, check
integer = 0
x = 0
y = 0
check = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A, B, C, D
    A = 0
    B = 0
    C = 0
    D = 0

    D = t % 10
    t = t - D
    if t == 0:
        return str(A) + ':' + str(B) + str(C) + '.' + str(D)
    else:
        C = t / 10 % 60 % 10
        t = t - C * 10
        if t == 0:
            return str(A) + ':' + str(B) + str(C) + '.' + str(D)
        else:
            B = t / 10 % 60 / 10
            t = t - B * 100
            if t == 0:
                return str(A) + ':' + str(B) + str(C) + '.' + str(D)
            else:
                A = t / 600
                return str(A) + ':' + str(B) + str(C) + '.' + str(D)
    
def counter():
    return str(x) + '/' + str(y)  

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    global check
    check = True

def stop():
    timer.stop()
    global x, y, check
    if check:
        y = y + 1
        if D == 0:
            x = x + 1
    
    check = False

def reset():
    timer.stop()
    global integer, x, y
    integer = 0
    x = 0
    y = 0
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global integer
    integer = integer + 1
    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(integer), (80, 150), 60 , 'Red')
    canvas.draw_text(counter(), (250, 30), 30, 'Green')

# create frame
frame = simplegui.create_frame('Stop Watch Game', 300, 300, 300)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
start_button = frame.add_button('Start', start, 50)
stop_button = frame.add_button('Stop', stop, 50)
reset_button = frame.add_button('Reset', reset, 50)

# start frame
frame.start()

# Please remember to review the grading rubric