from __future__ import annotations
from .Engine import Engine
from .Entity import Entity, MovableEntity


class Action:
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise NotImplementedError()


class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()


class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity: MovableEntity) -> None:
        new_x = entity.x + self.dx
        new_y = entity.y + self.dy
        if not engine.game_map.in_bounds(new_x, new_y):
            return
        if not engine.game_map.tiles["walkable"][new_x, new_y]:
            return
        entity.move(self.dx, self.dy)
