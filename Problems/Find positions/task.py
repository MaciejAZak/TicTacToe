# put your python code here
Myinput = input()
Mynumber = input()
numbers = Myinput.split()

answer = []
i = 0
for number in numbers:
    if number == Mynumber:
        answer.append(str(i))
    i += 1
if len(answer) == 0:
    print("not found")
else:
    answer = " ".join(answer)
    print(answer)