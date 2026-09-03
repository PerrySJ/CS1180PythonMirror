import random

#Variables
weapon = False
death = False
gold = random.randint(50, 500)

#if gold >=200:
 #   print("You're rich!")
#else:
 #   print("Broke")

name = input("What is your name?\n")

print(f"Hello {name}!")

print(f"It seems you have brought {gold} gold with you today!")

response = input("Would you like to purchase a weapon? ")

if response.strip().lower() == "yes":
    input(f"What weapon would you like? You have {gold} gold\nGreatsword:150g\nDagger:50g")




