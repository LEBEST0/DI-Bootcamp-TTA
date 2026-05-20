# Exercice 1: Hello World

print("Hello world \n"*4 )


# Exercice 2: Some Math


print((99**3)*8)

# Exercice 3: What is the output?



print(15 < 8)  # False
print(5 < 3)  # False
print(3 == 3) # True
print(3 == "3") # False
print("3" > 3)   # ErrorType
print("Hello" == "hello") #False

# Exercice 4: Your computer brand

computer_brand= "HP"
print(f"I have a {computer_brand} computer.")

# Exercice 5: Your information


name="AKRE ANGE DAVID"
age=22
shoe_size=42
info=f"Hello, my name's {name}, I'm {age} years old. I love technology and wear shoe with size {shoe_size} "

print(info)


# Exercise 6: A & B


a=1
b=2

if a>b:
    print("Hello World") 
    



# Exercise 7: Odd or Even



numb=int(input("Enter your number: "))
if numb%2==0:
    print("This number is even")
else: 
    print("This number is odd")


# Exercice 8 : What’s your name?

mon_nom = "AKRE" 
nom = input("Enter you name : ")

if nom.lower() == mon_nom.lower():
    print("No way ! We have the same first name, are we twins or ? 😂")
else:
    print(f"Ah {nom}... Pas aussi bien que {mon_nom} comme prénom...")


# Exercice  9:  Tall enough to ride a roller coaster

height = int(input("Enter your height in cm: "))

if height > 145:
    print("You are tall enough to ride the roller coaster! ")
else:
    print("Sorry, you need to grow some more to ride! 📏")