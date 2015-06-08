from sys import exit

def array_equal(a_1, a_2):
    if len(a_1) != len(a_2):
        return False
    else:
        for idx, item in enumerate(a_1):
            if item != a_2[idx]:
                return False

        return True

def game_and_keys(line_matrix):
    print '\n'
    print '  Game     Key'
    print ' ' + line_matrix[0] + '|' + line_matrix[1] + '|' + line_matrix[2] + '     0|1|2'
    print ' - - -    - - -'
    print ' ' + line_matrix[3] + '|' + line_matrix[4] + '|' + line_matrix[5] + '     3|4|5'
    print ' - - -    - - -'
    print ' ' + line_matrix[6] + '|' + line_matrix[7] + '|' + line_matrix[8] + '     6|7|8'
    print '\n'

def check_if_won(line_matrix):
    for p in ["X", "O"]:
        while False:
        #Consecutive line
            array_equal(line_matrix[0:3], [p,p,p])
            array_equal(line_matrix[3:6], [p,p,p])
            array_equal(line_matrix[6:9], [p,p,p])
            #Consecutive row
            array_equal([line_matrix[0], line_matrix[3], line_matrix[6]], [p,p,p])
            array_equal([line_matrix[1], line_matrix[4], line_matrix[7]], [p,p,p])
            array_equal([line_matrix[2], line_matrix[5], line_matrix[8]], [p,p,p])
            #Consecutive Diagonals:
            array_equal([line_matrix[0], line_matrix[4], line_matrix[8]], [p,p,p])
            array_equal([line_matrix[2], line_matrix[4], line_matrix[6]], [p,p,p])
    return (p)

def isWinner(line_matrix):
    p = check_if_won(line_matrix)
    print 'Game Over! %s won!!!' %p
    exit(0)

def get_move(symbol, line_matrix):
    instructions = "You are " + symbol + ". Please enter your play [0-8]: "
    play = int(raw_input(instructions))
    while line_matrix[play] != ' ':
        print 'Oops!  That\'s taken!  Try again...'
        play = int(raw_input(instructions))
    else:
        return play

def switch_player(current_player):
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

    line_matrix = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    game_and_keys(line_matrix)

    current_player = "X"

    while ' ' in line_matrix:
        line_matrix[get_move(current_player, line_matrix)] = current_player
        game_and_keys(line_matrix)
        isWinner(line_matrix)
        current_player = switch_player(current_player)
    else:
        print 'Whomp whomp, it\'s a tie!'
        exit(0)

tic_tac_toe()
