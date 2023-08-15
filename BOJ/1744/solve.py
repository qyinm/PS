import sys

one = []
neg = []
pos = []
n = int(sys.stdin.readline())

for i in range(n):
    tmp = int(sys.stdin.readline())
    if tmp > 1:
        pos.append(tmp)
    elif tmp <= 0:
        neg.append(tmp)
    else:
        one.append(tmp)

pos.sort(reverse=True)
neg.sort()

pos_n = len(pos)
neg_n = len(neg)
ans = len(one)

if neg_n % 2 == 1:
    ans += neg[-1]
    neg_n -= 1
for i in range(0, neg_n-1, 2):
    ans += neg[i] * neg[i+1]
    
if pos_n % 2 == 1:
    ans += pos[-1]
    pos_n -= 1
for i in range(0, pos_n-1, 2):
    ans += pos[i] * pos[i+1]
    
print(ans)
