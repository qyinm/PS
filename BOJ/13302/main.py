import sys

def dp(cache, coupon, day, n, closed):
    if day > n:
        return 0

    if (coupon, day) in cache:
        return cache[(coupon, day)]

    if day in closed:
        cache[(coupon, day)] = dp(cache, coupon, day + 1, n, closed)
        return cache[(coupon, day)]

    ret = min(10_000 + dp(cache, coupon, day + 1, n, closed), 25_000 + dp(cache, coupon + 1, day + 3, n, closed), 37_000 + dp(cache, coupon + 2, day + 5, n, closed))

    # 쿠폰 3장이 있으면 1일 무료
    if coupon >= 3:
        ret = min(ret, dp(cache, coupon - 3, day + 1, n, closed))

    cache[(coupon, day)] = ret
    return ret


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    closed = set(map(int, input().split()))

    cache = dict()
    print(dp(cache, 0, 1, n, closed))


if __name__ == "__main__":
    main()