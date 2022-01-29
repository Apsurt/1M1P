from player import Player

class Game:
    def __init__(self):
        self.player = Player()
        self.bot = Player()
        print(self.player.deck)

Game()