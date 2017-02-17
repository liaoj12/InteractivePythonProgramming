# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
previous = False

#messages
play_options = 'Hit or stand?'
again = 'New deal?'
lose1 = 'You lose'
lose2 = 'You went bust and lose'
lose3 = 'You have busted'
win = 'You win'

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []
        
    def __str__(self):
        # return a string representation of a hand
        ans = ''
        for c in self.hand:
            ans = ans + c.suit + c.rank + ' '
        return ans
        
    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        num = 0
        for c in self.hand:
            if 'A' == c.rank:
                num += 1
            value += VALUES[c.rank]
                
        if num > 0:
            if value + 10 <= 21:
                return value + 10
            else:
                return value
        else:
            return value
        
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        card_loc = (CARD_CENTER[0], 
                    CARD_CENTER[1])
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)        
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))
        
    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)
        
    def deal_card(self):
        # deal a card object from the deck
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card
    
    def __str__(self):
        # return a string representing the deck
        ans = ''
        for c in self.deck:
            ans = ans + c.suit + c.rank + ' '
        return ans

#define event handlers for buttons
def deal():
    global outcome, in_play, score  
    
    if in_play:
        score -= 1

    # your code goes here
    global deck, player, dealer
    deck = Deck()
    player = Hand()
    dealer = Hand()
    
    deck.shuffle()
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
        
    in_play = True

def hit():
    # replace with your code below
    global in_play, outcome, deck, player, score, dealer, previous
    # if the hand is in play, hit the player
    if in_play:
        if player.get_value() <= 21:
            player.add_card(deck.deal_card())
            if player.get_value() > 21:
                outcome = "You have busted"
                score -= 1
                while dealer.get_value() < 17:
                    dealer.add_card(deck.deal_card())
                    in_play = False
                
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # replace with your code below
    global outcome, score, dealer, deck, in_play, previous
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            outcome = "Player wins"
            score += 1
        else:
            if dealer.get_value() >= player.get_value():
                outcome = lose1
                score -= 1
            else:
                outcome = win
                score += 1
        in_play = False
        
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Blackjack', [100, 100], 50, 'Aqua')
    canvas.draw_text('Score ' + str(score), [400, 100], 30, 'Black')
    canvas.draw_text('Dealer', [100, 150], 30, 'Black')
    canvas.draw_text('Player', [100, 350], 30, 'Black')
    
    i = 0
    for c in player.hand:
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(c.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(c.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [100 + CARD_CENTER[0] + (CARD_SIZE[0]+ 20) * i, 400 + CARD_CENTER[1]], CARD_SIZE)
        i += 1
        
    dealer.hand[0].draw(canvas, [100 + CARD_SIZE[0] + 20, 190])
    if in_play:    
        canvas.draw_text(play_options, [300, 350], 25, 'Black')
        canvas.draw_image(card_back, (CARD_BACK_CENTER[0] + CARD_BACK_SIZE[0], CARD_BACK_CENTER[1]), CARD_BACK_SIZE, [100 + CARD_BACK_CENTER[0], 190 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)      
    else:
        canvas.draw_text(again, [300, 350], 25, 'Black')
        canvas.draw_text(outcome, [350, 150], 25, 'Black')
        i = 0
        for c in dealer.hand:
            if i != 0:
                if i == 1:
                    card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(c.rank), 
                                CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(c.suit))
                    canvas.draw_image(card_images, card_loc, CARD_SIZE, [100 + CARD_CENTER[0], 190 + CARD_CENTER[1]], CARD_SIZE)	
                else:
                    card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(c.rank), 
                                CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(c.suit))
                    canvas.draw_image(card_images, card_loc, CARD_SIZE, [100 + CARD_CENTER[0] + (CARD_SIZE[0]+ 20) * i, 190 + CARD_CENTER[1]], CARD_SIZE)
            i += 1

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")
    
#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
