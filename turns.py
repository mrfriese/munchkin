# holds turn progression

from player import Munchkin
import monsters
import time



class Game:

    def __init__(self):
        # screen input
        self.player = Munchkin()
        

    def main_menu(self):
        print("Welcome to the game Munchkin!")
        time.sleep(1)
        print("> New Game")
        time.sleep(1)
        choice = input("Please make a selection: ")
        if choice == "New Game":
            self.new_game()

    
    def new_game(self):

        # get number of players

        # put player name input inside a for loop
        pname = input("Please type out your name: ")
        self.player.name = pname
        print("Ok {}, you are a Level 1 Human".format(pname))
        # set defaults to level one human with no armour.
        # save player as munchkin subclass

        # import function for player hand(s)
        print("Dealing starting treasure cards...")
        time.sleep(1)

        # import function for character edit
        # ie. armour, race, class etc.
        print("{} are you going to update your equipment?".format(pname))
        
        time.sleep(1)
        print("Ok let's begin!")


class Game_sequence:
    
    def __init__(self):
        self.max_turns = 1

    def open_door(self):
        print("Open door place holder")

    def loot_room(self):
        print("loot the room place holder")

    def character_optimize(self):
        print("character optimization place holder")