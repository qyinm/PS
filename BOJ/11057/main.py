n = int(input())
cache = [[0] * 10 for _ in range(n+1)]

for i in range(10):
    cache[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        cache[i][j] = sum(cache[i-1][j:]) % 10007
        
print(sum(cache[n]) % 10007)
