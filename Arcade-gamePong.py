# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == LEFT:
        ball_vel = [-random.randrange(3, 10), -random.randrange(3, 10)]
    elif direction == RIGHT:
        ball_vel = [random.randrange(3, 10), -random.randrange(3, 10)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = [0, HEIGHT / 2]
    paddle2_pos = [WIDTH, HEIGHT / 2]
    paddle1_vel = 0 
    paddle2_vel = 0
    spawn_ball(random.choice([LEFT, RIGHT]))

    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
     
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_pos[1] = BALL_RADIUS
        ball_vel[1] = -1 * ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_pos[1] = HEIGHT - BALL_RADIUS
        ball_vel[1] = -1 * ball_vel[1]
        
    if ball_pos[0] <= PAD_WIDTH:
        if not(paddle1_pos[1] - PAD_HEIGHT / 2 <= ball_pos[1] <= paddle1_pos[1] + PAD_HEIGHT / 2):
            spawn_ball(RIGHT)
            score2 = score2 + 1
        else:
            ball_vel[0] = -ball_vel[0]
    if ball_pos[0] >= WIDTH - PAD_WIDTH:
        if not(paddle2_pos[1] - PAD_HEIGHT / 2 <= ball_pos[1] <= paddle2_pos[1] + PAD_HEIGHT / 2):
            spawn_ball(LEFT)
            score1 = score1 + 1
        else:
            ball_vel[0] = -ball_vel[0]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 8, 'White')
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    
    if paddle1_pos[1] <= PAD_HEIGHT / 2:
        paddle1_pos[1] = PAD_HEIGHT / 2
    if paddle1_pos[1] >= HEIGHT - PAD_HEIGHT / 2:
        paddle1_pos[1] = HEIGHT - PAD_HEIGHT / 2
        
    if paddle2_pos[1] <= PAD_HEIGHT / 2:
        paddle2_pos[1] = PAD_HEIGHT / 2
    if paddle2_pos[1] >= HEIGHT - PAD_HEIGHT / 2:
        paddle2_pos[1] = HEIGHT - PAD_HEIGHT / 2
        
    # draw paddles
    canvas.draw_line([paddle1_pos[0], paddle1_pos[1] - PAD_HEIGHT / 2], [paddle1_pos[0], paddle1_pos[1] + PAD_HEIGHT / 2], PAD_WIDTH, 'White')
    canvas.draw_line([paddle2_pos[0], paddle2_pos[1] - PAD_HEIGHT / 2], [paddle2_pos[0], paddle2_pos[1] + PAD_HEIGHT / 2], PAD_WIDTH, 'White')
    
    # draw scores
    canvas.draw_text(str(score1), (250, 50), 50, 'White')
    canvas.draw_text(str(score2), (350, 50), 50, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -15
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -15
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 15
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 15
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 15
    
def button():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', button)

# start frame
new_game()
frame.start()
