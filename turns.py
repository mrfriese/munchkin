# holds turn progression

from player import Munchkin
import monsters


class Game:

    def __init__(self):
        # screen input
        self.player = Munchkin(self)
        