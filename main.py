def greet():
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  Крестики-нолики  ")
    print("  Формат ввода : x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def show():
    field = [[""] * 3 for i in range(3) ]
    print(f"  0 1 2")
    print(f"0 {field[0][0]} {field[0][1]} {field[0][2]}")
    print(f"1 {field[1][0]} {field[1][1]} {field[1][2]}")
    print(f"2 {field[2][0]} {field[2][1]} {field[2][2]}")
show()

def ask():
    while True:
        x, y = map(int, input("  Ваш ход: ").split())

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                return x, y
            else:
                print(" Поле занято")
        else:
            print(" Числа вне диапозона игры")
ask()