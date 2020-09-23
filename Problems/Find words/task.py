inp = input()
inp = inp.split()
mylist =[]
for i in inp:
    if i.endswith("s"):
        mylist.append(i)

mylist = "_".join(mylist)
print(mylist)