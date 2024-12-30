class GameBoard:
    def __init__(self):
        self.tiles = []
        self.oceans = 0
        self.temperature = -30
        self.oxygen = 0

    def add_tile(self, tile):
        self.tiles.append(tile)

    def update_oceans(self, amount):
        self.oceans += amount

    def update_temperature(self, amount):
        self.temperature += amount

    def update_oxygen(self, amount):
        self.oxygen += amount

    def get_board_state(self):
        return {
            "tiles": self.tiles,
            "oceans": self.oceans,
            "temperature": self.temperature,
            "oxygen": self.oxygen
        }
