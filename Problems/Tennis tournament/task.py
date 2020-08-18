n = int(input())
winners = []
wins = 0
for i in range(n):
    match = input().split()
    if match[1] == "win":
        winners.append(match[0])
        wins += 1
print(winners)
print(len(winners))