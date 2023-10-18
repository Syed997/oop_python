class Student:
    def __init__(self):
        print(self)
        print("a student obj created")
    def __init__(self, name, Id):
        self.name = name
        self.id = Id

#s1 = Student()
s2 = Student("Bob", 11)
s2.id = 33
print(s2.name)
print(s2.id)