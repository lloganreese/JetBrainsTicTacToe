pos = "_________"

column_a = "".join(map(str, [pos[0], pos[3], pos[6]]))
column_b = "".join(map(str, [pos[1], pos[4], pos[7]]))
column_c = "".join(map(str, [pos[2], pos[5], pos[8]]))
row_a = "".join(map(str, [pos[0], pos[1], pos[2]]))
row_b = "".join(map(str, [pos[3], pos[4], pos[5]]))
row_c = "".join(map(str, [pos[6], pos[7], pos[8]]))
diagonal_right = "".join(map(str, [pos[2], pos[4], pos[6]]))
diagonal_left = "".join(map(str, [pos[0], pos[4], pos[8]]))

matrix_list = [column_a, column_b, column_c,
               row_a, row_b, row_c, diagonal_left,
               diagonal_right]
matrix_list_new = [pos]


def print_board(position):
    print("---------")
    print(f"| {position[0]} {position[1]} {position[2]} |")
    print(f"| {position[3]} {position[4]} {position[5]} |")
    print(f"| {position[6]} {position[7]} {position[8]} |")
    print("---------")


def play_game(user):
    global pos
    i = 0

    while i != 1:
        x, y = input("Enter the coordinates: ").split()

        if not x.isdigit() or not y.isdigit():
            print("You should enter numbers!")
            continue
        elif int(x) not in range(1, 4) or int(y) not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
            continue

        column = int(x) - 1
        row = 3 - int(y)
        index = (row * 3) + column

        if pos[index] == "X" or pos[index] == "O":
            print("This cell is occupied! Choose another one!")
            continue
        else:
            i += 1
            pos = pos[:index] + user + pos[index + 1:]
            create_board(pos)

    return pos


def create_board(new):
    global matrix_list_new

    column_a_new = "".join(map(str, [new[0], new[3], new[6]]))
    column_b_new = "".join(map(str, [new[1], new[4], new[7]]))
    column_c_new = "".join(map(str, [new[2], new[5], new[8]]))
    row_a_new = "".join(map(str, [new[0], new[1], new[2]]))
    row_b_new = "".join(map(str, [new[3], new[4], new[5]]))
    row_c_new = "".join(map(str, [new[6], new[7], new[8]]))
    diagonal_right_new = "".join(map(str, [new[2], new[4], new[6]]))
    diagonal_left_new = "".join(map(str, [new[0], new[4], new[8]]))

    matrix_list_new = [column_a_new, column_b_new, column_c_new,
                       row_a_new, row_b_new, row_c_new, diagonal_left_new,
                       diagonal_right_new]

    return matrix_list_new


def main():
    total_plays = 0

    while total_plays < 9:
        play_game(user="X")
        print_board(pos)
        total_plays += 1
        win_checker()

        if total_plays == 9:
            print("Draw")
            break

        play_game(user="O")
        print_board(pos)
        total_plays += 1
        win_checker()


def win_checker():
    for x in matrix_list_new:
        if x == "XXX":
            print("X wins")
            exit()
        if x == "OOO":
            print("O wins")
            exit()


main()
