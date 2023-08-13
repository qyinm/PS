import sys
input = sys.stdin.readline

data = []
result = []
for _ in range(9):
    data.append(int(input()))
s = sum(data)
for i in range(9):
    for j in range(9):
        if s - (data[i] + data[j]) == 100 and i != j:
            a = data[i]
            b = data[j]
            data.remove(a)
            data.remove(b)
            break
    if len(data) == 7:
        break

data.sort()
for h in data:
    print(h)