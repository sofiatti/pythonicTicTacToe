import pygame
from pygame.locals import *

green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic Tac Toe with Pygame')
pygame.init()

def introScreen():
    #Do I need to turn run = True off at some point?
    messages = []
    run = True
    while run:
        gameDisplay.fill(black)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_k:
                    pygame.quit()
                    sys.exit()
                if event.key == K_p:
                    tic_tac_toe()
                # if event.key == K_m:
                #     VolumeControl()

        messages.append(("Pythonic Tic Tac Toe", 100))
        messages.append(("Press p to Play", 350))

        for message in messages:
            font = pygame.font.Font(None, 100)
            text = font.render(message[0], 1, green)
            textpos = text.get_rect()
            textpos.centerx = gameDisplay.get_rect().centerx
            textpos.y = message[1]
            gameDisplay.blit(text, textpos)

        pygame.display.update()



    #Welcome to Pythonic Tic Tac Toe
    #Click Start to Play or Quit to Exit
    #2 Boxes - Start Quit
    print "This is a test of the intro function"
    # tic_tac_toe()    

def drawGrid():
    pygame.draw.line(gameDisplay, green, (120, 240), (480, 240), 10) #X, y - Top 
    pygame.draw.line(gameDisplay, green, (120, 360), (480, 360), 10) #X, y - Bottom
    
    
    pygame.draw.line(gameDisplay, green, (240, 120), (240, 480), 10) #x, Y - Left
    pygame.draw.line(gameDisplay, green, (360, 120), (360, 480), 10) #x, Y - Right

def draw_symbol(current_player, play):
    #Testing Purposes Only
    # current_player = "X"


    if current_player == "X":
        if play == 1:  #For Future: Use Blit instead of Square & do in non-naive way
            pygame.draw.line(gameDisplay, green, (130, 230), (230, 130), 10)
            pygame.draw.line(gameDisplay, green, (230, 230), (130, 130), 10)
        if play == 2:
            pygame.draw.line(gameDisplay, green, (250, 230), (350, 130), 10)
            pygame.draw.line(gameDisplay, green, (350, 230), (250, 130), 10)
        if play == 3:
            pygame.draw.line(gameDisplay, green, (370, 230), (470, 130), 10)
            pygame.draw.line(gameDisplay, green, (470, 230), (370, 130), 10)
        if play == 4:
            pygame.draw.line(gameDisplay, green, (130, 350), (230, 250), 10)
            pygame.draw.line(gameDisplay, green, (230, 350), (130, 250), 10)
        if play == 5:
            pygame.draw.line(gameDisplay, green, (250, 350), (350, 250), 10)
            pygame.draw.line(gameDisplay, green, (350, 350), (250, 250), 10)
        if play == 6:
            pygame.draw.line(gameDisplay, green, (370, 350), (470, 250), 10)
            pygame.draw.line(gameDisplay, green, (470, 350), (370, 250), 10)
        if play == 7:
            pygame.draw.line(gameDisplay, green, (130, 470), (230, 370), 10)
            pygame.draw.line(gameDisplay, green, (230, 470), (130, 370), 10)
        if play == 8:
            pygame.draw.line(gameDisplay, green, (250, 470), (350, 370), 10)
            pygame.draw.line(gameDisplay, green, (350, 470), (250, 370), 10)
        if play == 9:
            pygame.draw.line(gameDisplay, green, (370, 470), (470, 370), 10)
            pygame.draw.line(gameDisplay, green, (470, 470), (370, 370), 10)

    

    if current_player == "O":

        if play == 1:  #For Future: Use Blit instead of Square & do in non-naive way
            pygame.draw.circle(gameDisplay, green, (180, 180), 50, 10)
        if play == 2:  
            pygame.draw.circle(gameDisplay, green, (300, 180), 50, 10)
        if play == 3:  
            pygame.draw.circle(gameDisplay, green, (420, 180), 50, 10)
        if play == 4:  
            pygame.draw.circle(gameDisplay, green, (180, 300), 50, 10)
        if play == 5:  
            pygame.draw.circle(gameDisplay, green, (300, 300), 50, 10)
        if play == 6:  
            pygame.draw.circle(gameDisplay, green, (420, 300), 50, 10)
        if play == 7:  
            pygame.draw.circle(gameDisplay, green, (180, 420), 50, 10)
        if play == 8:  
            pygame.draw.circle(gameDisplay, green, (300, 420), 50, 10)
        if play == 9:  
            pygame.draw.circle(gameDisplay, green, (420, 420), 50, 10)



def draw(board):
    print '\n'
    print '  Game     Key'
    print ' ' + board[1] + '|' + board[2] + '|' + board[3] + '     1|2|3'
    print ' - - -    - - -'
    print ' ' + board[4] + '|' + board[5] + '|' + board[6] + '     4|5|6'
    print ' - - -    - - -'
    print ' ' + board[7] + '|' + board[8] + '|' + board[9] + '     7|8|9'
    print '\n'

def check_if_won(board):
    for p in ["X", "O"]:
        possibilities = [
            #Consecutive line
            board[1:4], board[4:7], board[7:10],
            #Consecutive Row:
            board[1::3], board[2::3], board[3::3],
            #Consecutive Diagonals:
            board[1::5], board[3::2]
            ]

        for element in possibilities:
            if element == [p,p,p]:
                return p
    return False

def get_move(symbol, board):
    instructions = "You are " + symbol + ". Please enter your play [1-9]: "
    play = int(raw_input(instructions))  ##Just use input
    while board[play] != ' ':
        print 'Oops!  That\'s taken!  Try again...'
        play = int(raw_input(instructions))
    else:
        return play


def other_player(current_player):
    if current_player == "X":
        return "O"
    elif current_player == "O":
        return "X"

def tic_tac_toe():
    print 'Welcome to Tic-Tac-Toe! '

    drawGrid()
    board = [' '] * 10
    draw(board)
    current_player = "X"

    gameDisplay.fill(black)

    while ' ' in board:
        drawGrid()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_k:
                    pygame.quit()
                    sys.exit()
                if event.key == K_1 or event.key == K_KP1:
                    play_choice = 1

        play_choice = get_move(current_player, board)

        board[play_choice] = current_player
        draw(board)
        draw_symbol(current_player, play_choice)
        p = check_if_won(board)
        if p:
            print 'Game Over! %s won!!!' %p
        else:
            print 'Whomp whomp, it\'s a tie!'
        current_player = other_player(current_player)

        pygame.display.update()

if __name__ == "__main__":
    introScreen()
    # tic_tac_toe()
