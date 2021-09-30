import sys, statistics
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    temp = int(input())
    data.append(temp)
data.sort()

print("%.f"%(sum(data) / n))
print(data[n//2])
result = statistics.multimode(data)
result = result[1] if len(result) > 1 else result[0]
print(result)
print(data[-1] - data[0])
