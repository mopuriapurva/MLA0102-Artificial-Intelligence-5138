import copy

# ----------------------------
# Board Representation
# ----------------------------

EMPTY = '.'
PLAYER = 'p'
AI = 'a'

def initialize_board():
    board = [[EMPTY for _ in range(8)] for _ in range(8)]
    # Place player pieces
    for row in range(3):
        for col in range(8):
            if (row + col) % 2 == 1:
                board[row][col] = AI
    # Place AI pieces
    for row in range(5,8):
        for col in range(8):
            if (row + col) % 2 == 1:
                board[row][col] = PLAYER
    return board

def print_board(board):
    print("  " + " ".join(map(str, range(8))))
    for i, row in enumerate(board):
        print(i, " ".join(row))
    print()

# ----------------------------
# Legal Moves
# ----------------------------

def get_moves(board, piece):
    moves = []
    directions = [(-1, -1), (-1, 1)] if piece == PLAYER else [(1, -1), (1, 1)]
    for r in range(8):
        for c in range(8):
            if board[r][c] == piece:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 8 and 0 <= nc < 8 and board[nr][nc] == EMPTY:
                        moves.append(((r,c), (nr,nc)))
                    # Capture
                    nr2, nc2 = r + 2*dr, c + 2*dc
                    if 0 <= nr2 < 8 and 0 <= nc2 < 8 and board[nr][nc] not in [piece, EMPTY] and board[nr2][nc2] == EMPTY:
                        moves.append(((r,c), (nr2,nc2)))
    return moves

# ----------------------------
# Minimax + Alpha-Beta
# ----------------------------

def evaluate(board):
    p_count = sum(row.count(PLAYER) for row in board)
    a_count = sum(row.count(AI) for row in board)
    return a_count - p_count

def minimax(board, depth, maximizingPlayer, alpha, beta):
    if depth == 0:
        return evaluate(board), None

    piece = AI if maximizingPlayer else PLAYER
    moves = get_moves(board, piece)
    if not moves:
        return evaluate(board), None

    best_move = None
    if maximizingPlayer:
        max_eval = float('-inf')
        for move in moves:
            new_board = copy.deepcopy(board)
            make_move(new_board, move)
            eval, _ = minimax(new_board, depth-1, False, alpha, beta)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in moves:
            new_board = copy.deepcopy(board)
            make_move(new_board, move)
            eval, _ = minimax(new_board, depth-1, True, alpha, beta)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def make_move(board, move):
    (r1, c1), (r2, c2) = move
    piece = board[r1][c1]
    board[r1][c1] = EMPTY
    board[r2][c2] = piece
    # Remove captured piece
    if abs(r2 - r1) == 2:
        board[(r1+r2)//2][(c1+c2)//2] = EMPTY

# ----------------------------
# Game Loop
# ----------------------------

def game_loop():
    board = initialize_board()
    print_board(board)
    turn = PLAYER  # Player starts

    while True:
        moves = get_moves(board, turn)
        if not moves:
            winner = AI if turn == PLAYER else PLAYER
            print(f"Game Over! Winner is {winner.upper()}")
            break

        if turn == PLAYER:
            # Human move
            print("Your turn (PLAYER).")
            print("Available moves:")
            for i, move in enumerate(moves):
                print(f"{i}: {move}")
            idx = int(input("Choose move index: "))
            make_move(board, moves[idx])
        else:
            # AI move
            print("AI is thinking...")
            _, move = minimax(board, depth=4, maximizingPlayer=True, alpha=float('-inf'), beta=float('inf'))
            print(f"AI chooses move: {move}")
            make_move(board, move)

        print_board(board)
        turn = AI if turn == PLAYER else PLAYER

# ----------------------------
# Run the Game
# ----------------------------

if __name__ == "__main__":
    game_loop()
