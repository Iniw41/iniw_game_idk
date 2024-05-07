import random
import Mob as stat

class Game:
    def __init__(self):
        # Define the mobs
        self.mob1 = stat.Mob("Goblin", 10, 50,1)
        self.mob2 = stat.Mob("Orc", 15, 70, 1)
        self.mob3 = stat.Mob("Ogre", 15, 150, 1)
        self.mobs = [self.mob1, self.mob2, self.mob3]

    def start(self):
        # Determine the number of enemies based on probabilities
        num_enemies = random.choices([1, 2, 3], weights=[30, 60, 10])[0]

        # Randomly select mobs from the list
        current_mobs = random.sample(self.mobs, num_enemies)

        print("Number of enemies:", num_enemies)
        print("Current mobs:", [mob.name for mob in current_mobs])

        # Perform actions
        self.action(current_mobs)

    def action(self, current_mobs):
        while True:
            print("Select Action: A. Attack B.Inventory C.Player Info")
            option = str.upper(input(": "))
            if option == 'A':
                self.attack_action(current_mobs)
            elif option == 'B':
                pass
            elif option == 'C':
                pass
            else:
                print("Invalid option.")

    def attack_action(self, current_mobs):
        while True:
            if not any(mob.health > 0 for mob in current_mobs):
                break
            else:
                print("Select which mob to attack:")
                for i, mob in enumerate(current_mobs, start=1):
                    print(f"{i}. Attack {mob.name}")

                option = input(": ")
                if option.isdigit():
                    option = int(option)
                    if 1 <= option <= len(current_mobs):
                        selected_mob = current_mobs[option - 1]
                        # Assuming character is defined elsewhere
                        character.attack(selected_mob)
                        print(character.attack(selected_mob))
                        print(selected_mob.info())
                        break
                    else:
                        print("Invalid option.")
                else:
                    print("Invalid input. Please enter a number.")

character = input("Input Character name: ")
character = stat.Mob(f"{character}", 10, 100, 1)
# Example usage
game = Game()
game.start()


