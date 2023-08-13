n, s = map(int, input().split())

data = list(map(int, input().split()))
INF = 987654321
minLen = INF
right = 0
left = 0

ssum = 0
for right in range(0, n):
    ssum += data[right]
    if ssum >= s:
        minLen = right + 1
        break

while left < n - 1:
    ssum -= data[left]
    left += 1
    if ssum >= s:
        minLen = min(right - left + 1, minLen)
        continue
    while ssum < s and right < n-1:
        right += 1
        ssum += data[right]
if minLen == INF:
    print(0)
else:
    print(minLen)