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
        pname = input("Please type out your name: ")
        self.player.name = pname
        print("Ok {}, you are a Level 1 Human".format(pname))

        # set defaults to level one human with no armour.
        # game probably includes some treasure cards to increase 
        # base stats. 