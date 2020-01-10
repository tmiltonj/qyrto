from piece import Piece
from player import Player
from board import Board, Point, Result

class Game():
    """ 
    Quarto game logic.

    Create an instance and call start() with two Player objects to play.
    """
    def __init__(self, bsize = 4, num_attr = 4):
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
            print("TURN {} ({})".format(turn, active_player))

            # Pick a piece
            print(active_player, "is picking a piece: ", end='')
            piece = active_player.select_piece(self.pieces, self.board)
            self.pieces.remove(piece)
            print(piece)

            # Change active players
            temp = active_player
            active_player = other_player
            other_player = temp

            # Place a piece
            print(active_player, "is placing a piece: ", end='')
            pos = active_player.place_piece(piece, self.board)
            self.board.place(piece, pos)
            print(pos)

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
            print("{} won on {} {}!".format(active_player, d_map[result.dir], result.n))
        else:
            print("DRAW: No moves available")

    def show_board(self):
        """ Print the current state of the board """
        for row in self.board.board:
            print("| ", end="")
            for tile in row:
                s = ''
                for attr in tile:
                    if attr == 1:
                        s += 'X'
                    elif attr == -1:
                        s += 'o'
                    else:
                        s += ' '
                print(s, end=' | ')
            print("\n")
