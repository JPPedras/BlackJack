import utils
import time
import random as rd

cards=['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

print('Welcome to BlackJack!')
print("Let's start!\n")

player_hand=[cards[rd.randint(0,13)]]
print('Your Hand:')
utils.draw_cards(player_hand)
print('')
time.sleep(2)
dealer_hand=[cards[rd.randint(0,13)]]
print("Dealer's Hand:")
utils.draw_cards(dealer_hand)

    