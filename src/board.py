class Board():

    EMPTY_TILE = "⬜"
    FILLED_TILE = "⬛"
    APPLE_TILE = "🟥"

    def __init__(self):
        self.size = [[Board.EMPTY_TILE for _ in range(10)] for _ in range(10)]

    def __str__(self):
        string = ""
        for i in self.size:
            for j in i:
                string += j
            string += "\n"
        return string

