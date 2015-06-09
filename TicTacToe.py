def draw(board):
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

corners = [1,3,7,9]
middle = [5]

def get_move(symbol, board):
    instructions = "You are " + symbol + ". Please enter your play [0-8]: "
    play = int(raw_input(instructions))
    while board[play] != ' ':
        print 'Oops!  That\'s taken!  Try again...'
        play = int(raw_input(instructions))
    else:
        return play

def get_bot_move(current_player, board):
    hypothetical_board = list(board)
    for idx, item in enumerate(board[1:]):
        idx += 1
        if item == ' ':
            # check if bot can win in the next move
            hypothetical_board[idx] = current_player
            if check_if_won(hypothetical_board):
                return idx
            # check player can win in the next move
            hypothetical_board[idx] = other_player(current_player)
            if check_if_won(hypothetical_board):
                return idx
            # check if space in corners, take it
            if idx in corners:
                return idx
            # check if space in middle, take it
            if idx in middle:
                return idx
            # take what's left
            else: 
                return idx

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
    while ' ' in board[1:]:
        board[get_move(current_player, board)] = current_player
        game_and_keys(board)
        p = check_if_won(board)
        if p:
            print 'Game Over! %s won!!!' %p
        current_player = other_player(current_player)
    else:
        print 'Whomp whomp, it\'s a tie!'

# tic_tac_toe()
