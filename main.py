from monsters import Monster, Potted_plant
from turns import Game, Game_sequence

# work to be done

# create character classes and monsters
# create items and bonuses
# create game progession
# ? multiplayer option ? 

# plant = Potted_plant()
# print(plant)
# print(plant.description())
# print(plant.bad_stuff())
# print()

# eventual plan for the main loop
# idea from dnd rpg lib

def main():
    game = Game()
    turn = Game_sequence()
    game.main_menu()
    while True:
        turn.open_door()
        turn.loot_room()
        turn.character_optimize()
        break

        # infinite loop 
    
main()