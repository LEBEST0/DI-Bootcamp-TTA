# === Exercice 1 ===

"""
print("=== What is the season ? ===")
print("Enter the number of month and you will know the month")


month=int(input("Enter the month's number: "))

if month in range(3,6):
    print("The season is Spring")
elif month in range(6,9):
    print("The season is Summer")
elif month in range(9,12):
    print("The season is Autumn")
elif month in [0,1,2,12]:
    print("The season is Winter")
else:
    print("The month with this number doesn't exist")

"""

# === Exercice 2 ===

"""

values=range(1,21)
for i in values:
    print(f"{i}")
print("===== Printing of index even=====")
for j in values:
    if j%2==0:
        print(f"{j}")
    else:
        continue
    
"""

# ==== Exercice 3 ====

"""
nom="OKEY"

while nom != "AKRE ANGE DAVID":
    print("What is your name")
    nom=input("Enter your name: ")

"""

# ==== Exercice 4 ====

"""
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# First we must got the number of user en then use index method to search the position of user's name
print(names.index(input("Enter your name: ")))

"""

# ==== Exercice 5 ====

"""
first=int(input("Enter the 1st number: "))
second=int(input("Enter the 2nd number: "))
third=int(input("Enter the 3rd number: "))

print("The greatest number is ", max(first,second,third))

"""

# ==== Exercice 6 =====

"""
import random
# numb is the number enter by user
win=0
lost=0
ne=1
while ne==1 :
    numb=int(input("Enter a number between 1 and 9: "))
    rand_num=random.randint(1,9)
    if rand_num==numb:
        print("Winner")
        win+=1
    else:
        lost+=1
        print("Better luck next time.")
    print("Print 1 for yes or 0 for not. If you write other option, this will be consider like you would not continue")
    ne=int(input("Would you continue ? "))
    if ne==0:
        print(f"Total games: {lost+win}")
        print(f"Total winning: {win}")
        print(f"Total losing: {lost}")

"""