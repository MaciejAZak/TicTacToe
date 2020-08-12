inp = input()
list = [float(x) for x in inp]
my_sum = 0
for x in list:
    my_sum = my_sum + x

mean = my_sum / len(list)
print(mean)