import sys
input = sys.stdin.readline;

prime = []
chey = [False for _ in range(100_001)]

for i in range(2, 100_001):
    if chey[i] == True:
        continue
    prime.append(str(i))
    for j in range(i + i, 100_001, i):
        chey[j] = True


while True:
    baseN = input()
    if int(baseN)== 0:
        break
    for x in prime[::-1]:
        if x in baseN:
            print(x)
            break
    
