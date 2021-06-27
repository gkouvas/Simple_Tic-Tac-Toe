# Tic Tac Toe Game
# ttt stands for tic tac toe

# Globals variables
chars_list = ["X", "O", "_"]
stop_list = ["X wins", "O wins", "Impossible"]
winner = []
ttt_nested_list = []
input_string = "_________"  # initialisation of the 9 chars string that will contain the board
input_set = set(input_string)
player = "X"

# This is the function that
#   a) checks that the board is correct and
#   b) create sub_lists to pass them from the who_won function


def check_function(in_string):
    global winner
    global ttt_nested_list
    sub_list = []  # this list is to help with sub-grouping of ttt list horizontally, vertically and diagonally
    x_counter = 0
    o_counter = 0
    empty_counter = 0
    winner = []
    ttt_nested_list = []
    in_set = set(in_string)

    if len(in_string) == 9 and in_set.issubset(chars_list):
        # input the ttt board and print it
        print("---------")
        for i in range(0, 9, 3):
            print('| {} |'.format(' '.join(in_string[i:(i + 3)])))
        print("---------")

        # count the difference between Xs and Os to see if the game is impossible
        for char in in_string:
            if char == "X":
                x_counter += 1
            elif char == "O":
                o_counter += 1
            elif char == "_":
                empty_counter += 1
        if abs(x_counter-o_counter) not in [0, 1]:
            winner.append("Impossible")

        # convert the board in a matrix list and calculate if one won horizontally using the sub_list
        for raws in range(0, 3):
            for sings in range(0, 3):
                j = sings + (raws * 3)
                sub_list.append(in_string[j])
            winner.append(who_won(sub_list)) if who_won(sub_list) is not None else None
            ttt_nested_list.append(sub_list)
            sub_list = []

        # calculate if one won vertically
        for signs in range(0, 3):
            for columns in range(0, 3):
                sub_list.append(ttt_nested_list[columns][signs])
            winner.append(who_won(sub_list)) if who_won(sub_list) is not None else None
            sub_list = []

        # calculate if one won diagonally from top left to right bottom
        for raws in range(0, 3):
            sub_list.append(ttt_nested_list[raws][raws])
        winner.append(who_won(sub_list)) if who_won(sub_list) is not None else None
        sub_list = []

        # calculate if one won diagonally from top right to left bottom
        for raws in range(0, 3):
            sub_list.append(ttt_nested_list[raws][2 - raws])
        winner.append(who_won(sub_list)) if who_won(sub_list) is not None else None


# Who_won function takes as an input a three-items_list and checks if they contain the same sting.
# It is used to pass sub-lists (horizontal, vertical or diagonal) and check if one won.


def who_won(thee_item_list):
    if len(set(thee_item_list)) == 1 and thee_item_list[0] == "X":
        return "X wins"
    elif len(set(thee_item_list)) == 1 and thee_item_list[0] == "O":
        return "O wins"
    elif "_" in set(thee_item_list):
        return "Game not finished"
    else:
        return "Draw"

# Here is where the game starts for the first time.
# The user give an input and we pass it from the check function


check_function(input_string)


# calculate if someone has won and print result
if "X wins" in set(winner) and "O" not in set(winner):
    print("X wins")
elif "O wins" in set(winner) and "X" not in set(winner):
    print("O wins")
elif "Impossible" in set(winner) or ("X" in set(winner) and "O" in set(winner)):
    print("Impossible")
elif "Draw" in set(winner) and "_" not in input_string:
    print("Draw")
elif "Game not finished" in set(winner):
    while any(item in stop_list for item in set(winner)) is False and set(winner) != {"Draw"}:
        coordinates = input("Enter the coordinates:").split()
        if len(coordinates) == 2:
            coordinate_x = coordinates[0]
            coordinate_y = coordinates[1]
            if coordinate_x.isdigit() and coordinate_y.isdigit():
                coordinate_x = int(coordinate_x)
                coordinate_y = int(coordinate_y)
                if 1 <= coordinate_x <= 3 and 1 <= coordinate_y <= 3:
                    position = (coordinate_x-1) * 3 + (coordinate_y-1)
                    if input_string[position] == "_":
                        input_string = input_string[:position] + player + input_string[position + 1:]
                        if player == "X":  # change player, depending on who was playing before
                            player = "O"
                        else:
                            player = "X"
                        check_function(input_string)
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")
        else:
            print("You should enter numbers!")

# Final result
if "X wins" in set(winner) and "O" not in set(winner):
    print("X wins")
elif "O wins" in set(winner) and "X" not in set(winner):
    print("O wins")
elif "Impossible" in set(winner) or ("X" in set(winner) and "O" in set(winner)):
    print("Impossible")
elif "Draw" in set(winner) and "_" not in input_string:
    print("Draw")
