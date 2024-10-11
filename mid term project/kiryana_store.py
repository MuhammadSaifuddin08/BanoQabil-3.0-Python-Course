"""
Huzaifah Saifuddin
Muhammad Saifuddin
huzaifahsaifuddin@gmail.com
msaifuddin77887@gmail.com

Problem Statement: This system will facilitate the management of grocery items, allow customers to shop for items, and enable the store admin to manage inventory.
"""
class Store:
    def __init__(self):
        # Initializing store items with their prices and stock quantities
        self.items = {
            "Rice": {"price": 50, "stock": 10},
            "Wheat": {"price": 40, "stock": 10},
            "Flour": {"price": 30, "stock": 10},
            "Oil": {"price": 100, "stock": 10},
            "Daal": {"price": 60, "stock": 10},
            "Soap": {"price": 20, "stock": 10},
            "Surf": {"price": 25, "stock": 10}
        }
        # Initializing an empty cart for the user
        self.cart = {}

    def admin_login(self):
        # Admin login with a fixed ID and password
        while True:
            if input("Enter Admin ID: ") == "admin@gmail.com" and input("Enter Admin Password: ") == "123456":
                print("Admin login successful!")
                break
            else:
                print("Incorrect ID or password. Please try again.")

    def show_items(self):
        # Displaying all available items with their prices and stock quantities
        for item, details in self.items.items():
            print(f"{item}: {details['stock']} in stock, Price: {details['price']} per unit")

    def add_to_cart(self):
        # Adding an item to the user's cart
        item = input("Enter the item name to add to cart: ").capitalize()
        if item in self.items and self.items[item]["stock"] > 0:
            quantity = int(input(f"Enter the quantity of {item} to add: "))
            if quantity <= self.items[item]["stock"]:
                self.items[item]["stock"] -= quantity
                self.cart[item] = self.cart.get(item, 0) + quantity
                print(f"{quantity} {item}(s) added to cart.")
            else:
                print(f"Only {self.items[item]['stock']} {item}(s) available.")
        else:
            print(f"{item} is not available or out of stock.")

    def remove_from_cart(self):
        # Removing an item from the user's cart
        item = input("Enter the item name to remove from cart: ").capitalize()
        if item in self.cart:
            quantity = int(input(f"Enter the quantity of {item} to remove: "))
            if quantity <= self.cart[item]:
                self.cart[item] -= quantity
                self.items[item]["stock"] += quantity
                if self.cart[item] == 0:
                    del self.cart[item]
                print(f"{quantity} {item}(s) removed from cart.")
            else:
                print(f"You only have {self.cart[item]} {item}(s) in your cart.")
        else:
            print(f"{item} is not in your cart.")

    def view_cart(self):
        # Displaying all items currently in the user's cart
        if not self.cart:
            print("Your cart is empty.")
        else:
            for item, quantity in self.cart.items():
                print(f"{item}: {quantity}")

    def generate_bill(self):
        # Generating a bill for the items in the user's cart
        total = 0
        for item, quantity in self.cart.items():
            price = self.items[item]["price"]
            total += price * quantity
            print(f"{item}: {quantity} x {price} = {price * quantity}")
        print(f"Total bill: {total}")

    def change_stock(self):
        # Admin changing the stock quantity of an item
        item = input("Enter the item name to change stock quantity: ").capitalize()
        if item in self.items:
            self.items[item]["stock"] = int(input(f"Enter the new quantity for {item}: "))
            print(f"The stock quantity for {item} has been updated.")
        else:
            print(f"{item} is not available in the store.")

    def add_stock_item(self):
        # Admin adding a new item to the inventory
        item = input("Enter the name of the new item: ").capitalize()
        if item in self.items:
            print(f"{item} already exists in the store.")
        else:
            price = int(input(f"Enter the price for {item}: "))
            quantity = int(input(f"Enter the initial stock quantity for {item}: "))
            self.items[item] = {"price": price, "stock": quantity}
            print(f"New item {item} added.")

    def admin_menu(self):
        # Admin menu for managing the store inventory
        while True:
            print("\nAdmin Menu\n1. View stock\n2. Change stock\n3. Add new stock item\n4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.show_items()
            elif choice == "2":
                self.change_stock()
            elif choice == "3":
                self.add_stock_item()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def user_menu(self):
        # User menu for shopping
        while True:
            print("\nUser Menu\n1. View items\n2. Add to cart\n3. Remove from cart\n4. View cart\n5. Checkout")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.show_items()
            elif choice == "2":
                self.add_to_cart()
            elif choice == "3":
                self.remove_from_cart()
            elif choice == "4":
                self.view_cart()
            elif choice == "5":
                self.generate_bill()
                break
            else:
                print("Invalid choice. Please try again.")

    def main(self):
        # Main method to start the application
        while True:
            user_type = input("Are you a User or Admin? (Enter 'User' or 'Admin'): ").strip().lower()
            if user_type == "admin":
                self.admin_login()
                self.admin_menu()
            elif user_type == "user":
                self.user_menu()
            else:
                print("Invalid choice. Please restart the program and enter 'User' or 'Admin'.")

if __name__ == "__main__":
    store = Store()
    store.main()
