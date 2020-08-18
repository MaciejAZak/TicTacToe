numbers = input()
my_list = [int(digit) for digit in numbers]
second_list = [((my_list[n] + my_list[n + 1]) / 2) for n in range(len(numbers) -1)]

print(second_list)