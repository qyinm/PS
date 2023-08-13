n = int(input())
d = []

for i in range(n):
    d.append(int(input()))
d = sorted(set(d))
for i in d:
    print(i)