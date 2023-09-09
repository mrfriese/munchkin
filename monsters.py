# Lists Monsters and associated characteristics

class Monster:
    """ Holds all monster that you may come across. """
    
    def __init__(self, name="default", level=1, treasure=1):
        self.name = name
        self.level = level
        self.treasure = treasure

    def description(self):
        description = description

    def bad_stuff(self):
        bad_stuff = bad_stuff
    
    def __str__(self):
        return "A level {0.level} {0.name} appeared!".format(self)
    
class Potted_plant(Monster):
    def __init__(self, name="Potted Plant"):
        super().__init__(name, level=1, treasure=1)

    def description(self):
        return("Elves draw an extra treasure after defeating it.")
        # if race == "Elf":
        #     treasure += 1
        # else:
        #     treasure = treasure

    def bad_stuff(self):
        return("Bad Stuff: None. Escape is automatic.")