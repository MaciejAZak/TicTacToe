list = []
while True:
    name = input()
    if name == ".":
        break
    else:
        list.append(name)
print(list)
print(len(list))