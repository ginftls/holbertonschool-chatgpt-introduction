#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.total_cells = width * height
        self.total_non_mine_cells = self.total_cells - mines
        self.revealed_count = 0

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if self.revealed[y][x]:
            return True

        if (y * self.width + x) in self.mines:
            return False

        self.revealed[y][x] = True
        self.revealed_count += 1

        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal(nx, ny)
        return True

    def play(self):
        while True:
            self.print_board()  # Print the board initially
             if self.revealed_count == self.total_non_mine_cells:
                self.print_board(reveal=True)
                print("Congratulations! You have won the game!")
                break

            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                # Check if the coordinates are within the valid range
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Invalid coordinates. Please enter values within the range.")
                    input("Press Enter to re-enter the coordinates...")  # Wait for user to press Enter
                    continue  # Prompt for new coordinates without clearing the screen
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                input("Press Enter to re-enter the coordinates...")  # Wait for user to press Enter
                continue  # Prompt for new coordinates without clearing the screen
            # Clear the screen only after valid input
            clear_screen()

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
