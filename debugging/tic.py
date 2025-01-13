#!/usr/bin/python3

def print_board(board):
    """Print the game board with proper formatting."""
    print("\nCurrent Board:")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # Don't print line after last row
            print("---------")

def check_winner(board):
    """Check if there is a winner or a tie."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True, row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True, board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True, board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True, board[0][2]

    # Check for tie
    if all(cell != " " for row in board for cell in row):
        return True, "Tie"

    return False, None

def is_valid_move(board, row, col):
    """Check if the move is valid."""
    if not (0 <= row <= 2 and 0 <= col <= 2):
        return False
    return board[row][col] == " "

def get_move(player):
    """Get and validate player move."""
    while True:
        try:
            print(f"\nPlayer {player}'s turn")
            row = int(input(f"Enter row (0-2): "))
            col = int(input(f"Enter column (0-2): "))
            return row, col
        except ValueError:
            print("Please enter valid numbers!")

def tic_tac_toe():
    """Main game function."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    print("Welcome to Tic-tac-toe!")
    print("Players take turns entering row and column numbers (0-2)")
    while True:
        print_board(board)
        # Get player move
        row, col = get_move(player)
        # Validate move
        if not is_valid_move(board, row, col):
            print("Invalid move! Cell is either taken or out of bounds.")
            continue
        # Make move
        board[row][col] = player
        # Check for winner or tie
        game_over, winner = check_winner(board)
        if game_over:
            print_board(board)
            if winner == "Tie":
                print("Game Over - It's a tie!")
            else:
                print(f"Game Over - Player {winner} wins!")
            break
        # Switch players
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    try:
        tic_tac_toe()
    except KeyboardInterrupt:
        print("\nGame terminated by user. Goodbye!")
    except EOFError:
        print("\nGame terminated. Goodbye!")
