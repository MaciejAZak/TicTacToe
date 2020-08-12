cafes = []
cats = []
while True:
    name = input()
    if name == "MEOW":
        break
    else:
        cafe = name.split()
        cafes.append(cafe[0])
        cats.append(int(cafe[1]))

my_index = (cats.index(max(cats)))
print(cafes[my_index])

#cats = 0
#for cafe in cafes:
#    cafename = cafe[0]
#    oldcats = cats
#    cats = int(cafe[1])
#    if cats >= oldcats:
#        message = cafename
#
#print(message)

