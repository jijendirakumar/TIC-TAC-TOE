import math

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        return "Tie"
    return None

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == "X":
        return -1
    if winner == "O":
        return 1
    if winner == "Tie":
        return 0
    
    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe! You are X, AI is O.")
    print_board(board)
    
    while True:
        try:
            row, col = map(int, input("Enter row and column (0-2): ").split())
            if board[row][col] != " ":
                print("Invalid move, try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers between 0 and 2.")
            continue
        
        board[row][col] = "X"
        print_board(board)
        if check_winner(board):
            break
        
        print("AI's turn...")
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        print_board(board)
        if check_winner(board):
            break
    
    result = check_winner(board)
    if result == "X":
        print("You win!")
    elif result == "O":
        print("AI wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
