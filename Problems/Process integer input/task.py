while True:
    number = int(input())
    if number < 10:
        continue
    if number > 100:
        break
    else:
        print(number)