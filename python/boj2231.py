n = int(input())
min = 1000000
temp = 0
sw = False
for i in range(1, n+1):
    temp = i 
    ti = list(str(i))
    for j in ti:
        temp += int(j)
    if temp == n and min > temp:
        min = i
        sw = True
if sw:
    print(min)
else:
    print(0)