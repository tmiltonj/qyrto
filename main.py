from game import Game
from player import Player

def main():
    game = Game()
    game.start(Player("Alice"), Player("Bob"))

if __name__ == "__main__":
    main()