n = int(input())
l = [0, 0]
for _ in range(n):
    l[int(input())] += 1

if l[0] > l[1]:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')