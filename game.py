from player import Player
from board import Board, Point, Result

class Game():
    """ 
    Quarto game logic.

    Create an instance and call start() with two Player objects to play.
    """
    def __init__(self, print_f = print, bsize = 4, num_attr = 4):
        self.print_f = print_f
        self.board = Board(bsize, num_attr)
        # Generate all num_attr digit binary numbers and convert into a list
        self.pieces = []
        for dec in range(2 ** num_attr):
            piece = []
            for attr in range(num_attr):
                piece.append(1 if dec & 1 else -1)
                dec = dec >> 1
            self.pieces.append(piece)

    def start(self, player_a: Player, player_b: Player):
        """ 
        Start the main game loop. Runs until a win state or draw state has been reached.
        player_a always goes first.

        :param player_a: the first player
        :param player_b: the second player
        """
        active_player = player_a
        other_player = player_b

        turn = 0
        result = Result(False, Board.DIR.H, -1)

        while not result.win:
            # Check for a draw (no free spaces left)
            free_spaces = self.board.free_spaces
            if (len(free_spaces) == 0):
                break

            # Show current turn
            turn += 1
            self.print_f("\nTURN {} ({})\n".format(turn, active_player))

            # Pick a piece
            self.print_f("{} is picking a piece: ".format(active_player))
            piece = active_player.select_piece(self.pieces, self.board)
            self.pieces.remove(piece)
            self.print_f('{}\n'.format(piece))

            # Change active players
            temp = active_player
            active_player = other_player
            other_player = temp

            # Place a piece
            self.print_f("{} is placing a piece: ".format(active_player))
            pos = active_player.place_piece(piece, self.board)
            self.board.place(piece, pos)
            self.print_f("{}\n".format(pos))

            # GUI
            self.show_board()

            # Check for win
            result = self.board.has_won()

        # Show if the game had a winner
        if result.win:
            d_map = {
                Board.DIR.H: 'row',
                Board.DIR.V: 'column',
                Board.DIR.D: 'diagonal'
            }
            self.print_f("{} won on {} {}!\n".format(active_player, d_map[result.dir], result.n))
            return active_player
        else:
            self.print_f("DRAW: No moves available\n")
            return None

    def show_board(self):
        """ Print the current state of the board """
        for row in self.board.board:
            self.print_f("| ")
            for tile in row:
                s = ''
                for attr in tile:
                    if attr == 1:
                        s += 'X'
                    elif attr == -1:
                        s += 'o'
                    else:
                        s += ' '
                self.print_f('{} | '.format(s))
            self.print_f("\n\n")
