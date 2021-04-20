from .Entity import Entity, MovableEntity
from .map.GameMap import GameMap
from typing import Set
from tcod.context import Context
from tcod.console import Console


class Engine:
    def __init__(self, entities: Set[Entity], game_map: GameMap, player: MovableEntity):
        self.entities = entities
        self.game_map = game_map
        self.player = player

    def handle_action(self, action) -> None:
        if action is not None:
            print(f"Performing {action}")
            action.perform(self, self.player)

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char)
        console.print(self.player.x, self.player.y, self.player.char)
        context.present(console)

        console.clear()