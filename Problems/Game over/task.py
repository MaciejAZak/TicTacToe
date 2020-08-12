scores = input().split()
# put your python code here
correct = 0
incorrect = 0
for answer in scores:
    if answer == "C":
        correct += 1
    if answer == "I":
        incorrect += 1
    if incorrect >= 3:
        break

if incorrect >= 3:
    print("Game over")
    print(correct)
else:
    print("You won")
    print(correct)