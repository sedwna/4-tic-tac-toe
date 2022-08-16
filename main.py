# 4-tic-tak-toe
from termcolor import colored
from time import sleep

board = list(range(1, 10))


def check_board(plyr):
    winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
               (0, 3, 6), (1, 4, 7), (2, 5, 8),
               (0, 4, 8), (2, 4, 6))

    for tup in winners:
        win = True
        for j in tup:
            if board[j] != plyr:
                win = False
                break
        if win:
            break
    return win


def plyer_move(num, shape):
    while True:
        move_p = int(input(f"turn player({num}) pls choose your move(1-9) ---> "))
        if move_p not in range(1, 10):
            continue
        if board[move_p - 1] == move_p:
            board[move_p - 1] = shape
            break
    print_board()
    if check_board(shape):
        print(f"Player({num}) WIN")
        exit()


def computer_move():
    moves = ((0, 2, 6, 8), (4,), (1, 3, 5, 7))

    # ایا کامپیوتر میتواند برنده شود؟
    for i in range(0, 9):
        if board[i] == i + 1:
            board[i] = "O"
            if check_board("O"):
                print_board()
                print("Computer WIN")
                exit()
            else:
                board[i] = i + 1
            # جلوگیری از برنده شدن کاربر درصورت عدم وجود حالت پیروزی برای کامپیوتر
    h = 0
    for k in range(0, 9):
        if board[k] == k + 1:
            board[k] = "X"
            if check_board("X"):
                board[k] = "O"
                h = 1
                break
            else:
                board[k] = k + 1

    if h == 0:
        ch = 0
        for tup in moves:
            for i in tup:
                if board[i] == i + 1:
                    board[i] = 'O'
                    ch = 1
                    break
            if ch == 1:
                break

    print_board()


def print_board():
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = "\n\n"
        if i == 'X':
            print(colored(f"[{i}]", "red"), end=end)
        elif i == 'O':
            print(colored(f"[{i}]", "blue"), end=end)
        else:
            print(f"[{i}]", end=end)
        j += 1


def start_AI():
    print_board()
    turn = 1
    while turn != 10:
        if turn % 2 != 0:
            plyer_move(1, 'X')
        if turn % 2 == 0:
            print("turn Computer pls wait... ")
            sleep(2)
            computer_move()
        turn += 1
    else:
        print('Equal.')


def start_duel():
    print_board()
    turn = 1
    while turn != 10:
        if turn % 2 != 0:
            plyer_move(1, 'X')

        if turn % 2 == 0:
            plyer_move(2, 'O')

        turn += 1
    else:
        print('Equal.')

def menu():
    x = input("choose what do you want? : 1.start_duel  2.start_AI \n--->")
    if x == '1' or x == 'start_duel':
        print("Player : X \nComputer : O")
        start_duel()
    elif x == '2' or x == 'start_AI':
        start_AI()


menu()
