class Student:
    def __init__(self):
        print(self)
        print("a student obj created")
    def __init__(self, name, Id):
        self.name = name
        self.id = Id
    def details(self):
        print("Name:",self.name, "ID:", self.id )

#s1 = Student()
#s2 = Student("Bob", 11)
#s2.id = 33
#s2.details()

class House:
    def __init__(self) -> None:
        self.window = 4
        self.door = 2

    def view(self):
        print("Windows:", self.window, "Doors:", self.door)

h1 = House()
h2 = House()

h1.window = 6
h1.door = 3
h2.door = 4
h2.window = 8
h1.view()
h2.view()
