t = [0, 1, 2]
n = int(input())
for x in range(3, n+1):
    t.append(t[x - 1] + t[x - 2])
print(t[n])