import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

cache = []

def dp(chapters, n, t, idx):
    if idx == n:
        return 0
    if cache[idx][t] != -1:
        return cache[idx][t]
    k, s = chapters[idx]
    maxx = 0
    if k <= t:
        maxx = max(dp(chapters, n, t - k, idx + 1) + s, dp(chapters, n, t, idx + 1))
    else:
        maxx = dp(chapters, n, t, idx + 1)
    cache[idx][t] = maxx
    return maxx

def main():
    global cache
    n, t = map(int, input().split())
    chapters = []
    for _ in range(n):
        chapter = [*map(int, input().split())]
        chapters.append(chapter)
    cache = [[-1] * (t + 1) for _ in range(n + 1)]
    ans = dp(chapters, n, t, 0)
    print(ans)
    

if __name__ == '__main__':
    main()
