row0 = ['-', '-', '-']
row1 = ['-', '-', '-']
row2 = ['-', '-', '-']
board = [row0, row1, row2]


def print_board():
    print("Printing board...")
    print("[", board[0][0], "] [", board[0][1], "] [", board[0][2], "]")
    print("[", board[1][0], "] [", board[1][1], "] [", board[1][2], "]")
    print("[", board[2][0], "] [", board[2][1], "] [", board[2][2], "]")


def check_mark(row, col):
    if board[row][col] == '-':
        return True
    else:
        return False


def place_mark(row, col, player):
    if check_mark(row, col):
        if player == 1:
            board[row][col] = 'X'
        elif player == 2:
            board[row][col] = 'O'
    elif not check_mark(row, col):
        print('Position already taken')


def check_win():
    # Check rows
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2] == 'X':
            print("Player 1 has won!")
        elif board[row][0] == board[row][1] == board[row][2] == 'O':
            print("Player 2 has won!")
    # Check Columns
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] == 'X':
            print("Player 1 has won!")
        elif board[0][col] == board[1][col] == board[2][col] == 'O':
            print("Player 2 has won!")
    # Check Diagonal 1
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        print("Player 1 has won!")
    elif board[0][0] == board[1][1] == board[2][2] == 'O':
        print("Player 2 has won!")
    # Check Diagonal 2
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        print("Player 1 has won!")
    elif board[0][2] == board[1][1] == board[2][0] == 'O':
        print("Player 2 has won!")


def main():
    print('Testing print_board')
    print_board()
    print('Before place_mark, check_mark for 1, 1 is ', check_mark(1, 1))
    place_mark(1, 1, 1)
    print('After place_mark, check_mark for 1, 1 is ', check_mark(1, 1))
    place_mark(0, 2, 2)
    print_board()
    place_mark(0, 0, 1)
    place_mark(2, 2, 2)
    place_mark(1, 0, 1)
    place_mark(1, 2, 2)
    print('Testing Winner')
    print_board()
    check_win()


main()
