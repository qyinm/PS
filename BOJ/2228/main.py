import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    arr = [0]*(N+1)
    for i in range(1, N+1):
        arr[i] = int(input())
        
    psum = [0]*(N+1)
    for i in range(1, N+1):
        psum[i] = psum[i-1] + arr[i]
    
    dp = [[float('-inf')]*(M+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 0 
    
    for i in range(1, N+1):
        for msel in range(1, M+1):
            dp[i][msel] = dp[i-1][msel]
            
            for s in range(1, i+1):
                val = psum[i] - psum[s-1]
                if s >= 2:
                    dp[i][msel] = max(dp[i][msel], dp[s-2][msel-1] + val)
                else:
                    if msel-1 == 0:
                        dp[i][msel] = max(dp[i][msel], val)
    
    print(dp[N][M])

if __name__ == "__main__":
    main()