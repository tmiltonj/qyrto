# QUARTO SIM #

CLI-based Python simulation of Quarto written in Python 3.6

## Running ##

To run a single game with UI output:

```bash
python main.py
```

To run a batch of games (e.g. 5000) and report results:

```bash
python main.py B 5000
```

## Writing Players / AI ##

1. Subclass the Player class in `player.py` and implement `select_piece()` and `place_piece()`
2. Modify `main.py` to use the new subclass

NovicePlayer is an example AI which looks 1 move ahead.

### Pieces ###

Pieces are represented as lists of attributes, with each element representing an attribute (color, size, shape, indent, etc). Attributes are either 1 or -1, with 0 representing an empty piece.

Color | Size | Shape | Indent
---|---|---|---
1 = White | 1 = Short | 1 = Square | 1 = Flat
-1 = Black | -1 = Tall | -1 = Circle | -1 = Indent

eg. `[1, -1, 1, 1]` = White, tall, square, flat piece.

### Board ###

The board is a `BSIZExBSIZE` (default 4) 2d list of Pieces. Empty spaces contain pieces with an attribute list filled with 0s.

The Board object contains the following helper methods and attributes:

```python
free_spaces # A list of Points(row, column) representing empty spaces
```

```python
get_row(n)  # Returns the nth row
get_col(n)  # Returns the nth column
get_attr(n) # Returns a 2d array of the nth attribute of each piece
```