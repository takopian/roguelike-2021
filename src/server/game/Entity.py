
class Entity:
    def __init__(self, x_coord: int, y_coord: int, char: str):
        self.x = x_coord
        self.y = y_coord
        self.char = char


class MovableEntity(Entity):
    def __init__(self, x_coord: int, y_coord: int, char: str):
        super().__init__(x_coord, y_coord, char)

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy
