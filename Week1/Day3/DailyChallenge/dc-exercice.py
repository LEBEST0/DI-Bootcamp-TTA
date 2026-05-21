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
    
    def get_animal_types(self):
        animals_list=sorted(self.animals.keys())
        return animals_list

    def get_short_info(self):
        liste=self.get_animal_types()
        fin=1
        d=""
        
        print(f"{self.name} farm has ",end="")
        for nom, nb in self.animals.items(): 
            pluriel="s" if nb>1 else ""
            part=f"{nom}{pluriel}"
            
           
            d=d+f"{part},"
            
            if fin==len(self.animals):
                d=d[0:len(d)-1]
            fin+=1
        print(d)
            
            

            
            
        


          
        

# Test the code 
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('cheap')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
macdonald.get_animal_types()
macdonald.get_short_info()

# Bonus: Expand The Farm

# Step 6: Implement the get_animal_types Method

