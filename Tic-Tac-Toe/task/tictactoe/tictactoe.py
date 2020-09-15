def askForInput():
    validSymbols = ["X", "O", "_"]
    inp = input("Enter cells:")
    if len(inp) != 9:
        print("Invalid input, try again")
        askForInput()
    else:
        for i in inp:
            if i not in validSymbols:
                print("Invalid input, try again")
                askForInput()
            else:
                continue

        Board = f"""---------
| {inp[0]} {inp[1]} {inp[2]} |
| {inp[3]} {inp[4]} {inp[5]} |
| {inp[6]} {inp[7]} {inp[8]} |
---------"""
        print(Board)

askForInput()