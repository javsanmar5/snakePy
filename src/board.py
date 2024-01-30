import random

class Board():

    EMPTY_TILE = "⬜"
    FILLED_TILE = "⬛"
    APPLE_TILE = "🟥"

    def __init__(self):
        self.size = [[Board.EMPTY_TILE for _ in range(10)] for _ in range(10)]
        self.apple_position= (random.randint(0,9),random.randint(0,9))


    def render_move(self, snake_positions):        
        self.size = [[Board.EMPTY_TILE for _ in range(10)] for _ in range(10)] 
        self.size[self.apple_position[0]][self.apple_position[1]]=Board.APPLE_TILE 
        self.handle_eat(snake_positions)
        for i in snake_positions:
            if i[0] < 10 and i[1] < 10:
                self.size[i[0]][i[1]] = Board.FILLED_TILE


    def handle_eat(self, snake_positions):
        if self.apple_position == snake_positions[-1]:
            snake_positions.append(self.apple_position)
            self.create_apple()

    def create_apple(self):
        self.apple_position = (random.randint(0,9),random.randint(0,9))


    def __str__(self):
        string = ""
        for i in self.size:
            for j in i:
                string += j
            string += "\n"
        return string

