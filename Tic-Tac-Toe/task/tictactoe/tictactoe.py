import math

def askForInput():
    valid_values = ['X', 'O', '_']
    cells_values = input('Enter cells: ')
    if len(cells_values) != 9:
        print("invalid value!")
        askForInput()
    else:
        for char in cells_values:
            if char not in valid_values:
                print("invalid value!")
                askForInput()
            else:
                continue
        print('---------')
        print('|', cells_values[0], cells_values[1], cells_values[2], '|')
        print('|', cells_values[3], cells_values[4], cells_values[5], '|')
        print('|', cells_values[6], cells_values[7], cells_values[8], '|')
        print('---------')

        x = 0
        o = 0
        result = ""
        for i in cells_values:
            if i == "X":
                x += 1
            if i == "O":
                o += 1
        if math.fabs(x - o) > 1:
            result = "imp"

        win1 = [cells_values[0], cells_values[1], cells_values[2]]
        win2 = [cells_values[3], cells_values[4], cells_values[5]]
        win3 = [cells_values[6], cells_values[7], cells_values[8]]
        win4 = [cells_values[0], cells_values[3], cells_values[6]]
        win5 = [cells_values[1], cells_values[4], cells_values[7]]
        win6 = [cells_values[2], cells_values[5], cells_values[8]]
        win7 = [cells_values[0], cells_values[4], cells_values[8]]
        win8 = [cells_values[2], cells_values[4], cells_values[6]]

        results = [win1, win2, win3, win4, win5, win6, win7, win8]
        x_winner = False
        o_winner = False
        not_finished = False

        for i in results:
            if i == ["X", "X", "X"]:
                x_winner = True
            elif i == ["O", "O", "O"]:
                o_winner = True

        if x_winner is True and o_winner is True:
            if result == "":
                result = "imp"
        elif x_winner is True and o_winner is False:
            if result == "":
                result = "X"
        elif x_winner is False and o_winner is True:
            if result == "":
                result = "O"
        elif x_winner is False and o_winner is False:
            for i in cells_values:
                if i == "_":
                    result = "not"
                else:
                    result = "Draw"


        if result == "imp":
            print("Impossible")
        elif result == "X":
            print("X wins")
        elif result == "O":
            print("O wins")
        elif result == "not":
            print("Game not finished")
        elif result == "Draw":
            print("Draw")



# ***********************************************
askForInput()