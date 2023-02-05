#
# CS1010S --- Programming Methodology
#
# Contest 14.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes_contest import *
from contest_simulation import *
import random


class Player(Tribute):
    def next_action(self):
        # Next action should return a tuple of what your next action should
        # be. For the full list of tuple that your AI can return, refer to
        # the pdf file

        # As an example: the following code will make your AI just walk around
        # randomly every turn. You do NOT have to use this code if you don't
        # want to!
        if self.get_exits():
            direction = random.choice(self.get_exits())
            return ("GO", direction)

        # Otherwise, do nothing
        return None


#######################################
# Testing Code
#######################################

# We only execute code inside the if statement if this file is
# not being imported into another file
if __name__ == '__main__':
    def qualifer_map(size, wrap):
        game_config = GameConfig()
        game_config.set_item_count(Weapon, 10)
        game_config.set_item_count(RangedWeapon, 10)
        game_config.set_item_count(Food, 10)
        game_config.set_item_count(Medicine, 10)
        game_config.set_item_count(Animal, 10)
        game_config.steps = 1000

        def spawn_wild_animals(game):
            for i in range(3):
                animal = DefaultItemFactory.create(WildAnimal)
                game.add_object(animal[0])
                GAME_LOGGER.add_event("SPAWNED", animal[0])

        def narrow_map(game):
            gm = game.map
            if isinstance(gm, (SquareWithHoleMap, InputMap)):
                raise Exception('Map not suitable for this modifier :(')
            crunch = gm.crunch
            if crunch < (max(gm.rows, gm.columns) - 1) // 2:
                # Handle row tiles by moving down/up
                if crunch < (gm.rows - 1) // 2:
                    for i in range(gm.columns):
                        gm.map[crunch][i].neighbor_dict.clear()
                        gm.map[-crunch - 1][i].neighbor_dict.clear()
                        for obj in gm.map[crunch][i].objects.copy():
                            if isinstance(obj, Tribute):
                                obj.move_to(gm.map[crunch + 1][i], True)
                        for obj in gm.map[-crunch - 1][i].objects.copy():
                            if isinstance(obj, Tribute):
                                obj.move_to(gm.map[-crunch - 2][i], True)
                        if "SOUTH" in gm.map[crunch + 1][i].neighbor_dict:
                            del gm.map[crunch + 1][i].neighbor_dict["SOUTH"]
                        if "NORTH" in gm.map[-crunch - 2][i].neighbor_dict:
                            del gm.map[-crunch - 2][i].neighbor_dict["NORTH"]
                        if wrap and gm.map[crunch + 1][i] != gm.map[-crunch - 2][i]:
                            gm.map[crunch + 1][i].add_neighbor(gm.map[-crunch - 2][i], "SOUTH")

                # Handle column tiles by moving left/right
                if crunch < (gm.columns - 1) // 2:
                    for i in range(gm.rows):
                        gm.map[i][crunch].neighbor_dict.clear()
                        gm.map[i][-crunch - 1].neighbor_dict.clear()
                        for obj in gm.map[i][crunch].objects.copy():
                            if isinstance(obj, Tribute):
                                obj.move_to(gm.map[i][crunch + 1], True)
                        for obj in gm.map[i][-crunch - 1].objects.copy():
                            if isinstance(obj, Tribute):
                                obj.move_to(gm.map[i][-crunch - 2], True)
                        if "WEST" in gm.map[i][crunch + 1].neighbor_dict:
                            del gm.map[i][crunch + 1].neighbor_dict["WEST"]
                        if "EAST" in gm.map[i][-crunch - 2].neighbor_dict:
                            del gm.map[i][-crunch - 2].neighbor_dict["EAST"]
                        if wrap and gm.map[i][crunch + 1] != gm.map[i][-crunch - 2]:
                            gm.map[i][crunch + 1].add_neighbor(gm.map[i][-crunch - 2], "WEST")
            gm.crunch += 1

        game_config.add_periodic_event(20, spawn_wild_animals, "Spawn Wild Animals")
        #game_config.add_periodic_event(40, narrow_map, "Map Narrowing")

        return (SquareMap(size, wrap=wrap), game_config)

    # Create 6 AI Clones
    tributes = []
    for i in range(6):
        # An AI is represented by a tuple, with the Class as the first element,
        # and the name of the AI as the second
        ai = (Player, "AI" + str(i))
        tributes.append(ai)

    # Qualifier Rounds
    # Uncomments to run more rounds, or modify the rounds list
    # to include more rounds into the simulation
    # (Note: More rounds = longer simulation!)
    rounds = [qualifer_map(4, False),
              #qualifer_map(4, False),
              #qualifer_map(4, False),
              qualifer_map(4, True),
              #qualifer_map(4, True),
              #qualifer_map(4, True),
             ]

    match = Match(tributes, rounds)
    print("Simulating matches... might take a while")

    # Simulate without the graphics
    match.text_simulate_all()

    # Simulate a specific round with the graphics
    # Due to limitation in the graphics framework,
    # can only simulate one round at a time
    # Round id starts from 0
    #match.gui_simulate_round(0)
