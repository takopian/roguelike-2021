from src.server.game.Engine import Engine
from src.server.game.Entity import MovableEntity, Entity


class Command:
    def invoke(self, engine: Engine, entity: Entity) -> None:
        raise NotImplementedError()


class EscapeCommand(Command):
    def invoke(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()


class MovementCommand(Command):
    def __init__(self, dx: int, dy: int):
        self.dx = dx
        self.dy = dy

    def invoke(self, engine: Engine, entity: MovableEntity) -> None:
        new_x = entity.x + self.dx
        new_y = entity.y + self.dy
        if not engine.game_map.in_bounds(new_x, new_y):
            return
        if not engine.game_map.tiles["walkable"][new_x, new_y]:
            return
        entity.move(self.dx, self.dy)
