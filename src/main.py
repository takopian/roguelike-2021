#!/usr/bin/env python3

import tcod

from src.client.commands import Move
from src.client.entity import Player
from src.client.input_handler import EventHandler


def main():
    screen_width = 80
    screen_height = 50

    player = Player(int(screen_width / 2), int(screen_height / 2))
    event_handler = EventHandler()

    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            title="roguelike",
            vsync=True,
    ) as context:
        console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            console.print(x=player.x, y=player.y, string=str(player))

            context.present(console)
            console.clear()

            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()

                action = event_handler.dispatch(event)
                if action is None:
                    continue

                if isinstance(action, Move):
                    player.move(action.dx, action.dy)


if __name__ == "__main__":
    main()
