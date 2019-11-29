import random

# Character
characterintro = ("You are a courier working for Flo, a businessman in Lumbridge. He seems shady. You don't really mind though, since the pay is good for what is essentially just walking around.")
print(characterintro)
character = input("Your character's name: ")
character = character.capitalize()
print("Here starts " + character + "'s adventure.")
print()

# Intro
intro = ("Welcome to the land of Gielinor, " + character + "! Enjoy your stay.")
print(intro)
print()

# Flo
choice1 = input("You wake up to another day. Luckily it's a day off work, so it's not too bad. You hear a knock on your door. Will you answer?(Y/N): ")
choice1 = choice1.capitalize()
print()
if choice1 == "N":
    print("The door opens despite you ignoring the knocking. It's Flo. He storms in and tells " + character + " that they have to help him. There are some loan sharks looking for me and he need a place to hide! Can he stay over for a while?")
elif choice1 == "Y":
    print("Before you can get to the door, your boss Flo opens the door and slams it shut behind him. He tells you that you have to help him. There are loan sharks after him and he couldn't find a better place to hide! Can he stay at your place?")
print("Considering he's your boss, you decide to let him stay. Not like the loan sharks would come looking for him here, right?")
print()

#
print("After calming down Flo and chatting with him for a while, you tell him he can stay there while you go and get some food and other supplies from the local general store.")
print("You go and use a few of your gold coins to buy a loaf of bread, an apple, and some wine for lonelier evenings.")
