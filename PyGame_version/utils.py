def draw_cards(hand):
    for card in hand:
        print('_____ ', end='')
    print('')
    for card in hand:
        print('|   | ', end='')
    print('')
    for card in hand:
        if card != 10:
            print(f'| {card} | ', end='')
        else:
            print(f'| {card}| ', end='')
    print('')
    for card in hand:
        print('|___| ', end='')
    print('')

def get_score(hand):
    score1=0
    score2=0
    for card in hand:
        if card == 'A':
            score1 += 11
            score2 += 1
        elif type(card) == int:
            score1 += card
            score2 += card
        else:
            score1 += 10
            score2 += 10
    if score1 > 21:
        return score2
    else:
        return score1

    

