import sqlite3
from datetime import datetime

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


def update_player_info():
    with conn:
        if check_win(1):
            cur.execute("UPDATE player_info SET wins = wins + 1 WHERE player_id='1'")
        elif check_win(2):
            cur.execute("UPDATE player_info SET wins = wins + 1 WHERE player_id='2'")
        cur.execute("UPDATE player_info SET games_played = games_played + 1 WHERE player_id='1'")
        cur.execute("UPDATE player_info SET games_played = games_played + 1 WHERE player_id='2'")
        conn.commit()


def update_board():
    with conn:
        new_board_id = 0
        cur.execute("SELECT board_id FROM game_data DESC")
        for r in cur.fetchall():
            new_board_id = r[0] + 1
        curr_date = datetime.now()
        winner = "Draw"
        if check_win(1):
            winner = "Player 1"
        elif check_win(2):
            winner = "Player 2"
        cur.execute('INSERT INTO game_data (board_id,date,winner,board) VALUES (?,?,?,?)', (new_board_id, curr_date, str(winner), str(board)))
        conn.commit()


def print_player_results():
    with conn:
        print('Results for player_info: ')
        cur.execute("SELECT wins FROM player_info WHERE player_id='1'")
        for r in cur.fetchall():
            player1_wins = r[0]
        cur.execute("SELECT games_played FROM player_info WHERE player_id='1'")
        for r in cur.fetchall():
            games = r[0]
        ratio1 = player1_wins/games * 100
        print("Player 1 - wins: ", player1_wins, ", Games played: ", games, ", Win Ratio: ", ratio1, "%")
        cur.execute("SELECT wins FROM player_info WHERE player_id='2'")
        for r in cur.fetchall():
            player2_wins = r[0]
        cur.execute("SELECT games_played FROM player_info WHERE player_id='2'")
        for r in cur.fetchall():
            games = r[0]
        ratio2 = player2_wins/games * 100
        print("Player 2 - wins: ", player2_wins, ", Games played: ", games, ", Win Ratio: ", ratio2, "%")


def print_game_results():
    with conn:
        print('Results for game_data')
        cur.execute("SELECT * FROM game_data ORDER BY board_id DESC LIMIT 10")
        for r in cur.fetchall():
            print(r)


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
                        update_player_info()
                        update_board()
                elif player == 2:
                    if check_mark(row, col):
                        turn += 1
                    place_mark(row, col, 2)
                    if check_win(2):
                        print_board()
                        print('Player 2 wins!')
                        update_player_info()
                        update_board()
                if turn == 10:
                    if not check_win(1) and not check_win(2):
                        print_board()
                        print('The game is a Draw!')
                        update_player_info()
                        update_board()
            else:
                print('Invalid row or column entered')
        except Exception as err:
            print("Error: ", err)
            pass


try:
    conn = sqlite3.connect('Tic_Tac_Toe.db')
    cur = conn.cursor()
except Exception as e:
    print("Error during connection: ", str(e))
else:
    try:
        cur.execute(""" CREATE TABLE player_info(
                        player_id int(11) primary key,
                        wins int(11),
                        games_played int(11)) """)
        cur.execute(""" CREATE TABLE game_data(
                        board_id int(11) primary key,
                        date datetime,
                        winner TEXT,
                        board TEXT) """)
        cur.execute("INSERT INTO player_info(player_id,wins,games_played) VALUES (1,0,0)")
        cur.execute("INSERT INTO player_info(player_id,wins,games_played) VALUES (2,0,0)")
    except Exception:
        pass
finally:
    try:
        main()
        player_results = input("Do you wish to view the player info? (Y or N)")
        if player_results.lower() == "y":
            print_player_results()
        game_results = input("Do you wish to view the previous 10 games? (Y or N)")
        if game_results.lower() == "y":
            print_game_results()
        print("Thanks for playing! - by Walker")
    except Exception as e:
        print("Error occurred: ", str(e))
    conn.close()
