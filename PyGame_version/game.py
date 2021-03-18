import os, pygame, random, sys, time
pygame.font.init()

WIDTH, HEIGHT = 900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
ARIAL_FONT = pygame.font.SysFont('DroidSans', 40)


pygame.display.set_caption('BlackJack')

FPS = 60
TEAL=(0,128,128)
WHITE=(255,255,255)
values=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits=['S','C','H','D']

def get_score(hand):
    score1=0
    score2=0
    for card in hand:
        if card[0] == 'A':
            score1 += 11
            score2 += 1
        elif type(card[0]) != int or card[1]=='0':
            score1 += 10
            score2 += 10
        else:
            score1 += int(card[0])
            score2 += int(card[0])
    if score1 > 21:
        return score2
    else:
        return score1


def draw_window(player_hand,dealer_hand,balance):
    WIN.fill(TEAL)

    balance_text = ARIAL_FONT.render("Balance: " + str(balance), 1, WHITE)
    WIN.blit(balance_text,(10,10))

    x=300
    for card in player_hand:
        WIN.blit(pygame.image.load(os.path.join('Assets/Cards',f'{card}.png')),(x,350))
        x+=100
    x=300
    for card in dealer_hand:
        WIN.blit(pygame.image.load(os.path.join('Assets/Cards',f'{card}.png')),(x,30))
        x+=100
    pygame.display.update()

def main():


    clock=pygame.time.Clock()
    run=True
    balance=100

    player_hand=[values[random.randint(0,12)] + suits[random.randint(0,3)]]
    dealer_hand=[values[random.randint(0,12)] + suits[random.randint(0,3)]]

    draw_window(player_hand,dealer_hand,balance)
    player_hand.append(values[random.randint(0,12)] + suits[random.randint(0,3)])
    dealer_hand.append('?')

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

        draw_window(player_hand,dealer_hand,balance)



    pygame.quit()


if __name__=='__main__':
    main()


    