data = list(map(int, input().split()))
data = map(lambda x: x**2, data)
summ = sum(data)
print(summ % 10)
