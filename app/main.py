class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False,
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        if health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if not isinstance(animal, Carnivore) and animal.hidden is False:
            damage = 50
            animal.health = animal.health - damage
            if animal.health <= 0:
                Animal.alive.remove(animal)
