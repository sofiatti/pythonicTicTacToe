class Game():
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

    @classmethod
    def check_if_won(cls, board):
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

    def get_play(self, symbol):
        instructions = "You are " + symbol + ". Please enter your play [1-9]: "
        try: 
            play = int(raw_input(instructions))
        except ValueError:
            print "Please enter a number from 1 to 9."  
            return self.get_play(symbol)
        try:
            play < 1 and play > 9
            raise Exception('**Error** Only numbers 1 through 9 are valid.\n')
        except Exception, e:
            print str(e)
            return self.get_play(symbol) 
        while self.board[play] != ' ':
            print 'Oops!  That\'s taken!  Try again...'
            return self.get_play(symbol)
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

    def next_step(self, idx, current_player):
        hypothetical_board = list(self.board)
        hypothetical_board[idx] = current_player
        if Game.check_if_won(hypothetical_board):
            return idx

    def empty_spaces(self):
        empty_idx = []
        for idx, item in enumerate(self.board[1:]):
            idx += 1
            if item == ' ':
                empty_idx.append(idx)
        return empty_idx

    def get_bot_move(self, current_player):
        possible_plays = self.empty_spaces()
        for next_play in possible_plays:
            # check if bot can win in the next move
            play = self.next_step(next_play, current_player)
            if play:
                return play
            # check player can win in the next move
            opponent = self.other_player(str(current_player))
            play = self.next_step(next_play, opponent)
            if play:
                return play
        # check if space in corners, take it
        for play in self.corners:
            if play in possible_plays:
                return play
        for play in self.middle:
            if play in possible_plays:
                return play
        for play in self.sides:
            if play in possible_plays:
                return play
    @classmethod
    def other_player(cls, current_player):
        if current_player == "X":
            return "O"
        elif current_player == "O":
            return "X"

    def make_a_play(self, current_player):
        self.draw()
        p = Game.check_if_won(self.board)
        
    def start_game(self):
        print 'Welcome to Tic-Tac-Toe! '
        bot_or_friend = raw_input("Who would you like to play? (bot/friend) ")
        self.draw()
        current_player = "X"
        while ' ' in self.board[1:]:
            if bot_or_friend == 'bot':
                bot_move = self.get_bot_move(current_player)
                self.board[bot_move] = current_player
                self.draw()
                if Game.check_if_won(self.board):
                    print 'Game Over! %s won!!!' %current_player
                current_player = Game.other_player(current_player)
                if ' ' not in self.board[1:]:
                    break
            self.board[self.get_play(current_player)] = current_player
            if Game.check_if_won(self.board):
                print 'Game Over! %s won!!!' %current_player
            current_player = Game.other_player(current_player)
        print 'Whomp whomp, it\'s a tie!'

if __name__ == "__main__":
    tic_tac_toe = Game()
    tic_tac_toe.start_game()
