from board import Board
from snake import Snake
import time
import os

def main():
    
    snake = Snake()
    board = Board()
    old_input = "d"

    while snake.alive:
        os.system("clear")

        board.render_move(snake.positions)
        print(board)
        
        kb_input = input()
        if kb_input=="": kb_input = old_input    
        snake.render_move(kb_input)
        
        old_input = kb_input
        
        time.sleep(0.5)
        

    return "You lost." 



if __name__ == "__main__":
    print(main())
