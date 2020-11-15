# write your code here
pos = input()
user_split = [(pos[i:i + 3]) for i in range(0, len(pos), 3)]
user_list = [i for i in pos]
x_total = [x for x in user_list if x == "X"]
o_total = [o for o in user_list if o == "O"]
win_counter = 0
x_wins = 0
o_wins = 0

column_a = []
column_b = []
column_c = []
row_a = user_split[0]
row_b = user_split[1]
row_c = user_split[2]

for row in user_split:  # creates columns from list of user inputs
    column_a.append(row[0])
column_a = "".join(column_a)

for row in user_split:
    column_b.append(row[1])
column_b = "".join(column_b)

for row in user_split:
    column_c.append(row[2])
column_c = "".join(column_c)

matrix_list = [column_a, column_b, column_c, row_a, row_b, row_c]

print("---------")
print(f"| {pos[0]} {pos[1]} {pos[2]} |")
print(f"| {pos[3]} {pos[4]} {pos[5]} |")
print(f"| {pos[6]} {pos[7]} {pos[8]} |")
print("---------")

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

# checks for a diagonal win
if pos[0] == "X" and pos[0] == pos[4] and pos[4] == pos[8]:
    x_wins += 1
    win_counter += 1
if pos[0] == "0" and pos[0] == pos[4] and pos[4] == pos[8]:
    o_wins += 1
    win_counter += 1
if pos[2] == "X" and pos[2] == pos[4] and pos[4] == pos[6]:
    x_wins += 1
    win_counter += 1
if pos[2] == "0" and pos[2] == pos[4] and pos[4] == pos[6]:
    o_wins += 1
    win_counter += 1

total_wins = x_wins + o_wins

# checks variables for winner and errors
if total_wins > 1:
    print("Impossible")
elif x_wins > 0:
    print("X wins")
elif o_wins > 0:
    print("O wins")
elif o_wins == 0 and x_wins == 0 and "_" in user_list:
    print("Game not finished")
elif o_wins == 0 and x_wins == 0:
    print("Draw")
