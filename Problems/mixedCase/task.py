inp = input()
split = inp.title().split()
split[0] = split[0].lower()
if len(split) != 1:
    join = "".join(split)
else:
    join = inp.lower()
print(join)
