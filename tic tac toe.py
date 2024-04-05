# Tic-Tac-Toe

# Create the game board
board = [' ' for _ in range(9)]

# Function to display the game board
def display_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check if any player has won
def check_winner():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True
    return False

# Function to play the game
def play_game():
    player = 'X'
    while True:
        display_board()
        position = int(input("Enter a position (1-9): ")) - 1
        if board[position] == ' ':
            board[position] = player
            if check_winner():
                display_board()
                print("Player", player, "wins!")
                break
            elif ' ' not in board:
                display_board()
                print("It's a tie!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

# Start the game
play_game()
