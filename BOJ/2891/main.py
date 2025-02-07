import sys
input = sys.stdin.readline

from collections import deque

N, S, R = map(int, input().split())



ls = set(map(int, input().split()))
lr = set(map(int, input().split()))
inter = lr & ls
ls = list(ls - inter)
lr = list(lr - inter)
ls.sort()

cnt = 0
for s in ls:
    if s - 1 in lr:
        lr.remove(s - 1)
    elif s + 1 in lr:
        lr.remove(s + 1)
    else:
        cnt += 1
print(cnt)