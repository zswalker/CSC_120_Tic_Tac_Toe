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


def check_win(player):
    # Check rows
    for row in range(0, 3):
        if player == 1:
            if board[row][0] == board[row][1] == board[row][2] == 'X':
                return True
        if player == 2:
            if board[row][0] == board[row][1] == board[row][2] == 'O':
                return True
    # Check Columns
    for col in range(0, 3):
        if player == 1:
            if board[0][col] == board[1][col] == board[2][col] == 'X':
                return True
        if player == 2:
            if board[0][col] == board[1][col] == board[2][col] == 'O':
                return True
    # Check Diagonal 1
    if player == 1:
        if board[0][0] == board[1][1] == board[2][2] == 'X':
            return True
    if player == 2:
        if board[0][0] == board[1][1] == board[2][2] == 'O':
            return True
    # Check Diagonal 2
    if player == 1:
        if board[0][2] == board[1][1] == board[2][0] == 'X':
            return True
    if player == 1:
        if board[0][2] == board[1][1] == board[2][0] == 'O':
            return True


def main():
    turn = 1
    while not check_win(1) and not check_win(2) and turn != 10:
        try:
            player = 1
            if turn % 2 == 0:
                player = 2
            print('Player', player, '\'s turn!')
            print_board()
            row = int(input('Enter row: '))
            col = int(input('Enter col: '))
            if (0 <= row < 3) and (0 <= col < 3):
                if player == 1:
                    if check_mark(row, col):
                        turn += 1
                    place_mark(row, col, 1)
                    if check_win(1):
                        print_board()
                        print('Player 1 wins!')
                elif player == 2:
                    if check_mark(row, col):
                        turn += 1
                    place_mark(row, col, 2)
                    if check_win(2):
                        print_board()
                        print('Player 2 wins!')
                if turn == 10:
                    if not check_win(1) and not check_win(2):
                        print_board()
                        print('The game is a Draw!')
            else:
                print('Invalid row or column entered')
        except Exception as err:
            print("Error: ", err)
            pass


main()
