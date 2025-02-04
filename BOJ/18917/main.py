import sys
input = sys.stdin.readline

M = int(input())

l = []
xor = 0
sum = 0
for _ in range(M):
    query = list(map(int, input().split()))

    if query[0] == 1:
        sum += query[1]
        xor ^= query[1]
    elif query[0] == 2:
        sum -= query[1]
        xor ^= query[1]
    elif query[0] == 3:
        print(sum)
    elif query[0] == 4:
        print(xor)