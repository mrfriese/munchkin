# Lists Monsters and associated characteristics

class Monster:
    """ Holds all monster that you may come across. """
    
    def __init__(self, name="default", level=1, treasure=1):
        self.name = name
        self.level = level
        self.treasure = treasure
    
    def __str__(self):
        return "A level {0.level} {0.name} appeared!".format(self)
    
class Potted_plant(Monster):
    def __init__(self, name="Potted Plant"):
        super().__init__(name, level=1, treasure=1)

        