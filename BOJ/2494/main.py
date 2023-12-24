import sys
sys.setrecursionlimit(10**9)

end = []
start = []

def dp(cache, level, n, left_turn):
    if level > n:
        return 0
    num = (start[level-1] + left_turn) % 10
    if cache[num][level][0] != -1:
        return cache[num][level][0]
        
    left_add = (10 + end[level-1] - num) % 10
    right_add = 10 - left_add
    
    left = dp(cache, level+1, n, (left_turn + left_add) % 10) + left_add
    right = dp(cache, level+1, n, left_turn) + right_add
    
    if left >= right:
        cache[num][level][1] = -right_add
        cache[num][level][0] = right
    else:
        cache[num][level][1] = left_add
        cache[num][level][0] = left
    
    return cache[num][level][0]
    

def main():
    global end, start
    n = int(input())
    start = [*map(int, input())]
    end = [*map(int, input())]
    cache = [[[-1, -1] for _ in range(n+1)]  for _ in range(10)]
    ans = dp(cache, 1, n, 0)
    print(ans)
    #print(answer)
    num = start[0]
    left = 0
    for i in range(1, n+1):
        print(i, cache[num][i][1])
        if cache[num][i][1] > 0:
            left += cache[num][i][1]
            left %= 10
        if i != n:
            num = (start[i] + left) % 10
    
if __name__ == "__main__":
    main()
