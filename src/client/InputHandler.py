from typing import Optional

import tcod.event

from src.server.game.Commands import Command, EscapeCommand, MovementCommand


class InputHandler(tcod.event.EventDispatch[Command]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Command]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Command]:
        action: Optional[Command] = None

        key = event.sym

        if key == tcod.event.K_UP:
            action = MovementCommand(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementCommand(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementCommand(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementCommand(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeCommand()

        return action
