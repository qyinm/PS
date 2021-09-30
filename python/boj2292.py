N = int(input())
cnt = 1
while N > 1:
    N -= (6 * cnt)
    cnt += 1
print(cnt)