pos = input()
user_split = [(pos[i:i + 3]) for i in range(0, len(pos), 3)]
user_list = [i for i in pos]
x_total = [x for x in user_list if x == "X"]
o_total = [o for o in user_list if o == "O"]

column_a = "".join(map(str, [pos[0], pos[3], pos[6]]))
column_b = "".join(map(str, [pos[1], pos[4], pos[7]]))
column_c = "".join(map(str, [pos[2], pos[5], pos[8]]))
row_a = user_split[0]
row_b = user_split[1]
row_c = user_split[2]
diagonal_right = "".join(map(str, [pos[2], pos[4], pos[6]]))
diagonal_left = "".join(map(str, [pos[0], pos[4], pos[8]]))

matrix_list = [column_a, column_b, column_c, row_a, row_b, row_c, diagonal_left, diagonal_right]

print("---------")
print(f"| {pos[0]} {pos[1]} {pos[2]} |")
print(f"| {pos[3]} {pos[4]} {pos[5]} |")
print(f"| {pos[6]} {pos[7]} {pos[8]} |")
print("---------")


def first_board():
    win_counter = 0
    x_wins = 0
    o_wins = 0

    # checks to see if there are more or less of one input on the field
    if len(x_total) + 2 <= len(o_total) or len(o_total) + 2 <= len(x_total):
        print("Impossible")
        exit()

    # iterates through direction of win to see if there is a winning combo
    # does not iterate diagonally
    for x in matrix_list:
        if x == "XXX":
            win_counter += 1
            x_wins += 1
        if x == "OOO":
            win_counter += 1
            o_wins += 1

    # checks table state for errors/winners
    # total_wins = x_wins + o_wins
    # if total_wins > 1:
    # print("Impossible")
    # elif x_wins > 0:
    # print("X wins")
    # exit()
    # elif o_wins > 0:
    # print("O wins")
    # exit()
    # elif o_wins == 0 and x_wins == 0 and "_" in user_list:
    # print("Game not finished")
    # elif o_wins == 0 and x_wins == 0:
    # print("Draw")
    # exit()


def second_board():
    i = 0
    coordinate_input = []

    while i < 1:
        coordinate_input = [x for x in (input("Enter the coordinates: ").split())]

        column = int(coordinate_input[0]) - 1
        row = 3 - int(coordinate_input[1])
        index = (row * 3) + column

        new = pos[:index] + "X" + pos[index + 1:]

        for x in coordinate_input:
            if not x.isdigit():
                print("You should enter numbers!")
                break
            elif int(x) not in [1, 2, 3]:
                print("Coordinates should be from 1 to 3!")
                break
            elif pos[index] == "X" or pos[index] == "O":
                print("This cell is occupied! Choose another one!")
                break
            else:
                i += 1

    print("---------")
    print(f"| {new[0]} {new[1]} {new[2]} |")
    print(f"| {new[3]} {new[4]} {new[5]} |")
    print(f"| {new[6]} {new[7]} {new[8]} |")
    print("---------")


first_board()
second_board()
