def draw_cards(hand):
    for card in hand:
        print('_____ ', end='')
    print('')
    for card in hand:
        print('|   | ', end='')
    print('')
    for card in hand:
        print(f'| {card} | ', end='')
    print('')
    for card in hand:
        print('|___| ', end='')
    print('') 

