from monsters import Monster, Potted_plant

# work to be done

# create character classes and monsters
# create items and bonuses
# create game progession
# ? multiplayer option ? 

trial_monster = Monster()
print(trial_monster)

plant = Potted_plant()
print(plant)
print(plant.description())
print(plant.bad_stuff())

# eventual plan for the main loop
# idea from dnd rpg lib

# def main():
#     game = Game()
#     game.main_menu
#     while True:
#         game.next_turn()
#         game.combat_system.start_combat("goblin")