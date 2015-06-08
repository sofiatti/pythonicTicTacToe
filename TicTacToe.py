def game_and_keys(board):
    print '\n'
    print '  Game     Key'
    print ' ' + board[0] + '|' + board[1] + '|' + board[2] + '     0|1|2'
    print ' - - -    - - -'
    print ' ' + board[3] + '|' + board[4] + '|' + board[5] + '     3|4|5'
    print ' - - -    - - -'
    print ' ' + board[6] + '|' + board[7] + '|' + board[8] + '     6|7|8'
    print '\n'

def check_if_won(board):
    for p in ["X", "O"]:
        possibilities = [
            #Consecutive line
            board[0:3], board[3:6], board[6:9],
            #Consecutive Row:
            board[0::3], board[1::3], board[2::3],
            #Consecutive Diagonals:
            board[0::4], board[2::2]
            ]

        for element in possibilities:
            if element == [p,p,p]:
                return p
    return False

def get_move(symbol, board):
    instructions = "You are " + symbol + ". Please enter your play [0-8]: "
    play = int(raw_input(instructions))
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
    '''
    Play Tic-Tac-Toe!

    Parameters:
    '''
    print 'Welcome to Tic-Tac-Toe! '

    board = [' ' for x in range(9)]
    game_and_keys(board)
    current_player = "X"
    while ' ' in board:
        board[get_move(current_player, board)] = current_player
        game_and_keys(board)
        p = check_if_won(board)
        if p:
                print 'Game Over! %s won!!!' %p
        current_player = other_player(current_player)
    else:
        print 'Whomp whomp, it\'s a tie!'

tic_tac_toe()
