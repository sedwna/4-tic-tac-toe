# 4-tic-tak-toe
from termcolor import colored

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


def start():
    print_board()
    turn = 1
    while turn != 10:
        if turn % 2 != 0:
            while True:
                move_p = int(input("turn player pls choose your move(1-9) ---> "))
                if move_p not in range(1, 10):
                    continue
                if board[move_p - 1] == move_p:
                    board[move_p - 1] = "X"
                    break
            print_board()
        if check_board("X"):
            print("Player WIN")
            exit()

        if turn % 2 == 0:
            while True:
                move_c = int(input("turn Computer pls choose your move(1-9) ---> "))
                if move_c not in range(1, 10):
                    continue
                if board[move_c - 1] == move_c:
                    board[move_c - 1] = "O"
                    break
            print_board()
        if check_board("O"):
            print("Computer WIN")
            exit()

        turn += 1


def menu():
    x = input("choose what do you want? : 1.start \n--->")
    if x == '1' or x == 'start':
        print("Player : X \nComputer : O")
        start()


menu()
