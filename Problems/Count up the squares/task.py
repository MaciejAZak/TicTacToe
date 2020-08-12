my_sum = 0
squares = 0
while True:
    number = int(input())
    my_sum = my_sum + number
    squares = squares + (number ** 2)
    if my_sum == 0:
        break

print(squares)