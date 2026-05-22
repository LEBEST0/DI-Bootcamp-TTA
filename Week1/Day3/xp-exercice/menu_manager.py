class MenuManager:
    def __init__(self,menu):
        self.menu=menu
    
    def add_item(self,name, price, spice, gluten):
        self.menu.append({"name":name, "price":price, "spice":spice, "gluten":gluten})
    def update_item(self,name, price, spice, gluten):
        for elt in self.menu:
            if elt["name"].lower()==name.lower() :
                self.menu.update({"price":price, "spice":spice, "gluten":gluten})
            
        print(f"This dish named {name} doesn't exist in the menu")
    
    def remove_item(self,name):
        dish=[elt for elt in self.menu if elt["name"]==name]
        if dish:
            for element in dish:
                self.menu.remove(element)
                print(self.menu)
        else:
            print("This dish doesn't")


l=MenuManager([{"name":"d 1", "price": "p 1", "spice": "s 1", "gluten":"g 1"},{"name":"d 2", "price": "p 2", "spice": "s 2", "gluten":"g 2"},{"name":"d 3", "price": "p 3", "spice": "s 3", "gluten":"g 3"}])
l.remove_item("d 1")