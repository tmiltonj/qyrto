from game import Game
from player import Player, NovicePlayer

def main():
    game = Game()
    game.start(NovicePlayer("Alice"), Player("Bob"))

if __name__ == "__main__":
    main()