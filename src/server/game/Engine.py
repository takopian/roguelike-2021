from typing import Set

from tcod.console import Console
from tcod.context import Context

from src.server.game.Entity import Entity, MovableEntity
from src.server.game.map.GameMap import GameMap


class Engine:
    def __init__(self, entities: Set[Entity], game_map: GameMap, player: MovableEntity):
        self.entities = entities
        self.game_map = game_map
        self.player = player

    def handle_action(self, action) -> None:
        if action is not None:
            print(f"Performing {action}")
            action.invoke(self, self.player)

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, str(entity))
        console.print(self.player.x, self.player.y, str(self.player))
        context.present(console)

        console.clear()
