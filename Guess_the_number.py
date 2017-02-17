# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

global r, n
r = 100
n =7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here

    # remove this when you add your code    
    global secret_number
    num = random.randrange(0,r)
    secret_number = num
    
    if r == 100:
        n = 7
    elif r == 1000:
        n = 10
    
    print "New game. Range is from 0 to",r
    print "Number of remaining guesses is",n
    print


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code  
    global n, r
    r = 100
    n = 7
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global n, r
    r = 1000
    n = 10
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    
    # remove this when you add your code
    global n
    tmp = int(guess)
    print "Guess was " + guess

    if n > 0:
        if tmp > secret_number:
            print "Lower!"
            n -= 1
            print "Number of remaining guesses is",n
            print
        elif tmp < secret_number:
            print "Higher!"
            n -= 1
            print "Number of remaining guesses is",n
            print
        else:
            print "Correct"
            print
            new_game()
    else:
        print "You ran out of guesses. The number was",secret_number
        print
        new_game()
            
# create frame
frame = simplegui.create_frame('Guess the number', 300, 300, 300)

# register event handlers for control elements and start frame
input_field = frame.add_input('Input Guess', input_guess, 50)
range1_button = frame.add_button('Range: 0 - 100', range100, 50)
range2_button = frame.add_button('Range: 0 - 1000', range1000, 50)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
