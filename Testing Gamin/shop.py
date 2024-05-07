
import json

class Shop:
    def __init__(self):
        self.inventory = self.load_inventory()

    # Load existing inventory from JSON file
    def load_inventory(self):
        try:
            with open("shop_inventory.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            create_shop_inventory(inventory_data)
            with open("shop_inventory.json", "r") as file:
                return json.load(file)

    # Save inventory to JSON file
    def save_inventory(self):
        with open("shop_inventory.json", "w") as file:
            json.dump(self.inventory, file, indent=4)

    # Display current shop inventory
    def display_inventory(self):
        print("Shop Inventory:")
        print("{:<5} {:<20} {:>10} {:<20} {:<10}".format("" ,"Item Name", "","price", "Stock"))
        for idx, item in enumerate(self.inventory):
            print("{:<5} {:<20} {:10} {:<20} {:<10}".format(item[0], item[1], item[2], item[3], item[4]))

    # Sell items from the shop
    def sell_item(self, item_index, quantity):
        if 0 <= item_index < len(self.inventory):
            item = self.inventory[item_index]
            if item[4] >= quantity:
                item[4] -= quantity
                self.save_inventory()
                print(f"You purchased {quantity} {item[1]} for {item[2] * quantity} gold.")
            else:
                print("Not enough stock.")
        else:
            print("Invalid item index.")

def main():
    shop = Shop()

    while True:
        print("\n1. Display Shop Inventory")
        print("2. Buy Item")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            shop.display_inventory()
        elif choice == "2":
            shop.display_inventory()
            item_index = int(input("Enter the index of the item you want to buy: "))
            quantity = int(input("Enter quantity: "))
            shop.sell_item(item_index, quantity)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

def create_shop_inventory(data):
    with open("shop_inventory.json", "w") as file:
        json.dump(data, file, indent=4)

inventory_data = [
    [0, "Small health potion", 10, "g", 99],
    [1, "Medium health potion", 25, "g", 99],
    [2, "Large health potion", 75, "g", 99],
    [3, "Ult potion", 100, "g", 99],
    [4, "DD potion", 100, "g", 99],
    [5, "Absorption potion", 50, "g", 99],
    [6, "Short Sword", 250, "g", 1],
    [7, "Long Sword", 250, "g", 1]
]


if __name__ == "__main__":
    main()



