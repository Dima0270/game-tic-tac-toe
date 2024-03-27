board = ([" ", '1', '2', '3'],
         ['1', "-", "-", "-"],
         ['2', "-", "-", "-"],
         ['3', "-", "-", "-"],
         )
for i in board:
    print(*i)


def X_():
    x_x = int(input("Выберите номер строчки в которую хотели бы поставить крестик: "))
    while x_x not in [1, 2, 3]:
        x_x = int(input("Данного номера строчки не существует. Попробуйте снова: "))
    x_y = int(input("Выберите номер столбца в который хотели бы поставить крестик: "))
    while x_y not in [1, 2, 3]:
        x_y = int(input("Данного номера столбца не существует. Попробуйте снова: "))
    if board[x_x][x_y] == "-":
        board[x_x][x_y] = "X"
        for i in board:
            print(*i)
    elif board[x_x][x_y] == "X":
        print("На этом месте уже есть крестик")
        X_()
    else:
        print("На этом месте уже есть нолик")
        X_()


def O_():
    o_x = int(input("Выберите номер строчки в которую хотели бы поставить нолик: "))
    while o_x not in [1, 2, 3]:
        o_x = int(input("Данного номера строчки не существует. Попробуйте снова: "))
    o_y = int(input("Выберите номер столбца в который хотели бы поставить нолик: "))
    while o_y not in [1, 2, 3]:
        o_y = int(input("Данного номера столбца не существует. Попробуйте снова: "))
    if board[o_x][o_y] == "-":
        board[o_x][o_y] = "O"
        for i in board:
            print(*i)
    elif board[o_x][o_y] == "O":
        print("На этом месте уже есть нолик")

    else:
        print("На этом месте уже есть крестик")
        O_()


end = 0
while end <= 9:
    X_()
    if (board[1][1] == "X") and (board[1][2] == "X") and (board[1][3] == "X"):
        print("Крестики выиграли")
        break
    elif (board[2][1] == "X") and (board[2][2] == "X") and (board[2][3] == "X"):
        print("Крестики выиграли")
        break
    elif (board[3][1] == "X") and (board[3][2] == "X") and (board[3][3] == "X"):
        print("Крестики выиграли")
        break
    elif (board[1][1] == "X") and (board[2][1] == "X") and (board[3][1] == "X"):
        print("Крестики выиграли")
        break
    elif (board[1][2] == "X") and (board[2][2] == "X") and (board[3][2] == "X"):
        print("Крестики выиграли")
        break
    elif (board[1][3] == "X") and (board[2][3] == "X") and (board[3][3] == "X"):
        print("Крестики выиграли")
        break
    elif (board[1][1] == "X") and (board[2][2] == "X") and (board[3][3] == "X"):
        print("Крестики выиграли")
        break
    elif (board[1][3] == "X") and (board[2][2] == "X") and (board[3][1] == "X"):
        print("Крестики выиграли")
        break
    end += 1
    if end == 9:
        print("Ничья")
        break
    O_()
    if (board[1][1] == "O") and (board[1][2] == "O") and (board[1][3] == "O"):
        print("Нолики выиграли")
        break
    elif (board[2][1] == "O") and (board[2][2] == "O") and (board[2][3] == "O"):
        print("Нолики выиграли")
        break
    elif (board[3][1] == "O") and (board[3][2] == "O") and (board[3][3] == "O"):
        print("Нолики выиграли")
        break
    elif (board[1][1] == "O") and (board[2][1] == "O") and (board[3][1] == "O"):
        print("Нолики выиграли")
        break
    elif (board[1][2] == "O") and (board[2][2] == "O") and (board[3][2] == "O"):
        print("Нолики выиграли")
        break
    elif (board[1][3] == "O") and (board[2][3] == "O") and (board[3][3] == "O"):
        print("Нолики выиграли")
        break
    elif (board[1][1] == "O") and (board[2][2] == "O") and (board[3][3] == "O"):
        print("Нолики выиграли")
        break
    elif (board[1][3] == "O") and (board[2][2] == "O") and (board[3][1] == "O"):
        print("Нолики выиграли")
        break
    end += 1

else:
    print("Ничья")
