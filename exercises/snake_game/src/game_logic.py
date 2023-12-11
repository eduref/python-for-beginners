import tkinter as tk
import random

class SnakeGame:
    def __init__(self):
        # Initialize game variables
        self.snake_position = [[100, 100]]
        self.snake_food = [200, 200]
        self.snake_speed = 100
        self.snake_direction = None
        self.window_size = "600x400"
        self.game_over = False

        # Create the window
        self.window = tk.Tk()
        self.window.title("Snake Game")

        # Create a canvas for drawing
        self.canvas = tk.Canvas(self.window, bg="white", height=400, width=600)
        self.canvas.pack()

        # Set up key bindings
        self.setup_bindings()

    def setup_bindings(self):
        self.window.bind("<Left>", lambda event: self.change_direction('Left'))
        self.window.bind("<Right>", lambda event: self.change_direction('Right'))
        self.window.bind("<Up>", lambda event: self.change_direction('Up'))
        self.window.bind("<Down>", lambda event: self.change_direction('Down'))
        self.window.focus_set()

    




    def start_game(self):
        self.game_loop()
        self.window.mainloop()