import random
from copy import deepcopy

class Player():
    """ 
    Interface for Players. 
    Subclass this and implement custom select_piece() and place_piece() logic.
    """
    def __init__(self, name = "Player"):
        self.name = name

    def __str__(self):
        return self.name

    def select_piece(self, pieces, board):
        """ 
        Choose which piece to give the opponent on a given turn.

        :param pieces: list of pieces to be selected from
        :param board: current state of the board, a 2d array of pieces

        :returns: a piece, which must be from the pieces list provided
        """
        return random.choice(pieces)

    def place_piece(self, piece, board):
        """
        Choose where to place a given piece.

        :param piece: the piece to place
        :param board: current state of the board, a 2d array of pieces

        :returns: a tuple (column, row), indicating the position to place the piece
        """
        return random.choice(board.free_spaces)

class NovicePlayer(Player):
    """
    def select_piece(self, pieces, board):
        pass
    """

    def place_piece(self, piece, board):
        b = deepcopy(board)

        free_spaces = board.free_spaces

        winning_moves = []
        for space in free_spaces:
            b.place(piece, space)
            res = b.has_won()
            if res.win:
                return space
            else:
                b.remove(space)
        
        return random.choice(free_spaces)