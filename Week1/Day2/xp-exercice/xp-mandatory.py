# Exercise 1: Converting Lists into Dictionaries


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(dict(zip(keys,values)))




#  Exercise 2: Cinemax #2

family = {}

# Ajouter les membres de la famille
while True:
    nom = input("Enter family member's name (or 'done' to stop): ")
    
    if nom.lower() == "done":
        break
    
    age = int(input(f"Enter {nom}'s age: "))
    family[nom] = age

# calcul du prix

price = 0

print("\n--- Ticket Prices ---")
for cle, val in family.items():
    if val < 3:
        print(f"The ticket is free for {cle} ")
    elif 3 <= val < 12:
        price += 10
        print(f"Price of ticket for {cle} : $10")
    else:
        price += 15
        print(f"Price of ticket for {cle} : $15")

print(f"\nTotal cost for the family: ${price} ")



# Exercice 3: Zara


brand={
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": {
        "men", "women", "children", "home"
    },
    "international_competitors": {
        "Gap", "H&M", "Benetton"
    },
    "number_stores": 7000,
    "major_color": 
        {
            "France": "blue", 
            "Spain": "red", 
            "US": {
                "pink", "green"
            }
        }
}

brand["number_stores"]=2
print("Zara's client a women or children or men or she build for home")

brand.update({"country_creation":"Spain"})

if "international_competitors" in brand.keys():
    brand["international_competitors"].add("Desigual")

del brand["creation_date"]

print(list(brand["international_competitors"])[-1])
print(brand["major_color"]["US"])
print(len(brand.keys()))
print(brand.keys())

more_on_zara={
    "creation_date":"22/05/26",
    "number_stores": 10
}
brand.update(more_on_zara)

print(brand)



# Exercise 4 : Some Geography


def describe_city(city,country="Unknown"):
    print(f"{city} is in {country}")

describe_city("Cité du port", "Côte d'Ivoire")
describe_city("Shenzen", "Chine")
describe_city("Paris")


# Exercise 5 : Random


import random

def my_fonction(numb):
    nb_g=random.randint(1, 100)

    if nb_g==numb:
        print("Success!")
    else: 
        print("Vous venez de perdre")
        print(f"Fail! Your number: {numb} , Random number: {nb_g}")


my_fonction(3)


# Exercise 6 : Let’s create some personalized shirts !


#Step 1
def make_shirt(size="large",text="I love Python"): #step 4
    print(f" the size of the shirt is {size} and the text content is: {text}\n ") #step 2

make_shirt("L","This the text of test") #step 3

# step 5
make_shirt()
make_shirt("Medium","This the text of test")
make_shirt("small","This the text for any shirt")

#step 6: bonus
make_shirt(size="small", text="Hello!")




#  Exercise 7 : Temperature Advice



def get_random_temp():
    
    #return random.randint(-10, 40)
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


    return random.uniform(-10, 40)

def main():
    temp=get_random_temp()

    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp< 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0<=temp< 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16<=temp<= 23:
        print("Nice weather.")
    elif 24<=temp< 32:
        print("A bit warm, stay hydrated.")
    elif 32<=temp< 40:
        print("It’s really hot! Stay cool.")

main()


# Exercise 8: Pizza Toppings
price=10
s=0
pizza={}
while True:
    user_m=input("Enter pizza toppings: ")
    if user_m == "quit":
        break
    else: 
        price=price+s
        pizza.update({user_m:price})
        print(f"Adding {user_m} to your pizza.")
        s=s+2.5
s=0
for cle,val in pizza.items():
    print(f"This one topping: {cle}")
    s=s+val
print(f"Total price is: {s}")


 