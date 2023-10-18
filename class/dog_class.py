class Dog:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
    def update_color(self, color):
        self.color = color
    def poke(self):
        print("Name:", self.name, "Color:", self.color)
d1 = Dog("rover", "brown")
d2 = Dog("tomy", "white")
d1.poke()
d2.poke()
d2.update_color("black")
d2.poke()