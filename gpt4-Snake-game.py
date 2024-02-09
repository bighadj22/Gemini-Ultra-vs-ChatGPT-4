import tkinter as tk
from random import randint

class SnakeGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Snake Game')
        self.geometry('600x400')
        self.resizable(False, False)

        self.canvas = tk.Canvas(self, bg='black', width=600, height=400)
        self.canvas.pack()

        self.snake = [(20, 20), (20, 40), (20, 60)]
        self.snake_direction = 'Right'
        self.food = self.create_food()
        self.score = 0

        self.bind_all('<Key>', self.on_key_press)
        self.update_game()

    def create_food(self):
        """Place food at a random position on the canvas."""
        return randint(0, 29) * 20, randint(0, 19) * 20

    def on_key_press(self, event):
        """Change snake direction based on key press."""
        direction = event.keysym
        if direction in ['Left', 'Right', 'Up', 'Down']:
            self.snake_direction = direction

    def move_snake(self):
        """Move the snake based on the current direction."""
        head_x, head_y = self.snake[0]
        if self.snake_direction == 'Left':
            head_x -= 20
        elif self.snake_direction == 'Right':
            head_x += 20
        elif self.snake_direction == 'Up':
            head_y -= 20
        elif self.snake_direction == 'Down':
            head_y += 20
        new_head = (head_x, head_y)

        if new_head in self.snake or not (0 <= head_x < 600 and 0 <= head_y < 400):
            # Game over
            self.game_over()
            return

        if new_head == self.food:
            # Eat food
            self.score += 10
            self.food = self.create_food()
        else:
            # Move snake
            self.snake.pop()

        self.snake.insert(0, new_head)

    def update_game(self):
        """Update game state, redraw canvas, and schedule next update."""
        self.move_snake()
        self.draw()
        self.after(100, self.update_game)

    def draw(self):
        """Draw snake and food on the canvas."""
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill='white', font=('Arial', 14))
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+20, y+20, fill='green')
        fx, fy = self.food
        self.canvas.create_rectangle(fx, fy, fx+20, fy+20, fill='red')

    def game_over(self):
        """Display game over message and stop the game."""
        self.canvas.create_text(300, 200, text="GAME OVER", fill='white', font=('Arial', 30))
        self.after_cancel(self.update_game)

if __name__ == "__main__":
    game = SnakeGame()
    game.mainloop()
