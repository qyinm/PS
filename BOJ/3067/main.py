import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def main():
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    cache = [[-1] * (m + 1) for _ in range(n)]

    def dp(left_cost, idx):
        if left_cost < 0:
            return 0
        if left_cost == 0:
            return 1
        if cache[idx][left_cost] != -1:
            return cache[idx][left_cost]
        
        cache[idx][left_cost] = 0
        for index, coin in enumerate(coins):
            if idx <= index:
                cache[idx][left_cost] += dp(left_cost - coin, index)
            
        return cache[idx][left_cost]
    
    print(dp(m, 0))

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        main()