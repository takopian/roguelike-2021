import socket
import keyboard


class Client:
    def __init__(self, server=None, port=None):
        self.SERVER = server or "127.0.0.1"
        self.PORT = port or 5050
        self.FORMAT = 'utf-8'
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.SERVER, self.PORT))

    def send(self, msg):
        self.client.send(msg.encode(self.FORMAT))
        print(self.client.recv(2048).decode(self.FORMAT))

    def click_handler(self, event):
        if event.event_type == "down":
            self.send(event.name)

    def start(self):
        print(self.client.recv(2048).decode(self.FORMAT))
        while True:
            keyboard_event = keyboard.read_event()
            self.click_handler(keyboard_event)


if __name__ == "__main__":
    client = Client()
    client.start()