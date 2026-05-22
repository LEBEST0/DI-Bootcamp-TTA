class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 =  Cat("cat 1",12)
cat2 =  Cat("cat 2",3)
cat3 =  Cat("cat 3",1)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    # ... code to find and return the oldest cat ...
    table=[cat1,cat2,cat3]
    max_age=max(cat1.age, cat2.age, cat3.age)
    for i in table:
        if i.age==max_age:
          return i
#Call the function to get the oldest cat.
old_cat=find_oldest_cat(cat1, cat2, cat3) 

# Step 3: Print the Oldest Cat’s Details
print(f"The oldest cat is {old_cat.name}, and is {old_cat.age} years old.")



#  Exercise 2 : Dogs

class Dog():
    def __init__(self,name,height):
        self.name=name
        self.height=height
    
    def bark(self):
        print(self.name, "goes woof!")
    
    def jump(self):
        print(self.name, "jumps ", self.height*2,"cm high! \n")


davids_dog=Dog("Davroy",0.6)
sarahs_dog=Dog("Sararo",0.4)
list_of_dog=[davids_dog,sarahs_dog]

for i in list_of_dog:
  print("This is the doc ", i.name,". This height is",i.height, )
  i.bark()
  i.jump()

# Step 4: Compare Dog Sizes

if list_of_dog[0].height>list_of_dog[1].height:
     print(list_of_dog[0].name, "is biggest than",list_of_dog[1].name)
else:
    print(list_of_dog[1].name, "is biggest than",list_of_dog[0].name)


# Exercise 3 : Who’s the song producer?

class Song():
    def __init__(self,lyrics:list):
        self.lyrics=lyrics
    
    def sing_me_a_song(self):
        for e in self.lyrics:
            print(e,"\n")
        
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()


# Exercise 4 : Afternoon at the Zoo

class Zoo():
    def __init__(self,zoo_name,animals):
        self.zoo_name=zoo_name
        self.animals=animals
    
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
           self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal,"is currently in the zoo")
    
    def sell_animal(self,animal_sold):
        for i in range(len(self.animals)):
            if self.animals[i]==animal_sold:
               del self.animals[i]
               break
    def sort_animals(self):
        new_animals=sorted(self.animals)
        dic={}
        for anim in new_animals:
            anim=anim.capitalize()
            if anim[0] in dic.keys():
                dic[anim[0]].append(anim)
            else:
                dic[anim[0]]=[anim]
        return dic
    
    def get_groups(self):

        for key,val in self.sort_animals().items():
            print(f"{key}: {val}")


#Step 2: Create a Zoo Object
    
zo=Zoo("Le premier zo",["Baboon","Bear","Cat","Giraffe","Lion","Zebra"])

#Step 3: Call the Zoo Methods

zo.add_animal("Panda")
zo.get_animals()
zo.sell_animal("Baboon")
zo.sort_animals()
zo.get_groups()



# This is the bonus

class Zoo1():
    def __init__(self,zoo_name,animals):
        self.zoo_name=zoo_name
        self.animals=animals
    
    def add_animal(self,*args):
        for new_animal in args:
           self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal,"is currently in the zoo 1")
    
    def sell_animal(self,animal_sold):
        for i in range(len(self.animals)):
            if self.animals[i]==animal_sold:
               del self.animals[i]
               break
    def sort_animals(self):
        new_animals=sorted(self.animals)
        dic={}
        for anim in new_animals:
            anim=anim.capitalize()
            if anim[0] in dic.keys():
                dic[anim[0]].append(anim)
            else:
                dic[anim[0]]=[anim]
        return dic
    
    def get_groups(self):

        for key,val in self.sort_animals().items():
            print(f"{key}: {val}")

zo1=Zoo1("Le deuxième zoo1",["Baboon","Bear","Cat","Giraffe","Lion","Zebra"])

zo1.add_animal("Panda")
zo1.get_animals()
zo1.sell_animal("Baboon")
zo1.sort_animals()
zo1.get_groups()