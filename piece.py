from enum import Enum

# Piece Attributes
class Color(Enum):
    BLACK = True
    WHITE = False

class Size(Enum):
    TALL = True
    SHORT = False

class Shape(Enum):
    CIRCLE = True
    SQUARE = False

class Indent(Enum):
    INDENT = True
    FLAT = False

class Piece:
    """ 
    Represents the pieces used in Quarto.

    Has 4 attributes: color, size, shape and indentation represented
    as object attributes or a 4-digit binary 'code'
    """
    @classmethod
    def GetPieces(cls):
        """ Factory method returning a list of the 16 Pieces used in a regular game """
        return [
            Piece(Color.BLACK, Size.SHORT, Shape.SQUARE, Indent.FLAT),
            Piece(Color.BLACK, Size.SHORT, Shape.SQUARE, Indent.INDENT),
            Piece(Color.BLACK, Size.SHORT, Shape.CIRCLE, Indent.FLAT),
            Piece(Color.BLACK, Size.SHORT, Shape.CIRCLE, Indent.INDENT),

            Piece(Color.BLACK, Size.TALL, Shape.CIRCLE, Indent.FLAT),
            Piece(Color.BLACK, Size.TALL, Shape.CIRCLE, Indent.INDENT),
            Piece(Color.BLACK, Size.TALL, Shape.SQUARE, Indent.FLAT),
            Piece(Color.BLACK, Size.TALL, Shape.SQUARE, Indent.INDENT),

            Piece(Color.WHITE, Size.SHORT, Shape.SQUARE, Indent.FLAT),
            Piece(Color.WHITE, Size.SHORT, Shape.SQUARE, Indent.INDENT),
            Piece(Color.WHITE, Size.SHORT, Shape.CIRCLE, Indent.FLAT),
            Piece(Color.WHITE, Size.SHORT, Shape.CIRCLE, Indent.INDENT),

            Piece(Color.WHITE, Size.TALL, Shape.CIRCLE, Indent.FLAT),
            Piece(Color.WHITE, Size.TALL, Shape.CIRCLE, Indent.INDENT),
            Piece(Color.WHITE, Size.TALL, Shape.SQUARE, Indent.FLAT),
            Piece(Color.WHITE, Size.TALL, Shape.SQUARE, Indent.INDENT),
        ]

    def __init__(self, color: Color, size: Size, shape: Shape, indent: Indent):
        self.color = color
        self.size = size
        self.shape = shape
        self.indent = indent

    @property
    def code(self):
        """ 
        Code is a 4digit binary number representing the Piece's attributes, ordered by;

        (color) (size) (shape) (indent)
        """
        return (self.color == Color.BLACK) * 0b1000 + \
        (self.size == Size.SHORT) * 0b0100 + \
        (self.shape == Shape.SQUARE) * 0b0010 + \
        (self.indent == Indent.FLAT) * 0b0001