height = int(input())

block = "#"

i = 0
while i < height:
    level = block.center(2 * height - 1)
    block = "#" + block + "#"
    print(level)
    i += 1