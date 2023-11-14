import sys
input = sys.stdin.readline

n = int(input())

v = [[*map(int, input().rstrip())] for _ in range(n)]

def check(n, sx, sy):
    global v
    zero, one = 0, 0
    
    for y in range(sy, sy + n):
        for x in range(sx, sx + n):
            if v[y][x] == 1:
                one += 1
            else:
                zero += 1
    if one == n**2:
        return 1
    elif zero == n**2:
        return 0
    else:
        return -1

def recur(n, sx, sy):
    if n == 0:
        return
    ret = check(n, sx, sy)
    if ret != -1:
        print(ret, end="")
        return
    nextn = n // 2
    print("(", end="")
    recur(nextn, sx, sy)
    recur(nextn, sx + nextn, sy)
    recur(nextn, sx, sy + nextn)
    recur(nextn, sx + nextn, sy + nextn)
    print(")", end="")

recur(n, 0, 0)
    
