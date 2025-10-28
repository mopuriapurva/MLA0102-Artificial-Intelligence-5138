import random

# Step a) Represent the 3x3 game board
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")
    print("\n")

# Step b) Human move
def human_move(board):
    while True:
        try:
            move = input("Enter your move (row and column: 1 1 for top-left): ").split()
            if len(move) != 2:
                print("Enter two numbers!")
                continue
            row, col = int(move[0])-1, int(move[1])-1
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Cell already taken!")
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers 1-3.")

# Step b) AI move (random choice)
def ai_move(board):
    available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    move = random.choice(available_moves)
    board[move[0]][move[1]] = 'O'

# Check for winner or draw
def check_winner(board):
    # Rows, columns, diagonals
    lines = board + [list(col) for col in zip(*board)] + [[board[i][i] for i in range(3)]] + [[board[i][2-i] for i in range(3)]]
    for line in lines:
        if line == ['X']*3:
            return 'Human'
        elif line == ['O']*3:
            return 'AI'
    # Check draw
    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'
    return None

# Main game loop
def play_game():
    board = create_board()
    print("Tic Tac Toe Game! You are 'X', AI is 'O'.")
    print_board(board)
    
    while True:
        human_move(board)
        print_board(board)
        winner = check_winner(board)
        if winner:
            break
        
        ai_move(board)
        print("AI has moved:")
        print_board(board)
        winner = check_winner(board)
        if winner:
            break
    
    if winner == 'Draw':
        print("It's a draw!")
    else:
        print(f"{winner} wins!")

# Run the game
if __name__ == "__main__":
    play_game()
