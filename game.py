from piece import Piece
from player import Player

class Game():
    """ 
    Quarto game logic.

    Create an instance and call start() with two Player objects to play.
    """
    BSIZE = 4 # Size of the board

    def __init__(self):
        self.board = [[None for cols in range(Game.BSIZE)] for rows in range(Game.BSIZE)]
        self.pieces = Piece.GetPieces()

    def get_free_spaces(self):
        """ Return the empty spaces on the board as a list of tuples (x, y) """
        spaces = []
        for y, row in enumerate(self.board):
            for x, tile in enumerate(row):
                if tile == None:
                    spaces.append((y, x))

        return spaces

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
        draw = False

        while not self.has_won():
            free_spaces = self.get_free_spaces()

            # Check for a draw (no free spaces left)
            if (len(free_spaces) == 0):
                draw = True
                break

            # Show current turn
            turn += 1
            print("TURN {} ({})".format(turn, active_player))

            # Pick a piece
            print(active_player, "is picking a piece: ", end='')
            piece = active_player.select_piece(self.pieces, self.board, free_spaces)
            self.pieces.remove(piece)
            print('{0:0>4b}'.format(piece.code))

            # Change active players
            temp = active_player
            active_player = other_player
            other_player = temp

            # Place a piece
            print(active_player, "is placing a piece: ", end='')
            loc = active_player.place_piece(piece, self.board, free_spaces)
            self.board[loc[0]][loc[1]] = piece
            print(loc)

            # GUI
            self.show_board()

        # Show if the game had a winner
        if draw:
            print("DRAW: No moves available")
        else:
            print("\nWIN:", active_player)

    def has_won(self):
        """ 
        Determine whether the board has a winning configuration

        :returns: True if a row, column or diagonal has 4 pieces 
        with a matching attribute. Otherwise returns False.
        """
        
        """ 
        Each piece is represented as a binary number w/ each digit representing an attr, so a bitwise 
        mask is used to filter for each attribute.

        For each attribute in each row/column/diagonal, count +1 or -1 for a 1 or 0 respectively.
        If the total is +4 or -4, we have seen 4 of the same attribute in a row, which is a win state.
        """
        masks = [0b1000, 0b100, 0b10, 0b1]
        for mask in masks:
            # Check rows
            for y in range(Game.BSIZE):
                count = 0
                for x in range(Game.BSIZE):
                    if (self.board[y][x] != None):
                        # Increase the count based on the attr is present
                        count += 1 if self.board[y][x].code & mask else -1
                # +/-4 means 4 of the same attribute in a row
                if (abs(count) == Game.BSIZE):
                    print("Row", y, "has a win")
                    return True

            # Check cols (same logic as rows)
            for x in range(Game.BSIZE):
                count = 0
                for y in range(Game.BSIZE):
                    if (self.board[y][x] != None):
                        count += 1 if self.board[y][x].code & mask else -1
                if (abs(count) == Game.BSIZE):
                    print("Col", x, "has a win")
                    return True

            # Check diagonals (no need for nested loops)
            count = 0
            for d in range(Game.BSIZE):
                if (self.board[d][d] != None):
                    count += 1 if self.board[d][d].code & mask else -1
            if (abs(count) == Game.BSIZE):
                print("D+ has a win")
                return True
            
            # Top-right to bottom-left diagonal
            count = 0
            for d in range(Game.BSIZE):
                if (self.board[d][Game.BSIZE - d - 1] != None):
                    count += 1 if self.board[d][Game.BSIZE - d - 1].code & mask else -1
            if (abs(count) == Game.BSIZE):
                print("D- has a win")
                return True

        # We didn't find a win states
        return False

    def show_board(self):
        """ Print the current state of the board """
        for row in self.board:
            print("| ", end="")
            for tile in row:
                print('{0:0>4b}'.format(tile.code) if tile != None else '    ', end=" | ")
            print("\n")
