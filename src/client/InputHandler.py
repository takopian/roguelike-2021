from typing import Optional

import tcod.event

from src.server.game.Commands import Command, Escape, Movement


class InputHandler(tcod.event.EventDispatch[Command]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Command]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Command]:
        action: Optional[Command] = None

        key = event.sym

        if key == tcod.event.K_UP:
            action = Movement(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = Movement(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = Movement(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = Movement(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = Escape()

        return action
