data = list(map(int, input().split()))
data.sort()

orders = list(input())

for order in orders:
    idx = ord(order) - ord('A')
    print(data[idx], end=" ")