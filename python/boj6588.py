import sys

max = 1000000
ch = [True for _ in range(max + 1)]


n = int(max ** 0.5)
for i in range(2, n + 1):
    if ch[i]:
        for j in range(i * 2, max + 1, i):
            ch[j] = False

while True:
    n = int(sys.stdin.readline())

    if n == 0:  break

    flag = True
    for i in range(3, len(ch)):
        if ch[i] and ch[n - i]:   
            print("%d = %d + %d"%(n, i, n - i))
            flag = False
            break         
    if flag:
        print("Goldbach's conjecture is wrong.")