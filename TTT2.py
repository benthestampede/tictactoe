# this is my tic tac toe game

# tic tac toe board generation
def generate_board(number, count):
    list = []
    for x in range(number):
        list.append(count)
        if count != "_":
            count += 1
    return list


# variables
board_size = 9
board_numbers = generate_board(board_size, 1)
board = []
move_list = []


# primary functions
def intro():
    print("Welcome to Ben's Tic Tac Toe Dungeon. Choose wisely...")
    board = generate_board(board_size, "_")
    return board


def print_board(board):
    print()
    print(board[:3])
    print(board[3:6])
    print(board[6:9])
    print()


def defeat(board):
    def defeat_text():
        print("You have been pulverized. Sad!")
        print()
        choice = input("Press 1 to play again. Press 2 to exit.")
        print()
        if choice == "1":
            new_board = intro()
            print_board(new_board)
            move_list = []
            guess(board_numbers, new_board, move_list)
        elif choice == "2":
            quit()
        else:
            print("Invalid entry.")

    if board[0] == "O" and board[1] == "O" and board[2] == "O":
        defeat_text()
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        defeat_text()
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        defeat_text()
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        defeat_text()
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        defeat_text()
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        defeat_text()


def victory(board):
    def victory_text():
        print("Congratulations, you are a tic tac toe megabrain!")
        print()
        choice = input("Press 1 to play again. Press 2 to exit.")
        print()
        if choice == "1":
            new_board = intro()
            print_board(new_board)
            move_list = []
            guess(board_numbers, new_board, move_list)
        elif choice == "2":
            quit()
        else:
            print("Invalid entry.")

    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        victory_text()
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        victory_text()
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        victory_text()
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        victory_text()
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        victory_text()
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        victory_text()


def tie(board):
    def tie_text():
        print("'Twas a tie, my good man.")
        print()
        choice = input("Press 1 to play again. Press 2 to exit.")
        print()
        if choice == "1":
            new_board = intro()
            print_board(new_board)
            move_list = []
            guess(board_numbers, new_board, move_list)
        elif choice == "2":
            quit()
        else:
            print("Invalid entry.")

    if "_" not in board:
        tie_text()


def opponent(board, move_list):
    move = 0
    move_prio = [6, 8, 7, 0, 1, 2, 3, 5, 4]  # it loops through them backwards
    for m in move_prio:
        if m not in move_list and board[m] == "_":
            move = m
    move_list.append(move)
    #print(move_list)
    board[move] = "O"
    return board, move_list


def guess(x, y, move_list):
    current_guess = int(input("Please choose a square to place an X."))
    if current_guess in x and y[current_guess - 1] == "_":
        if y[current_guess - 1] != "X":
            y[current_guess - 1] = "X"
        opponent(y, move_list)  # this works as it is referencing the global variable, wasn't assigned in the function
        print_board(y)
        victory(y)
        defeat(y)
        tie(y)
        guess(x, y, move_list)
    else:
        print()
        print("Invalid entry.")
        print()
        guess(x, y, move_list)


# call the game functions
board = intro()
print_board(board)
guess(board_numbers, board, move_list)
