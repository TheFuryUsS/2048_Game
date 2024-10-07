# Basic Tic-Tac-Toe game in the console

# Create an empty 3x3 board
board = [[" " for _ in range(3)] for _ in range(3)]

# Function to print the board
def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check for a winner
def check_winner(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to check for a tie
def check_tie():
    for row in board:
        if " " in row:
            return False
    return True

# Main function to play the game
def play():
    current_player = "X"
    while True:
        print_board()
        print(f"Player {current_player}'s turn")

        # Ask the player to choose a row and column
        try:
            row = int(input("Choose a row (0, 1, 2): "))
            col = int(input("Choose a column (0, 1, 2): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check if the position is valid
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move, try again.")
            continue

        # Place the player's symbol on the board
        board[row][col] = current_player

        # Check if the player has won
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if check_tie():
            print_board()
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Game
if __name__ == "__main__":
    play()