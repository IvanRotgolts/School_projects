field=[["*","*","*"],["*","*","*"],["*","*","*"]]

def get_input_values():
    row=int(input("Введите ряд: "))
    column=int(input("Введите столбец: "))
    return (row, column)

def set_coordinates(row,column,element_type):
    field[row][column]=element_type


def print_field():
    for element in field:
        print(element)

def get_symbol(turn):
    if turn%2==0:
        element="O"
    else:
        element="X"
    return element

def check_win_O():
    if "O" in field[0] and "X" not in field[0] and "*" not in field[0] or "O" in field[1] and "X" not in field[1] and "*" not in field[1] or "O" in field[2] and "X" not in field[2] and "*" not in field[2] :
        return True
    elif field[0][0]=="O" and field[1][0]=="O" and field[2][0]=="O":
        return True
    elif field[0][1]=="O" and field[1][1]=="O" and field[2][1]=="O":
        return True
    elif field[0][2]=="O" and field[1][2]=="O" and field[2][2]=="O":
        return True
    elif field[0][0]=="O" and field[1][1]=="O" and field[2][2]=="O":
        return True
    elif field[0][2]=="O" and field[1][1]=="O" and field[0][2]=="O":
        return True
def check_win_X():
    if "X" in field[0] and "O" not in field[0] and "*" not in field[0] or "X" in field[1] and "O" not in field[1] and "*" not in field[1] or "X" in field[2] and "O" not in field[2] and "*" not in field[2] :
        return True
    elif field[0][0]=="X" and field[0][1]=="X" and field[0][2]=="X":
        return True
    elif field[0][0]=="X" and field[1][0]=="X" and field[2][0]=="X":
        return True
    elif field[0][1]=="X" and field[1][1]=="X" and field[2][1]=="X":
        return True
    elif field[0][2]=="X" and field[1][2]=="X" and field[2][2]=="X":
        return True
    elif field[0][0]=="X" and field[1][1]=="X" and field[2][2]=="X":
        return True
    elif field[0][2]=="X" and field[1][1]=="X" and field[2][0]=="X":
        return True
    
    

def game_loop():
    for i in range(1,10):
        row,column=get_input_values()
        element=get_symbol(i)
        set_coordinates(row,column,element)
        print_field()
        if check_win_O():
            print("Нолики выиграли")
            break
        elif check_win_X():
            print("Крестики выиграли")
            break
        elif i>=9:
            print("Ничья")
game_loop()
