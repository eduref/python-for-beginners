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

    def draw_snake(self):
         for segment in self.snake_position:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0]+20, segment[1]+20, fill="green")

    def draw_food(self):
        self.canvas.create_oval(self.snake_food[0], self.snake_food[1], self.snake_food[0]+20, self.snake_food[1]+20, fill="red")
    
    def game_loop(self):
        if not self.game_over:
            self.game_over = not self.move_snake()

        if not self.game_over:
            self.canvas.delete("all")  # Clear canvas
            self.draw_snake()
            self.draw_food()
            self.window.after(self.snake_speed, self.game_loop)  # Schedule next update
        else:
            print("Game Over")

    # Write your code after this line



    # Solution to excercise "Snake"
    def move_snake(self):
        global snake_food  # Declare snake_food as global at the beginning

        if snake_direction is None:
            return True  # Skip moving the snake if no direction is set

        # Calculate new head position
        head_x, head_y = self.snake_position[0]
        if snake_direction == 'Left':
            head_x -= 20
        elif snake_direction == 'Right':
            head_x += 20
        elif snake_direction == 'Up':
            head_y -= 20
        elif snake_direction == 'Down':
            head_y += 20

        new_head = [head_x, head_y]

        # Check for game over conditions
        if new_head in self.snake_position or head_x < 0 or head_x >= 600 or head_y < 0 or head_y >= 400:
            return False  # Game over

        # Move snake
        self.snake_position.insert(0, new_head)

        # Check for food collision
        if new_head == snake_food:
            snake_food = [random.randint(0, 29)*20, random.randint(0, 19)*20]  # New food position
        else:
            self.snake_position.pop()  # Remove tail segment

        return True  # Continue game

    def change_direction(self, new_direction):
        global snake_direction
        if snake_direction is None or new_direction in ['Left', 'Right', 'Up', 'Down']:
            snake_direction = new_direction

    def start_game(self):
        self.game_loop()
        self.window.mainloop()