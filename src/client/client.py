import socket
import pickle
import tcod
from InputHandler import InputHandler


class Client:
    def __init__(self, server=None, port=None):
        self.SERVER = server or "127.0.0.1"
        self.PORT = port or 5050
        self.FORMAT = 'utf-8'
        self.HEADER = 64
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.SERVER, self.PORT))

    def send(self, msg):
        message = pickle.dumps(msg)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)

    def receive(self):
        msg_length = self.client.recv(self.HEADER).decode(self.FORMAT)
        msg_length = int(msg_length)
        data_binary = self.client.recv(msg_length)
        data = pickle.loads(data_binary)
        return data

    def click_handler(self, event):
        if event.event_type == "down":
            self.send(event.name)

    def start(self):
        engine = self.receive()
        with tcod.context.new_terminal(
                70, 70
        ) as context:
            input_handler = InputHandler()
            root_console = tcod.Console(engine.game_map.width, engine.game_map.height, order="F")
            while True:
                print(engine.player.x)
                engine.render(console=root_console, context=context)
                for event in tcod.event.wait():
                    action = input_handler.dispatch(event)
                    if action is not None:
                        print(action)
                        self.send(action)
                        engine = self.receive()


if __name__ == "__main__":
    client = Client()
    client.start()
