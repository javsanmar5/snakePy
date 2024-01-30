import random

class Snake():

    def __init__(self):
        initial_position = (random.randint(0,9), random.randint(0,9))
        self.positions = [initial_position]
        self.alive = True

    def render_move(self, kb_input):
        match kb_input:
            case "a":
                new_pos = (self.positions[-1][0], self.positions[-1][1] -1)
                self.handle_game_over2(new_pos)
                self.positions.append(new_pos)
                del self.positions[0]
            case "s":
                new_pos = (self.positions[-1][0]+1, self.positions[-1][1])
                self.handle_game_over2(new_pos)
                self.positions.append(new_pos)
                del self.positions[0]
            case "d":
                new_pos = (self.positions[-1][0], self.positions[-1][1] +1)
                self.handle_game_over2(new_pos)
                self.positions.append(new_pos)
                del self.positions[0]
            case "w":
                new_pos = (self.positions[-1][0]-1, self.positions[-1][1] )
                self.handle_game_over2(new_pos)
                self.positions.append(new_pos)
                del self.positions[0]
            case _:
                print("Something went wrong")

        self.handle_game_over()

    def handle_game_over(self):
        if self.positions[-1][0] < 0 or self.positions[-1][1] < 0 or self.positions[-1][0] >= 10 or self.positions[-1][1] >= 10:
            self.alive = False 

    def handle_game_over2(self, new_pos):
        if new_pos in self.positions:
            self.alive = False
