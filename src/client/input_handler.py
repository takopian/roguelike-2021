from typing import Optional

import tcod.event

from src.client.commands import Command, Move


class EventHandler(tcod.event.EventDispatch[Command]):
    def ev_keydown(self, event: tcod.event.KeyDown):
        action: Optional[Command] = None

        key = event.sym

        if key == tcod.event.K_UP:
            action = Move(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = Move(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = Move(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = Move(dx=1, dy=0)

        return action
