my_list = []
while True:
    variable = input()
    if variable == ".":
        break
    else:
        number = float(variable)
        my_list.append(number)

print(min(my_list))