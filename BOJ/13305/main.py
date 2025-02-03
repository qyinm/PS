import sys
input = sys.stdin.readline

n = int(input())
distances = list(map(int, input().split()))
gasoline = list(map(int, input().split()))

prev_idx = 0
idx = 1
answer = 0
while idx < n:
    minGas = gasoline[prev_idx]
    while idx < n - 1 and minGas < gasoline[idx]:
        idx += 1
    for j in range(prev_idx, idx):
        answer += minGas * distances[j]
    prev_idx = idx
    idx += 1
print(answer)