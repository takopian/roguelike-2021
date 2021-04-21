class Entity:
    def __init__(self, x_coord: int, y_coord: int):
        self.x = x_coord
        self.y = y_coord

    def __str__(self):
        return ' '

    @property
    def color(self):
        return tuple([0, 0, 0])


class MovableEntity(Entity):
    def __init__(self, x_coord: int, y_coord: int):
        super().__init__(x_coord, y_coord)

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy
