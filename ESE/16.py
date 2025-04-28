#Two-Player Game Using Minimax Algorithm (Computer Loses or Draws)
import math

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    return board[0][0] == board[1][1] == board[2][2] == player or \
           board[0][2] == board[1][1] == board[2][0] == player

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return -1   # Computer loses if it wins
    if is_winner(board, 'X'):
        return 1    # Player wins if they win
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def worst_move(board):
    worst_score = math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, True)
                board[i][j] = ' '
                if score < worst_score:
                    worst_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe (Computer tries to lose)")
    print_board(board)

    while True:
        # Player move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input.")

        print_board(board)

        if is_winner(board, 'X'):
            print("You win!")
            break
        if is_full(board):
            print("Draw!")
            break

        # Computer move
        move = worst_move(board)
        if move:
            board[move[0]][move[1]] = 'O'
            print("Computer played:")
            print_board(board)

            if is_winner(board, 'O'):
                print("Computer wins!")
                break
            if is_full(board):
                print("Draw!")
                break
        else:
            print("Draw!")
            break

play_game()
