# SPDX-License-Identifier: AGPL-3.0-or-later
import time

# Game variables
food = 10
population = 5
housing = 2


def game_reset():
    """reset the game"""
    population = 5
    food = 10
    housing = 2


print("Second Nature")
time.sleep(3)
print("Reach a population of 20 to win\n")
time.sleep(3)
game_reset()


# Main game loop
while population > 0 and population < 20:
    print("Colony Status:")
    print(f"population: {population}\n" f"food: {food}\n" f"housing: {housing}\n")
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
        pass
