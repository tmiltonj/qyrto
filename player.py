import random

class Player():
    """ 
    Interface for Players. 
    Subclass this and implement custom select_piece() and place_piece() logic.
    """
    def __init__(self, name = "Player"):
        self.name = name

    def __str__(self):
        return self.name

    def select_piece(self, pieces, board, free_spaces):
        """ 
        Choose which piece to give the opponent on a given turn.

        :param pieces: list of Piece objects to be selected from
        :param board: current state of the board, a 2d array of Pieces
        :param free_spaces: list of tuples (column, row), representing the free spaces on the board

        :returns: a Piece, which must be from the pieces list provided
        """
        return random.choice(pieces)

    def place_piece(self, piece, board, free_spaces):
        """
        Choose where to place a given piece.

        :param piece: the Piece to place
        :param board: current state of the board, a 2d array of Pieces
        :param free_spaces: list of tuples (column, row), representing the free spaces on the board

        :returns: a tuple (column, row), indicating the position to place the piece
        """
        return random.choice(free_spaces)