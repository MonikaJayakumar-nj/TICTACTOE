# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# -----Global Variables-----

# play_game
# display_board
# handle_turn
# check_game_still_going
# Flip_player

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

winner = None

game_still_goes = True

current_player = "X"


def play_game():

    display_board()

    while game_still_goes:

        handle_turn(current_player)

        check_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("Tie.")


def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


def handle_turn(player):

    print(player + "'s turn.")
    position = input("Enter the position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Input. Enter a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again")

    board[position] = player
    display_board()


def check_game_over():
    check_for_win()
    check_for_tie()


def check_for_win():
    global winner
    # check_row
    row_winner = check_rows()

    # check_columns
    column_winner = check_columns()

    # check_diagonal
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_still_goes
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_still_goes = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None


def check_columns():
    global game_still_goes
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        game_still_goes = False

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    else:
        return None


def check_diagonal():
    global game_still_goes
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    if diagonal1 or diagonal2:
        game_still_goes = False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    else:
        return None


def check_for_tie():
    global game_still_goes
    if "-" not in board:
        game_still_goes = False
        return True
    else:
        return False


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


play_game()
