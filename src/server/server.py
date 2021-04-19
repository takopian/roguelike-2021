import socket
from src.server.game.map.map_generator import Map
from src.server.game.Game import Game


class Server:
    def __init__(self, host=None, port=None):
        self.HOST = host or '127.0.0.1'
        self.PORT = port or 5050
        self.FORMAT = 'utf-8'
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.HOST, self.PORT))

    def start(self):
        print(f"Server started on port: {self.PORT}")
        with self.socket as s:
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                map_generator = Map()
                map = map_generator.generate_map()
                game = Game(map)
                conn.send(str(game).encode(self.FORMAT))
                while True:
                    data = conn.recv(1024).decode(self.FORMAT)
                    print(data)
                    if not data:
                        break
                    conn.send(f"Got Message {data}".encode(self.FORMAT))


if __name__ == "__main__":
    server = Server()
    server.start()
