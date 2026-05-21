class Farm:
    def __init__(self,farm_name):
        self.name=farm_name
        self.animals={}
    
    def add_animal(self,animal_type,count=1):

        if animal_type in self.animals.keys():
            self.animals[animal_type]+=1
        else:
            self.animals[animal_type]=count
        
    def get_info(self):
        s=""
        for name, nb in self.animals.items():
             s= s + f"{name} : {nb}\n"
        else:    
          return s+"\n E-I-E-I-0!"
          
        

# Test the code 
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())