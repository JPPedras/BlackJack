import utils
import time
import sys
import random as rd

cards=['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

print('Welcome to BlackJack!')
print("Let's start!\n")

player_hand=[cards[rd.randint(0,12)]]
print('Your Hand:')
utils.draw_cards(player_hand)
print('')
time.sleep(2)

dealer_hand=[cards[rd.randint(0,12)]]
print("Dealer's Hand:")
utils.draw_cards(dealer_hand)
print('')
time.sleep(2)

player_hand.append(cards[rd.randint(0,12)])
print('Your Hand:')
utils.draw_cards(player_hand)
print('')
time.sleep(2)

if utils.get_score(player_hand) == 21:
    print('YOU GOT BLACKJACK AND WON!')
    sys.exit()

dealer_hand.append('?')
print("Dealer's Hand:")
utils.draw_cards(dealer_hand)
print('')

    
choice=input("'H' to hit or 'S' to stand: ")
while choice == 'H':

    player_hand.append(cards[rd.randint(0,12)])
    print('Your Hand:')
    utils.draw_cards(player_hand)
    print('')
    time.sleep(2)

    if utils.get_score(player_hand) > 21:
        print('You Busted! Game Over!')
        sys.exit()

    choice=input("'H' to hit or 'S' to stand: ")

time.sleep(2)
dealer_hand[1]=cards[rd.randint(0,12)]
print("Dealer's Hand:")
utils.draw_cards(dealer_hand)
print('')
time.sleep(2)

while utils.get_score(dealer_hand) < 17:

    dealer_hand.append(cards[rd.randint(0,12)])
    print("Dealer's Hand:")
    utils.draw_cards(dealer_hand)
    print('')
    time.sleep(2)

if utils.get_score(dealer_hand) > 21:
        print('Dealer Busted! YOU WON!')
        sys.exit()

time.sleep(2)
if utils.get_score(player_hand) > utils.get_score(dealer_hand):
    print('YOU WON! GONGRATS')
elif utils.get_score(player_hand) < utils.get_score(dealer_hand):
    print('YOU LOST! GAME OVER!')
else:
    print("IT'S A DRAW!")

    