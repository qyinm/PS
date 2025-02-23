def main():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i]  = max(dp[i], dp[j]+1)
    lis_len = max(dp)
    print(n - lis_len + 1)

if __name__ == "__main__":
    main()