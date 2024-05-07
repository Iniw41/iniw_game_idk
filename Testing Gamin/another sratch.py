from pydantic.dataclasses import dataclass

@dataclass
class Character:
    health: int
    attack: int
    speed: int

tank = Character(health=1000, attack=10, speed=10)
print(tank.attack)