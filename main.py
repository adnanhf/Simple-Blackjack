'''
This file would written as exercise
to mastering python. This file would
always be overwritten.
'''

import random
from os import system

'''
Our Blackjack House Rules:
- The deck is unlimited in size. 
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The the Ace can count as 11 or 1.
- Cards 2-9 count as it is.
- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The player options for playing is only Hit or Stand.
- Other basic applied rules can be seen here:
  https://bicyclecards.com/how-to-play/blackjack/
'''

#Draw logo for our simple interface
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

#Created 2nd
def deal_card():
    """
    Randomly return a card from deck.
    Deck values related to card value.
    (2-9 card, Jack/Queen/King are 10, and Ace is 11).
    """
    deck = [i for i in range(2,12)]
    card = random.choice(deck)
    return card

#Created 3rd
def calculate_score(cards):
    #Take list of cards and return the score
    
    '''
    Quick notes:
    To represent a Blackjack, if the list
    consist of an ace and a face card, score would
    returned 0
    '''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    '''
    Quick notes:
    If in the first draw user's score gets 
    over 21 and user have an ace, it counts as 1
    '''
    if 11 in cards and len(cards) == 2 and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    '''
    Quick notes:
    In a function, if the first 'return' work,
    it would break--get out from--the function
    in this specific case: line 58
    '''
    return sum(cards)

#Created 4th
def compare(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    elif user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, the opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    elif computer_score > user_score:
        return "You lose 😤"

#Created 1st
def play_game():
    #This is the main function.

    print(logo)

    user_cards, computer_cards = [],[]
    is_game_over = False

    #Step 1: Give both sides two random cards
    for _ in range(2):
        '''
        Quick notes:
        When you are not interested in some
        values returned by a function/for loop
        use '_' in place of variable name

        in this specific case, the loop should
        just run some specific number of times.
        '''
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        #Step 2: calculate both side score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        #Step 3: Check both side cards score for the first time
        
        '''
        Quick notes:
        If the computer or the user has a blackjack
        (score 0) or if the user's score is over 21,
        then the game ends.
        '''
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            #Step 3: User has always the option to Hit or Stand
            
            '''
            More info:
            If the game has not ended, ask the user
            if they want to draw another card. If 'yes',
            then use the deal_card() function to add
            another card to the user_cards List. If 'no',
            then the game has ended.
            '''
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
              user_cards.append(deal_card())
            else:
              is_game_over = True
    
    #Step 4: Computer's turn

    '''
    Quick notes:
    The computer should keep drawing cards as long
    as it has a score less than 17. This decision
    are automatic on all plays
    '''
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    #Step 5: Show both side cards
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score:{computer_score}")

    #Step 6: Show the game result
    print(compare(user_score, computer_score))

'''
Optional Step: Ask the user if they want to restart the game.
If they answer yes, clear the console and start a new game
of blackjack and show the logo again.
'''
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  '''
  Quick notes:
  Pay attention where you're gonna run the code!
  if in windows, use system('cls')
  if in linux/mac, use system('clear')

  in this specific case, we run it in windows
  '''
  system('cls')
  play_game()
