import math
EMPTY = 0
PLAYER_X = 1
PLAYER_O = -1
def print_board(board):
    for row in board:
        print(" | ".join(map(lambda x: "X" if x == PLAYER_X else ("O" if x == PLAYER_O else " "), row)))
        print("-" * 5)
def game_over(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    if all(board[i][j] != EMPTY for i in range(3) for j in range(3)):
        return 0
    return None
def evaluate(board):
    winner = game_over(board)
    if winner == PLAYER_X:
        return 1
    elif winner == PLAYER_O:
        return -1
    else:
        return 0
def minimax(board, depth, maximizing_player):
    if game_over(board) is not None or depth == 0:
        return evaluate(board)
    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth - 1, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth - 1, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval
def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                eval = minimax(board, 5, False)
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move
def play_game():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    current_player = PLAYER_X
    while game_over(board) is None:
        print_board(board)
        if current_player == PLAYER_X:
            row, col = find_best_move(board)
            print("AI's turn (X):")
        else:
            while True:
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter column (0-2): "))
                    if board[row][col] == EMPTY:
                        break
                    else:
                        print("That spot is already taken!")
                except ValueError:
                    print("Invalid input! Please enter a number.")
        board[row][col] = current_player
        current_player = -current_player
    print_board(board)
    winner = game_over(board)
    if winner == 0:
        print("It's a tie!")
    elif winner == PLAYER_X:
        print("AI wins!")
    else:
        print("You win!")
play_game()
