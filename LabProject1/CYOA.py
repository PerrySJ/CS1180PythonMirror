import random

#Variables
weapon = False
death = False
gold = random.randint(50, 500)

name = input("What is your name?\n")

print(f"Hello {name}!")

print(f"It seems you have brought {gold} gold with you today!")

response = input("Would you like to purchase a weapon?\n")
print("\n")

if response.strip().lower() == "yes":
    response = input(f"What weapon would you like? You have {gold} gold\nGreatsword:150g\nDagger:50g\n")

    if response.strip().lower() == "greatsword":

        if gold < 150:
            print("You do not have enough gold, offer is closed.")
            weapon = False

        else:
            gold = gold - 150
            print("You have purchased the greatsword")
            print(f"You have {gold: .2f} gold remaining")
            weapon = True

    elif response.strip().lower() == "dagger":
        gold = gold - 50
        print("You have purchased the dagger")
        print(f"You have {gold: .2f} gold remaining\n")
        weapon = True

    else:
        print("Invalid Response, no weapon purchased")

elif response.strip().lower() == "no":
    print("Bold choice, lets continue.")

else:
    print("Invalid response, no weapon purchased")

print("Let's being our adventure!")

response = input("You leave your house, you must make a choice.\nGo up the mountain\nCross the bridge\nGo into the cave\n")
print("\n")

if response.strip().lower() == "go up the mountain":
    response = input("You encounter a bear. Do you:\nfight\nsneak\n")
    print("\n")

    if response.strip().lower() == "fight":

        if weapon:
            gold = gold * .8
            print(f"You killed the bear with your weapon\nYou dropped some gold during the fight\nYou continuted on in search of the dragon.\nGold remaining: {gold}")

        if not weapon:
            print("You did not bring a weapon, you have died")

    else:
        print("You sneak past the bear and continue in search of the dragon.")
#if response.strip().lower() == "go into the cave":








