import sys
sys.setrecursionlimit(10**6)

def lcs(str1, str2, n, m, dp):
    if n == -1 or m == -1:
        return 0
    if dp[n][m] != -1:
        return dp[n][m]
    if str1[n] == str2[m]:
        dp[n][m] = 1 + lcs(str1, str2, n-1, m-1, dp)
        return dp[n][m]
    dp[n][m] = max(lcs(str1, str2, n-1, m, dp), lcs(str1, str2, n, m-1, dp)) 
    return dp[n][m]

def main():
    str1, str2 = list(input()), list(input())
    n, m = len(str1), len(str2)
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    print(lcs(str1, str2, n-1, m-1, dp))

if __name__ == "__main__":
    main()