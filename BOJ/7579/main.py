import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    used_bytes = list(map(int, input().split()))
    unable_costs = list(map(int, input().split()))

    max_cost = sum(unable_costs)
    cache = [[-1] * (max_cost + 1) for _ in range(n)]

    def dp(idx, cost_left):
        if idx < 0 or cost_left < 0:
            return 0
        if cache[idx][cost_left] != -1:
            return cache[idx][cost_left]
        
        if cost_left >= unable_costs[idx]:
            cache[idx][cost_left] = max(dp(idx - 1, cost_left - unable_costs[idx]) + used_bytes[idx], dp(idx - 1, cost_left))
        else:
            cache[idx][cost_left] = dp(idx - 1, cost_left)
        return cache[idx][cost_left]
        
    for i in range(max_cost + 1):
        if dp(n - 1, i) >= m:
            print(i)
            return

if __name__ == '__main__':
    main()