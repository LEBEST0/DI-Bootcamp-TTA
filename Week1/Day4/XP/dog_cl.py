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
