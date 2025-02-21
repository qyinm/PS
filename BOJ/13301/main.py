n = int(input())

cache = [1, 1]

for _ in range(2, n + 1):
    cache.append(cache[-1] + cache[-2])

area = [4, 6]
for i in range(2, n + 1):
    area.append(3 * cache[i] + area[-1] - (cache[i-1] + cache[i-2]))

print(area[n-1])
