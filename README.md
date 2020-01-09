# QUARTO SIM #

CLI-based Python simulation of Quarto written in Python 3.6

## Running ##

```bash
python main.py
```

## Writing Players / AI ##

1. Subclass the Player class in `player.py` and implement `select_piece()` and `place_piece()`
2. Modify `main.py` to use the new subclass

### Pieces ###

Pieces are represented as 4-digit binary numbers, with each digit representing an attribute (color, size, shape, indent).

Color | Size | Shape | Indent
---|---|---|---
0 = White | 0 = Short | 0 = Square | 0 = Flat
1 = Black | 1 = Tall | 1 = Circle | 1 = Indent

eg. `0100` = White, tall, square, flat piece

### Board ###

The board is a `BSIZExBSIZE` (default 4) 2d list of Pieces. Empty spaces contain `None` values.

### Free Spaces ###

Represented by `(row, column)` tuples. Used to determine which spaces are valid moves, and where a piece will be placed by each Player.