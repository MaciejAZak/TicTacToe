n = int(input())

inner_list = [1, 2]
my_list = []
i = 0
while i < n:
    my_list.append(inner_list)
    i += 1

print(my_list)