
class Player:
    def __init__(self, name, damage, health, level):
        """
        Initialize a mob with the given attributes.

        Args:
            name (str): The name of the player.
            damage (int): The damage dealt by the player.
            health (int): The health points of the mob.
        """
        self.name = name
        self.damage = damage
        self.health = health
        self.max_health = health  # Store the maximum health
        self.level = level
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
            target_mob.health = 0
        if target_mob.health <= 0:
            return f"{self.name} defeated {target_mob.name}!"
        else:
            return f"{self.name} attacked {target_mob.name}. {target_mob.name}'s health: {target_mob.health}"
    def level_up(self, target_mob):
        if target_mob.health == 0:
            current_level = self.level
            exp_gain = target_mob.level * 10
            exp_need_lvl_up = current_level * 100 * 1.25
            current_exp = 0 + exp_gain

            while current_exp >= exp_need_lvl_up:
                current_level += 1
                current_exp -= exp_need_lvl_up
                exp_need_lvl_up = current_level * 100 * 1.25
    def info(self):
        """
        Display information about the mob's health.

        Returns:
            str: A message with current and maximum health.
        """
        return f"{self.name} - Current Health: {self.health}/{self.max_health}"

