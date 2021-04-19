class Command:
    pass


class Move(Command):
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
