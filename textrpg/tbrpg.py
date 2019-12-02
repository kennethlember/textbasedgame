import random

# Character
character = input("Your character's name: ")
character = character.capitalize()
print("Here starts " + character + "'s adventure.")
print()
character_level = 1

# Intro
intro = ("Welcome, " + character + "! Enjoy your stay.")
print(intro)
print()

# Start
start = ("You find yourself in front of the town castle. From here you can head wherever you want to.")
print(start)

# Movement
start_position = [2, 0]
user_position = start_position
def get_allowed_movechoices(up):
    allowed_movechoices = ["N", "S", "W", "E"]
    if up[0] == 0:
        allowed_movechoices.remove("N")
    return allowed_movechoices
    
while True:
    print(user_position)
    movechoice = ""
    while movechoice not in get_allowed_movechoices(user_position):
        movechoice = input("Which direction would you like to move to?(N/W/S/E): ")
        movechoice = movechoice.capitalize()

    if movechoice == "N":
        user_position[0] -= 1
    elif movechoice == "S":
        user_position[0] += 1
    elif movechoice == "W":
        user_position[1] -= 1
    elif movechoice == "E":
        user_position[1] += 1