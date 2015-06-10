import sys
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
                return True
    return False

corners = [1,3,7,9]
sides = [2,4,6,8]
middle = [5]

def get_move(symbol, board):
    instructions = "You are " + symbol + ". Please enter your play [1-9]: "
    try:
        play = int(raw_input(instructions)
        if play < 0 and play > 9:
            raise Exception('Not a valid number. Please enter a number from 1 '
                            'to 9')
    except ValueError:
        print "Please enter a number from 1 to 9"  
    except Exception, e:
        print str(e)       
    while board[play] != ' ':
        print 'Oops!  That\'s taken!  Try again...'
        play = int(raw_input(instructions))
    else:
        return play

def next_step(idx, current_player, board):
    hypothetical_board = list(board)
    hypothetical_board[idx] = current_player
    if check_if_won(hypothetical_board):
        return idx

def empty_spaces(board):
    empty_idx = []
    for idx, item in enumerate(board[1:]):
        idx += 1
        if item == ' ':
            empty_idx.append(idx)
    return empty_idx

def get_bot_move(current_player, board):
    possible_plays = empty_spaces(board)
    for next_play in possible_plays:
        # check if bot can win in the next move
        play = next_step(next_play, current_player, board)
        if play:
            return play
        # check player can win in the next move
        opponent = other_player(str(current_player))
        play = next_step(next_play, opponent, board)
        if play:
            return play
    # check if space in corners, take it
    for play in corners:
        if play in possible_plays:
            return play
    for play in middle:
        if play in possible_plays:
            return play
    for play in sides:
        if play in possible_plays:
            return play

def other_player(current_player):
    if current_player == "X":
        return "O"
    elif current_player == "O":
        return "X"

def make_a_play(board, current_player):
    draw(board)
    p = check_if_won(board)

def get_value_bot_or_friend():
    bot_or_friend = raw_input("Who would you like to play? (bot/friend) ")
    try:
        if bot_or_friend not in ['bot', 'friend']:
            raise Exception("Only 'bot' or 'friend' are valid inputs.")
        else:
            return bot_or_friend
    except Exception, e:
        str(e)
        return get_value_bot_or_friend()


def tic_tac_toe():
    print 'Welcome to Tic-Tac-Toe! '

    board = [' '] * 10
    draw(board)
    current_player = "X"
    while ' ' in board[1:]:
        if bot_or_friend == 'bot':
            board[get_bot_move(current_player, board)] = current_player
            draw(board)
            if check_if_won(board):
                print 'Game Over! %s won!!!' %current_player
            current_player = other_player(current_player)
            if ' ' not in board[1:]:
                break
        board[get_move(current_player, board)] = current_player
        if check_if_won(board):
            print 'Game Over! %s won!!!' %current_player
        current_player = other_player(current_player)
    print 'Whomp whomp, it\'s a tie!'

tic_tac_toe()
