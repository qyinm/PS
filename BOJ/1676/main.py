n = int(input())

fac = 1
for i in range(1, n+1):
    fac *= i
facs = str(fac)[::-1]
l = len(facs)
i = 0
for a in facs:
    if a == '0':
        i += 1
        continue
    print(i)
    break
