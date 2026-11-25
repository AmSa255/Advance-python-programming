class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class Store:
    def __init__(self):
        self.grocery = []

    def add_item(self):
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        obj = Item(name, quantity, price)

        self.grocery.append(obj)

        print("Grocery item added successfully!")

    def display_items(self):
        if len(self.grocery) == 0:
            print("No items available.")
        else:
            print("\n--- Grocery List ---")

            for obj in self.grocery:
                print("Item Name:", obj.name)
                print("Quantity:", obj.quantity)
                print("Price:", obj.price)
                print("-------------------")

s = Store()

while True:
    print("\n1. Add Grocery Item")
    print("2. Display All Items")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        s.add_item()

    elif choice == 2:
        s.display_items()

    elif choice == 3:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
