from .Entity import MovableEntity


class Character(MovableEntity):
    def __init__(self, x_coord: int, y_coord: int, char: str):
        super().__init__(x_coord, y_coord, char)
        self.health = 100
