n = int(input())
data = [0 for i in range(n+1)]

for i in range(n):
    t = int(input())
    data[t] += 1

for i in range(n+1):
    if data[i]:
        for j in range(data[i]):
            print(i)