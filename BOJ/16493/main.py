def main():
    n, m = map(int, input().split())
    cost_days = []
    reward_pages = []

    for _ in range(m):
        cost, days = map(int, input().split())
        cost_days.append(cost)
        reward_pages.append(days)

    cache = [[-1] * (n + 1) for _ in range(m)]

    def dp(idx, cost_left):
        if idx < 0 or cost_left <= 0:
            return 0
        if cache[idx][cost_left] != -1:
            return cache[idx][cost_left]

        take = 0
        if cost_left >= cost_days[idx]:
            take = dp(idx - 1, cost_left - cost_days[idx]) + reward_pages[idx]

        skip = dp(idx - 1, cost_left)

        cache[idx][cost_left] = max(take, skip)
        return cache[idx][cost_left]

    print(dp(m - 1, n))

if __name__ == '__main__':
    main()