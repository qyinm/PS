import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

volums = [*map(int, input().split())]
cache = [[-2 for _ in range(k+1)] for _ in range(51)]

def valid(val):
    global k
    return 0 <= val and val <= k
    
def recur(idx, val):
    global n, k
    if idx == n:
        return val
    if cache[idx][val] != -2:
        return cache[idx][val]
    up = val+volums[idx]
    down = val-volums[idx]
    
    if valid(up) and valid(down):
        cache[idx][val] = max(recur(idx+1, up), recur(idx+1, down))
    elif valid(up):
        cache[idx][val] = recur(idx+1, up)
    elif valid(down):
        cache[idx][val] = recur(idx+1, down)
    else:
        cache[idx][val] = -1
    return cache[idx][val]
    
print(recur(0, m))
    
