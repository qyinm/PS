import sys
input = sys.stdin.readline
string = input().rstrip()

count_alpha = [{string[0]: 1}]
for s in string[1:]:
    prev = count_alpha[-1].copy()
    if not s in prev:
        prev[s] = 0
    prev[s] += 1
    count_alpha.append(prev)

query = int(input())
for _ in range(query):
    findS, l, r = input().split()
    l = int(l)
    r = int(r)

    lfind = 0 if l <= 0 else count_alpha[l - 1].get(findS, 0)
    rfind = count_alpha[r].get(findS, 0)
    print(rfind - lfind)