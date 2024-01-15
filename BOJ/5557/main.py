import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = 0
arr = []
cache = []

def dp(idx, val):
    if idx == n-1:
        if val == arr[idx]:
            return 1
        return 0
    if val < 0 or val > 20:
        return 0
    if cache[val][idx] != -1:
        return cache[val][idx]
    cache[val][idx] = 0
    cache[val][idx] = dp(idx+1, val+arr[idx]) + dp(idx+1, val-arr[idx])
    return cache[val][idx]

def main():
    global n, arr, cache
    n = int(input())
    arr = [*map(int, input().split())]
    cache = [[-1] * n for _ in range(21)]
    
    ans = dp(1, arr[0])
    print(ans)
if __name__ == "__main__":
    main()