import json
import shop

class Inventory:
    def __init__(self):
        self.inventory = self.load_inventory()

    # Load existing inventory from JSON file
    def load_inventory(self):
        try:
            with open("inventory.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            create_player_inventory(player_inventory_data)
            with open("inventory.json", "r") as file:
                return json.load(file)


    # Save inventory to JSON file
    def save_inventory(self):
        with open("inventory.json", "w") as file:
            json.dump(self.inventory, file, indent=4)

    # Display current inventory
    def display_inventory(self):
        print("Current Inventory:")
        print("{:<5} {:<20} {:>10} {:<20} {:<10}".format("" ,"Item Name","", "Price", "Quantity"))
        for item in self.inventory:
            print("{:<5} {:<20} {:>10} {:<20} {:<10}".format(item[0], item[1], item[2], item[3], item[4]))

    # Add items to inventory
    def add_item(self, item_name, price, quantity):
        for item in self.inventory:
            if item[1] == item_name:
                item[4] += quantity
                break
        else:
            self.inventory.append([item_name, price, quantity])
        self.save_inventory()

def main():
    player_inventory = Inventory()
    shop_inventory = shop.Shop()

    while True:
        print("\n1. Display Shop Inventory")
        print("2. Buy Item")
        print("3. Display Player Inventory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            shop_inventory.display_inventory()
        elif choice == "2":
            shop_inventory.display_inventory()
            item_index = int(input("Enter the index of the item you want to buy: "))
            quantity = int(input("Enter quantity: "))
            item = shop_inventory.inventory[item_index]
            if item[4] >= quantity:
                shop_inventory.sell_item(item_index, quantity)
                player_inventory.add_item(item[1], item[2], quantity)
            else:
                print("Not enough stock in the shop.")
        elif choice == "3":
            player_inventory.display_inventory()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

def create_player_inventory(data):
    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

player_inventory_data = [
    [0, "Small health potion", 10, "g", 0],
    [1, "Medium health potion", 25, "g", 0],
    [2, "Large health potion", 75, "g", 0],
    [3, "Ult potion", 100, "g", 0],
    [4, "DD potion", 100, "g", 0],
    [5, "Absorption potion", 50, "g", 0],
    [6, "Short Sword", 250, "g", 0],
    [7, "Long Sword", 250, "g", 0]
]

if __name__ == "__main__":
    main()
