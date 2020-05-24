# SPDX-License-Identifier: AGPL-3.0-or-later
import time

# Game variables
number_of_forcasters = 0
number_of_farmers = 0
number_of_harvesters = 0
number_of_resters = 0
receiver_charge = 0
amount_of_food = 10
population = 5
number_of_houses = 2
number_of_food_silos = 1
food_cap = number_of_food_silos * 5
pop_cap = number_of_houses * 3
disaster_threshold = 3 + (number_of_forcasters * 2)
amount_of_material = 0


def game_reset():
    """reset the game"""
    population = 5
    food = 10
    houses = 2


print("Second Nature")
time.sleep(3)
print("Reach a population of 20 to win\n")
time.sleep(3)
game_reset()


# Main game loop
while population > 0 and population < 20:
    print("Colony Status:")
    print(
        f"population: {population}\n"
        f"food: {amount_of_food}\n"
        f"houses: {number_of_houses}\n"
    )
    print("1. Activate\n" "2. Move\n" "3. Build")
    player_choice = input()
    if player_choice == "1":
        # Activate what?
        pass
    if player_choice == "2":
        # from where -> to where
        pass
    if player_choice == "3":
        # build what?
        print("1. Food Silo\n" "2. House")
        pass
    # feed colonists
    # disaster chance
