class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.wheel = 4
    def view(self):
        print("The model year of this", self.name, "is", self.model)
        print("This is a", self.wheel, "driven vehicle")

c1 = Car("BMW", 2016)
c2 = Car("Audi", 2018)
c1.view()
c2.view()