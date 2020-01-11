from game import Game
from player import Player, NovicePlayer
from functools import partial
import sys

player_one = NovicePlayer("Nelly")
player_two = Player("Bob")

def single():
    """ Run a single game, printing to console """
    game = Game(print_f = partial(print, end=''))
    game.start(player_one, player_two)

def batch(n_games = 10000):
    """ Run n_games trials and report the results """
    # Skip print statements
    def dummy_print(str):
        pass

    # Run the batch
    pone_wins = 0
    ptwo_wins = 0
    n_draws = 0
    alt = False
    for _ in range(n_games):
        # Reset the game
        game = Game(print_f=dummy_print)

        # Alternate who goes first
        if alt:
            winner = game.start(player_one, player_two)
        else:
            winner = game.start(player_two, player_one)
        alt = not alt

        # Record W/L/D
        if winner == player_one:
            pone_wins += 1
        elif winner == player_two:
            ptwo_wins += 1
        else:
            n_draws += 1

    # Show results
    print("P1: {:>7.2%}\t({:>6})\nP2: {:>7.2%}\t({:>6})\nD:  {:>7.2%}\t({:>6})".format(
        pone_wins / n_games, pone_wins,
        ptwo_wins / n_games, ptwo_wins,
        n_draws / n_games, n_draws)
    )

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].upper() == 'B':
        if len(sys.argv) > 2:
            # Specify number of times to run
            batch(int(sys.argv[2]))
        else:
            # Default
            batch()
    else:
        single()