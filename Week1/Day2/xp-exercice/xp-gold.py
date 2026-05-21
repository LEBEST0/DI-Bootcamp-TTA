
# Exercise 1: Birthday Look-up


"""
birthdays=[{
        "name":"personne 1",
        "birthday":"2001/02/15"
    },
    {
        "name":"personne 2",
        "birthday":"2000/08/01"
    },
    {
        "name":"personne 3",
        "birthday":"2003/04/22"
    },
    {
        "name":"personne 4",
        "birthday":"1950/07/18"
    },
    {
        "name":"personne 5",
        "birthday":"2025/01/24"
    }]
    


print("Welcome, dear user. \n You can look up the birthday of person in the list")
user_message=input("Enter the name of the person: ")

for elt in birthdays:
    if elt["name"]==user_message:
        print(f"This is the birthday of {user_message}: {elt["birthday"]}")

"""

# Exercise 2: Birthdays Advanced
"""

birthdays=[{
        "name":"personne 1",
        "birthday":"2001/02/15"
    },
    {
        "name":"personne 2",
        "birthday":"2000/08/01"
    },
    {
        "name":"personne 3",
        "birthday":"2003/04/22"
    },
    {
        "name":"personne 4",
        "birthday":"1950/07/18"
    },
    {
        "name":"personne 5",
        "birthday":"2025/01/24"
    }]

print("========= LISTE OF PERSON============")

for i in range(len(birthdays)):
    print(f"{i+1}-{birthdays[i]["name"]}\n")

name=input("Write a name: ")
is_find=False

for elt in birthdays:
    if elt["name"]==name:
        print(f"This is the birthday of {name}: {elt["birthday"]}")
        break
else: 
    print("Sorry, we don’t have the birthday information for person's name")

"""

# Exercise 3: Check the index

import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    nb = 0        # compteur de lancers
    l, q = -1, -2 # valeurs différentes pour démarrer la boucle
    while l != q:
        l = throw_dice()
        q = throw_dice()
        nb += 1
    return nb

def main():
    results = []  # liste pour stocker les résultats des 100 doubles
    
    for _ in range(100):
        results.append(throw_until_doubles())
    
    total = sum(results)
    average = total / len(results)
    
    print(f"Total throws: {total}")
    print(f"Average throws to reach doubles: {round(average, 2)}.")

main()