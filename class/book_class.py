class Book:
    def __init__(self, name, author) -> None:
        self.name = name
        self.author = author
        self.price = 0
    def set_price(self, price):
        self.price = price
    def get_price(self):
        return self.price
    def details(self):
        print("Name:", self.name,
              "\nAuthor:", self.author,
              "\nPrice:", self.price, "BDT")
    
