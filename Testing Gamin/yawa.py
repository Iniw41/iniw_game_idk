class Mob:
    def __init__(self, name, damage, health):
        """
        Initialize a mob with the given attributes.

        Args:
            name (str): The name of the mob.
            damage (int): The damage dealt by the mob.
            health (int): The health points of the mob.
        """
        self.name = name
        self.damage = damage
        self.health = health
        self.max_health = health  # Store the maximum health

    def attack(self, target_mob):
        """
        Simulate an attack by this mob on another mob.

        Args:
            target_mob (Mob): The target mob to attack.

        Returns:
            str: A message describing the attack outcome.
        """
        target_mob.health -= self.damage
        if target_mob.health <= 0:
            return f"{self.name} defeated {target_mob.name}!"
        else:
            return f"{self.name} attacked {target_mob.name}. {target_mob.name}'s health: {target_mob.health}"

    def info(self):
        """
        Display information about the mob's health.

        Returns:
            str: A message with current and maximum health.
        """
        return f"{self.name} - Current Health: {self.health}/{self.max_health}"

# Example usage:
mob1 = Mob(name="Goblin", damage=10, health=50)
mob2 = Mob(name="Orc", damage=15, health=70)

print(mob1.attack(mob2))
print(mob2.attack(mob1))

print(mob1.info())
print(mob2.info())
