# Exercise 1 : Geometry
"""
class Circle():
  def __init__(self, radius=10):
    self.radius=radius 
  def area(self):
    return 3.14*(self.radius)**2
  def perimeter(self):
    return 2*3.14*self.radius
  def print_c(self):
    print("This is the geometrical definition of the cercle: \n")
    print(f"Perimetre:",self.perimeter())
    print(f"area:",self.area())

c1=Circle(12)
c1.print_c()
"""


# Exercise 2 : Custom List Class
"""
import random
class MyList():
  def __init__(self,liste:list):
      self.liste=liste
  def reverse(self):
      return self.liste.reverse()
  def ordonner(self):
     return self.liste.sort()
  
  def generate(self):
     return [random.randint(1,8) for e in range(len(self.liste)) ]

l1=MyList(["ok","ca","àpioj"])
print(l1.generate())
"""