dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
inp = input()
list = inp.split()
i = 0
for word in list:
    if word not in dictionary:
        print(word)
    else:
        i += 1

if i == len(list):
    print("OK")