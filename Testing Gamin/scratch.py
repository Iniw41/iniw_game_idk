import random
class Mob:
    def __init__(self, name, damage, health, level):

        self.name = name
        self.damage = damage
        self.health = health
        self.max_health = health  # Store the maximum health
        self.level = level

mob1 = Mob(name="Goblin", damage=10, health=50, level=5)
mob2 = Mob(name="Goblin", damage=10, health=50, level=2)


current_level = 1
exp_gain = mob1.level * 10 + (100*0.25)
exp_need_lvl_up = current_level * 10 * 1.25
current_exp =  exp_gain

while current_exp >= exp_need_lvl_up:
    current_level += 1
    current_exp -= exp_need_lvl_up
    exp_need_lvl_up = current_level * 10 * 1.25

print(f"Current Level: {current_level}")
print(f"current XP: {int(current_exp)} / {int(exp_need_lvl_up)} ")

current_gold = 0
g = current_gold
gold_gain = random.randint(5, 10) * (mob1.level * 2 * 0.25)


print(f"{int(gold_gain)}g")
#random mob drops
mobdrops = random.choices([1, 2, 3], weights=[30, 60, 10])[0]

"""def attack_action():
    while True:
        if mob1.health and mob2.health == 0:
            break
        else:
            print(f"A. Attack {mob1.name}, B.Attack {mob2.name}")
            option = str.upper(input(":"))
            if option == 'A':
                character.attack(mob1)
                print(character.attack(mob1))
                print(mob1.info())
            elif option == 'B':
                character.attack(mob2)
                print(character.attack(mob2))
                print(mob2.info())
            else:
                print("Invalid")"""

"""import main as stat
import random
character = input("Input Character name: ")
character = stat.Mob(name=f"{character}", damage=10, health=100, level=1)

# Define the mobs
mob1 = stat.Mob(name="Goblin", damage=10, health=50, level=1)
mob2 = stat.Mob(name="Orc", damage=15, health=70, level=1)
mob3 = stat.Mob(name="Oger", damage=15, health=150, level=1)

# Create a list of mobs
mobs = [mob1, mob2, mob3]
# Determine the number of enemies based on probabilities
num_enemies = random.choices([1, 2, 3], weights=[30, 60, 10])[0]
# Randomly select mobs from the list
current_mobs = random.sample(mobs, num_enemies)

print("Number of enemies:", num_enemies)
print("Current mobs:", [mob.name for mob in current_mobs])

def action():
    while True:
        print("Select Action: A. Attack B.Inventory C.Player Info")
        option = str.upper(input(":"))
        if option == 'A':
            attack_action(current_mobs)
        elif option == 'B':
            pass
        elif option == 'C':
            pass
def attack_action(current_mobs):
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
                    character.attack(selected_mob)
                    print(character.attack(selected_mob))
                    print(selected_mob.info())
                    break
                else:
                    print("Invalid option.")
            else:
                print("Invalid input. Please enter a number.")"""
"""import Player_stats as Pstat
import json
class player_cration:
    @staticmethod
    def create_character():
        character = player_name
        while True:
            if character.isalpha():
                try:
                    with open("Player_data.json", "r") as file:
                        data = json.load(file)
                except FileNotFoundError:
                    data = {}


                    data[character] = {
                        "damage":character.damage,
                        "health":character.health,
                        "level":character.level
                    }
                    with open("Player_data.json", "w") as file:
                        json.dump(data, file)
            else:
                print("Pls Enter a Valid Name")

player_name = input("Enter Character Name: ")"""
