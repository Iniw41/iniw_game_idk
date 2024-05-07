from pydantic.dataclasses import dataclass

@dataclass
class Weapon:
    weapon_name:str
    weapon_add_dmg: int

stick = Weapon(weapon_name="stick", weapon_add_dmg=10)
Short_sword = Weapon(weapon_name=" Short Sword", weapon_add_dmg=50)
Long_sword = Weapon(weapon_name=" Long Sword", weapon_add_dmg=75)

