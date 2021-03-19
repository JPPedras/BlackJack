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
    scores=[0]
    for card in hand:
        if card[0] == 'A':
            scores.append(scores[len(scores)-1]+1)
            for i in range(len(scores)-1):
                scores[i]+=11
        elif card[0].isdigit()==False or card[1]=='0':
            for i in range(len(scores)):
                scores[i]+=10
        else:
            for i in range(len(scores)):
                scores[i]+=int(card[0])
    for score in scores:
        if score<=21:
            return score

    return scores[len(scores)-1]

def draw_result(text):
    WIN.blit(ARIAL_FONT.render(text, 1, WHITE), (300, HEIGHT/2))
    pygame.display.update()
    pygame.time.delay(5000)


def manage_bet(op,bet,balance):
    if op == 1 and bet < balance:
        bet += 5
    elif op == -1 and bet > 0:
        bet -= 5
    return bet


def draw_window(player_hand,dealer_hand,balance,bet):
    WIN.fill(TEAL)

    balance_text = ARIAL_FONT.render("Balance: " + str(balance), 1, WHITE)
    bet_text = ARIAL_FONT.render("Bet:     " + str(bet), 1, WHITE)
    WIN.blit(balance_text,(10,10))
    WIN.blit(bet_text,(5,250))
    WIN.blit(pygame.transform.scale(pygame.image.load(os.path.join('Assets/Buttons','stand.png')),(100,100)),(10,400))
    WIN.blit(pygame.transform.scale(pygame.image.load(os.path.join('Assets/Buttons','hit.png')),(100,100)),(120,395))
    WIN.blit(pygame.transform.scale(pygame.image.load(os.path.join('Assets/Buttons','add.png')),(50,50)),(83,190))
    WIN.blit(pygame.transform.scale(pygame.image.load(os.path.join('Assets/Buttons','subtract.png')),(50,50)),(83,290))

    x=300
    for card in player_hand:
        WIN.blit(pygame.image.load(os.path.join('Assets/Cards',f'{card}.png')),(x,350))
        x+=100
    x=300
    for card in dealer_hand:
        WIN.blit(pygame.image.load(os.path.join('Assets/Cards',f'{card}.png')),(x,30))
        x+=100
    pygame.display.update()

def setup(player_hand,dealer_hand):

    player_hand.append(values[random.randint(0,12)] + suits[random.randint(0,3)])
    WIN.blit(pygame.image.load(os.path.join('Assets/Cards',f'{player_hand[0]}.png')),(300,350))
    pygame.time.delay(1000)
    pygame.display.update()

    dealer_hand.append(values[random.randint(0,12)] + suits[random.randint(0,3)])
    WIN.blit(pygame.image.load(os.path.join('Assets/Cards',f'{dealer_hand[0]}.png')),(300,30))
    pygame.time.delay(1000)
    pygame.display.update()

    player_hand.append(values[random.randint(0,12)] + suits[random.randint(0,3)])
    WIN.blit(pygame.image.load(os.path.join('Assets/Cards',f'{player_hand[1]}.png')),(400,350))
    pygame.time.delay(1000)
    pygame.display.update()

    dealer_hand.append('?')
    WIN.blit(pygame.image.load(os.path.join('Assets/Cards',f'{dealer_hand[1]}.png')),(400,30))
    pygame.time.delay(1000)
    pygame.display.update()

    return(player_hand,dealer_hand)




def main(balance):


    clock=pygame.time.Clock()
    run=True
    bet = 0
    player_hand=list()
    dealer_hand=list()
    done=0
    settedup=0

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if 10 <= mouse[0] and mouse[0] <= 110 and 400 <= mouse[1] and mouse[1] <= 500 and settedup == 1:
                    dealer_hand[1]=(values[random.randint(0,12)] + suits[random.randint(0,3)])
                    draw_window(player_hand,dealer_hand,balance,bet)
                    pygame.time.delay(1000)
                    done=1
                    while get_score(dealer_hand) < 17:
                        dealer_hand.append(values[random.randint(0,12)] + suits[random.randint(0,3)])
                        draw_window(player_hand,dealer_hand,balance,bet)
                        pygame.time.delay(1000)
                if 120 <= mouse[0] and mouse[0] <= 220 and 395 <= mouse[1] and mouse[1] <= 495:
                    if len(player_hand) == 0 and bet != 0:
                        settedup = 1
                        (player_hand,dealer_hand)=setup(player_hand,dealer_hand)
                    elif bet != 0 and len(player_hand) >= 2:
                        player_hand.append(values[random.randint(0,12)] + suits[random.randint(0,3)])
                if 83 <= mouse[0] and mouse[0] <= 133 and 190 <= mouse[1] and mouse[1] <= 240 and len(player_hand)==0:
                    bet=manage_bet(1,bet,balance)
                if 83 <= mouse[0] and mouse[0] <= 133 and 290 <= mouse[1] and mouse[1] <= 340 and len(player_hand)==0:
                    bet=manage_bet(-1,bet,balance)

        draw_window(player_hand,dealer_hand,balance,bet)



        result_text=''   
        if get_score(player_hand) == 21:
            result_text='BLACKJACK!!!'
            balance += bet
            bet=0       
        elif get_score(player_hand) > 21:
            result_text='YOU BUSTED!'
            balance -= bet
            bet=0
        elif get_score(dealer_hand) > 21:
            result_text='DEALER BUSTED! YOU WON'
            balance += bet
            bet=0  
        elif get_score(player_hand) > get_score(dealer_hand) and done == 1:
            result_text='YOU WON!'
            balance += bet
            bet=0 
        elif get_score(player_hand) < get_score(dealer_hand) and done == 1:
            result_text='DEALER WON!'
            balance -= bet
            bet=0
        elif get_score(player_hand) == get_score(dealer_hand) and done == 1:
            result_text='DRAW!'
            bet=0

        if result_text != '':
            draw_result(result_text)
            break

        mouse = pygame.mouse.get_pos() 



    if balance <= 0:
        draw_window(player_hand,dealer_hand,balance,bet)
        draw_result('GAME OVER!')
        pygame.quit()
    main(balance)


if __name__=='__main__':
    main(100)


    