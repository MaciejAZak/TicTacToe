inp = input()
list = [int(x) for x in inp]
new_list = [sum(list[:i +1]) for i in range(len(list))]
print(new_list)