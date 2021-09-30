import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    x, y = input().split()
    temp = [x, y]
    data.append(temp)
data.sort()

for i in range(n):
    print(data[i][0], data[i][1])