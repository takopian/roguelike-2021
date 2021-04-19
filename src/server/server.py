import socket
import pickle
from src.server.game.map.DungeonGenerator import generate_dungeon
from src.server.game.Engine import Engine
from src.server.game.Character import Character


class Server:
    def __init__(self, host=None, port=None):
        self.HOST = host or '127.0.0.1'
        self.PORT = port or 5050
        self.FORMAT = 'utf-8'
        self.HEADER = 64
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.HOST, self.PORT))

    def send(self, conn, msg):
        message = pickle.dumps(msg)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        conn.send(send_length)
        conn.send(message)

    def receive(self, conn):
        msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
        msg_length = int(msg_length)
        data_binary = conn.recv(msg_length)
        data = pickle.loads(data_binary)
        return data

    def start(self):
        print(f"Server started on port: {self.PORT}")
        with self.socket as s:
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                player = Character(35, 35, "@")
                npc = Character(25, 15, "@")
                map = generate_dungeon(20, 15, 20, 70, 70, player)
                game = Engine({npc}, map, player)
                self.send(conn, game)
                while True:
                    action = self.receive(conn)
                    print(f"Got action {action}")
                    game.handle_action(action)
                    self.send(conn, game)
                    # msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
                    # msg_length = int(msg_length)
                    # data = conn.recv(msg_length).decode(self.FORMAT)
                    # print(data)
                    # if not data:
                    #     break
                    # conn.send(f"Got Message {data}".encode(self.FORMAT))


if __name__ == "__main__":
    server = Server()
    server.start()
