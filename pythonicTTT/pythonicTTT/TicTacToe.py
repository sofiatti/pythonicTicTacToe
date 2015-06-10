class game():
    def __init__(self):
        self.board = [' '] * 10
        self.corners = [1,3,7,9]
        self.sides = [2,4,6,8]
        self.middle = [5]

    def draw(self):
        print '\n'
        print '  Game     Key'
        print ' ' + self.board[1] + '|' + self.board[2] + '|' + self.board[3] + '     1|2|3'
        print ' - - -    - - -'
        print ' ' + self.board[4] + '|' + self.board[5] + '|' + self.board[6] + '     4|5|6'
        print ' - - -    - - -'
        print ' ' + self.board[7] + '|' + self.board[8] + '|' + self.board[9] + '     7|8|9'
        print '\n'

    def check_if_won(self):
        for p in ["X", "O"]:
            possibilities = [
                #Consecutive line
                self.board[1:4], self.board[4:7], self.board[7:10],
                #Consecutive Row:
                self.board[1::3], self.board[2::3], self.board[3::3],
                #Consecutive Diagonals:
                self.board[1::4], self.board[3::2]
                ]

            for element in possibilities:
                if element == [p,p,p]:
                    return True
        return False

def get_play(symbol, board):
    instructions = "You are " + symbol + ". Please enter your play [1-9]: "
    try: 
        play = int(raw_input(instructions))
    except ValueError:
        print "Please enter a number from 1 to 9."  
        return get_play(symbol, board)
    try:
        if play < 0 and play > 9:
            raise Exception('Only 1 through 9 are valid.')
    except Exception, e:
        print str(e)
        return get_play(symbol, board) 
    while board[play] != ' ':
        print 'Oops!  That\'s taken!  Try again...'
        return get_play(symbol, board)
    return play  

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

    def next_step(idx, current_player, self):
        hypothetical_board = list(self.board)
        hypothetical_board[idx] = current_player
        if check_if_won(hypothetical_board):
            return idx

    def empty_spaces(self):
        empty_idx = []
        for idx, item in enumerate(self.board[1:]):
            idx += 1
            if item == ' ':
                empty_idx.append(idx)
        return empty_idx

    def get_bot_move(current_player, self):
        possible_plays = empty_spaces(self.board)
        for next_play in possible_plays:
            # check if bot can win in the next move
            play = next_step(next_play, current_player, self.board)
            if play:
                return play
            # check player can win in the next move
            opponent = other_player(str(current_player))
            play = next_step(next_play, opponent, self.board)
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

    def make_a_play(self, current_player):
        draw(self.board)
        p = check_if_won(self.board)
        
    def start_game(self):
        print 'Welcome to Tic-Tac-Toe! '
        bot_or_friend = raw_input("Who would you like to play? (bot/friend) ")
        self.draw(self)
        current_player = "X"
        while ' ' in self.board[1:]:
            if bot_or_friend == 'bot':
                self.board[get_bot_move(current_player, self.board)] = current_player
                self.draw(self)
                if self.check_if_won(self.board):
                    print 'Game Over! %s won!!!' %current_player
                current_player = other_player(current_player)
                if ' ' not in self.board[1:]:
                    break
            self.board[get_move(current_player, self)] = current_player
            if self.check_if_won(self):
                print 'Game Over! %s won!!!' %current_player
            current_player = other_player(current_player)
        print 'Whomp whomp, it\'s a tie!'

if __name__ == "__main__":
    tic_tac_toe = game()
    tic_tac_toe.start_game()
    tic_tac_toe()
