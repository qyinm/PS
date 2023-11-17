n, k = map(int, input().split())

m1 = [[*map(int, input().split())] for _ in range(n)]
m2 = [[*map(int, input().split())] for _ in range(n)]

for i in range(n):
    for j in range(k):
        m1[i][j] += m2[i][j]

for i in range(n):
    for j in range(k):
        print(m1[i][j], end=' ')
    print('')
