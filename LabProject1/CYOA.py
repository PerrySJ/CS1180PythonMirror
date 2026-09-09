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
elif response.strip().lower() == "go into the cave":
    response = input("There is a foundtain in the cave. Do you:\nDrink from it\nContinue on\n")
    print("\n")
    if response.strip().lower() == "drink from it":
        death = True
        print("The fountain was poison, you have died")
        
    else:
        print("You throw some coin into the foundtain and continue forward through the cave, in search of the dragon\n")
        gold = gold * .8
        print(f"Gold remaining: {gold}\n")

elif response.strip().lower() == "cross the bridge":
    response = input("There is a troll guarding the bridge, he wants gold to pass. Do you:\nGive gold\nDon't give gold\n")
    print("\n")
    if response.strip().lower() == "give gold":
        if gold >= 200:
            print("You pay the trolls fee, and continue on in search of the dragon.\n")
            gold = gold * .5
            print(f"Gold remaining: {gold}")
            print("\n")
        else:
            if weapon == True:
                print("You did not have enough gold, but you have slain the troll with your weapon.\nYou drop some gold during the battle\nYou carry on in search of the dragon")
                gold = gold * .8
                print(f"Gold remaining: {gold}")
                print("\n")
            else:
                death = True
                print("You did not have enough gold, and without a weapon, you have been slain by the troll")
    else:
        if weapon == True:
            print("You refuse to pay the fee, but thankfully you had a weapon.\nThe troll has been slain\nYou drop some gold during the battle\n You carry on in search of the dragon\n")
            gold = gold * .8
            print(f"Gold remaining: {gold}")
            print("\n")
        else:
            death = True
            print("Without having a weapon, refusing to pay the trolls fee resulted in your death")
            print("\n")
else:
    print("Incorrect response, program terminated")
    death = True

if death == False:
    response = input("It has been quite the search but you have finally found the Dragon. Do you:\nFight the dragon\nRun away\n")

    if response.strip().lower() == "fight the dragon":
        if weapon == True:
            print(f"You have slain the dragon with your weapon. Congratulations, you are victorious {name}.\n")
            print(f"You won with {gold} remaining")
        else:
            if gold >= 75:
                print("You do not have a weapon to fight, but you threw your remaining gold to distract the dragon")
                gold = 0
                print("You succesfully snuck past the dragon, maybe you can defeat him another time")
            elif gold < 75:
                print("You did not have enough gold to distract the dragon. Without a weapon, you have died")
                death = True
    else:
        print(f"After all this journey, you have chosen the cowards way out {name}, You are not victorious")

print("Game over")











