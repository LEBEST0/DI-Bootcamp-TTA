"""
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# step 1
class Siamese(Cat):
    pass

#step 2

all_cats=[Bengal("chien Begal"),Chartreux("chien Chartreux"),Siamese("chien Siamese")]

#step 3

sara_pets=Pets(all_cats)

#Step 4: Take Cats for a Walk

sara_pets.walk()
"""

#Exercise 2: Dogs
"""


class Dog:
    def __init__(self, name, age, weight):
        self.name=name
        self.age=age
        self.weight=weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        pow1=self.weight*self.run_speed()
        pow2=other_dog.weight * other_dog.run_speed()
        if pow1>pow2:
            return f"{self.name} won"
        elif  pow2>pow1:
            return f"{other_dog.name} won"
        else:
            return "both are winner"

# Step 2: Create dog instances

dog1=Dog("dog 1",2,10)
dog2=Dog("dog 1",5,9)
dog3=Dog("dog 1",3,11)
# Step 3: Test dog methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))


"""
#Exercise 3: Dogs Domesticated
"""
import random
from dog_cl import Dog

class PetDog(Dog):

    def __init__(self, name, age, weight, trained=False):

        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):

        print(self.bark())
        self.trained = True

    def play(self, *args):

        dogs = [dog.name for dog in args]

        dogs.insert(0, self.name)

        s = ", ".join(dogs)

        print(f"{s} all play together")

    def do_a_trick(self):

        tricks = [
            "does a barrel roll",
            "stands on his back legs",
            "shakes your hand",
            "plays dead"
        ]

        if self.trained:

            nb = random.randint(0, 3)

            print(f"{self.name} {tricks[nb]}")


p1 = PetDog("Rocky", 3, 20)
p2 = PetDog("Max", 2, 15)
p3 = PetDog("Buddy", 4, 18)

p1.train()

p1.play(p2, p3)

p1.do_a_trick()

p1=PetDog("Dog 1",12,50,False)
p2=PetDog("Dog 2",1,5,True)
p3=PetDog("Dog 3",2,6,False)
p1.train()
p1.play(p2,p3)
p1.do_a_trick()
"""

# xercise 4: Family and Person Classes

# Step 1: Create the Person class

class Person:

    def __init__(self, first_name, age):

        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):

        return self.age >= 18


# Step 2: Create the Family class

class Family:

    def __init__(self, last_name):

        self.last_name = last_name
        self.members = []

    # Method to add a new family member
    def born(self, first_name, age):

        person = Person(first_name, age)

        person.last_name = self.last_name

        self.members.append(person)

        print(f"{person.first_name} {person.last_name} has been added to the family.")

    def check_majority(self, first_name):

        for person in self.members:

            if person.first_name == first_name:

                if person.is_18():

                    print(
                        "You are over 18, your parents Jane and John accept that you will go out with your friends"
                    )

                else:

                    print(
                        "Sorry, you are not allowed to go out with your friends."
                    )

                return

        print("Person not found in the family.")

    def family_presentation(self):

        print(f"\nThe {self.last_name} Family")

        print("-" * 30)

        for person in self.members:

            print(f"Name: {person.first_name} , Age: {person.age}")


# ---------------- TEST ---------------- #

# Create a family
family1 = Family("Smith")

# Add family members
family1.born("John", 45)
family1.born("Emma", 17)
family1.born("Michael", 21)

# Check majority
family1.check_majority("Emma")

family1.check_majority("Michael")

# Display family information
family1.family_presentation()