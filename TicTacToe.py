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
            board[1::4], board[3::2]
            ]

        for element in possibilities:
            if element == [p,p,p]:
                return p
    return False

def get_move(symbol, board):
    instructions = "You are " + symbol + ". Please enter your play [1-9]: "
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
    print 'Welcome to Tic-Tac-Toe! '

    board = [' '] * 10
    draw(board)
    current_player = "X"
    while ' ' in board:
        board[get_move(current_player, board)] = current_player
        draw(board)
        p = check_if_won(board)
        if p:
            print 'Game Over! %s won!!!' %p
        current_player = other_player(current_player)
    else:
        print 'Whomp whomp, it\'s a tie!'

tic_tac_toe()
