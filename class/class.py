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
s2 = Student("Bob", 11)
s2.id = 33
s2.details()
