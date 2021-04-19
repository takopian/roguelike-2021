class Map:
    def __init__(self):
        self.height = 100
        self.width = 150
        self.map = []

    def generate_map(self):
        for i in range(self.height):
            self.map.append([])
            for j in range(self.width):
                self.map[i].append('.')
        return self.map