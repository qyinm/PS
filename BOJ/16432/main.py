import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = 0
ricecakes = []
cache = [[[-1] * (1001) for _ in range(10)] for _ in range(2)]

def dp(day, rice):
    if day == n:
        return 1
    if cache[0][rice][day] != -1:
        return cache[0][rice][day]
    
    nxt, maxx = 0, 0
    for cake in ricecakes[day]:
        if cake == rice:
            continue
        ret = dp(day+1, cake)
        if ret > maxx:
            maxx = ret + 1
            nxt = cake
    cache[0][rice][day] = maxx
    cache[1][rice][day] = nxt
    return cache[0][rice][day]

def main():
    global ricecakes, rice_n, n
    
    n = int(input())
    
    for _ in range(n):
        data = [*map(int, input().split())]
        ricecakes.append(data[1:])
    ans = dp(0, 0)
    if ans == 0:
        print(-1)
        exit(0)
    cur = 0
    for i in range(n):
        print(cache[1][cur][i])
        cur = cache[1][cur][i]
        
if __name__ == "__main__":
    main()