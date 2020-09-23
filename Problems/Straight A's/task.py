# put your python code here
marks = input()
A = marks.split()
i = 0
for mark in A:
    if mark =="A":
        i += 1
print(round(i/len(A),2))