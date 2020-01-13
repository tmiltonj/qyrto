from collections import namedtuple
from enum import Enum

Point = namedtuple('Point', ['x', 'y'])
Result = namedtuple('Result', ['win', 'dir', 'n'])

class Board:
    """ 
    Represents the game board, contains helper methods to add/remove pieces
    and check if the board is in a winning state
    """
    class DIR(Enum):
        """ Directions used when reporting the location of a win """
        H = 0
        V = 1
        D = 2

    def __init__(self, size: int = 4, num_attr: int = 4):
        self.size = size
        self.num_attr = num_attr
        self.board = [[[0] * num_attr for cols in range(size)] for rows in range(size)]
        self.free_spaces = [Point(x, y) for x in range(size) for y in range(size)]

    def place(self, piece, pos: Point):
        """ Place a new piece at pos, if not occupied """
        if (pos not in self.free_spaces):
            raise ValueError("Cannot place piece at {}".format(pos))

        self.board[pos.x][pos.y] = piece
        self.free_spaces.remove(pos)

    def remove(self, pos: Point):
        """ Remove a piece from pos, if a piece exists """
        if (pos in self.free_spaces):
            raise ValueError("No piece to remove at {}".format(pos))

        self.board[pos.x][pos.y] = [0] * self.num_attr
        self.free_spaces.append(pos)

    def get_row(self, n: int):
        """ Return the nth row of the board """
        return self.board[n]

    def get_col(self, n: int):
        """ Returns the nth column of the board """
        return [row[n] for row in self.board]

    def get_attr(self, n: int):
        """ Return a 2d array of the nth attribute of pieces on the board """
        return [list(map(lambda p: p[n], row)) for row in self.board]

    def has_won(self):
        """ 
        Determine if the board is in a winning state.
        
        :returns: a Result tuple indicating whether a win is found,
                  it's direction and location (row/col/diagonal index)
        """
        # Check each attribute
        for attr in range(self.num_attr):
            b = self.get_attr(attr)
            d_sum_pos = 0
            d_sum_neg = 0
            # Loop over each row/column
            for i in range(self.size):
                # Since attributes are 1 or -1, if they are all the same, a win has been found
                if abs(sum(b[i])) == self.size:
                    return Result(True, Board.DIR.H, i)
                elif abs(sum([row[i] for row in b])) == self.size:
                    return Result(True, Board.DIR.V, i)
                else:
                    # Check diagonals
                    d_sum_pos += b[i][i]
                    d_sum_neg += b[self.size - i - 1][i]

            if d_sum_pos == self.size:
                return Result(True, Board.DIR.D, 0)
            elif d_sum_neg == self.size:
                return Result(True, Board.DIR.D, 1)

        return Result(False, Board.DIR.H, -1)


if __name__ == "__main__":
    """ Test code """
    def print_win(res: Result):
        if res.win:
            if res.dir == Board.DIR.H:
                print("Win on row {}".format(res.n))
            elif res.dir == Board.DIR.V:
                print("Win on col {}".format(res.n))
            else:
                print("Win on diagonal {}".format(res.n))
        else:
            print("No win")

        return res.win

    b = Board(4, 4)

    assert not print_win(b.has_won())

    b.place([1, 1, 1, 1], Point(0, 0))
    b.place([1, 1, 1, 1], Point(1, 1))
    b.place([1, 1, 1, 1], Point(2, 2))

    assert not print_win(b.has_won())

    b.remove(Point(2, 2))

    b.place([-1, -1, 1, -1], Point(0, 1))
    b.place([-1, 1, 1, 1], Point(2, 1))
    b.place([1, -1, 1, -1], Point(3, 1))

    assert print_win(b.has_won())

    b.remove(Point(1, 1))

    assert not print_win(b.has_won())

    b.place([-1, 1, 1, -1], Point(2, 0))
    b.place([-1, 1, 1, -1], Point(2, 2))
    b.place([-1, -1, -1, -1], Point(2, 3))

    assert print_win(b.has_won())

    b.remove(Point(2, 3))

    assert not print_win(b.has_won())

    b.place([-1, -1, 1, 1], Point(0, 3))
    b.place([-1, -1, -1, 1], Point(1, 2))
    b.place([-1, -1, 1, 1], Point(3, 0))

    assert print_win(b.has_won())