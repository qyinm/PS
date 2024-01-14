ans = []
wn = 0
weights = []

def dp(curr, idx, cache):
    if curr == 0:
        return 1
    if idx == wn:
        return 0
    if cache[idx][curr] != -1:
        return cache[idx][curr]
    ldp = dp(abs(curr-weights[idx]), idx+1, cache)
    if ldp == 1:
        cache[idx][curr] = ldp
        return 1
    rdp = dp(curr+weights[idx], idx+1, cache)
    if rdp == 1:
        cache[idx][curr] = rdp
        return 1
    mdp = dp(curr, idx+1, cache)
    if mdp == 1:
        cache[idx][curr] = mdp
        return 1
    cache[idx][curr] = 0
    return 0

def main():
    global wn, weights
    wn = int(input())
    weights = [*map(int, input().split())]
    bn = int(input())
    bizs = [*map(int, input().split())]
    
    cache = [[-1] * 55001 for _ in range(wn+1)]
    for biz in bizs:
        ret = 'Y' if dp(biz, 0, cache) == 1 else 'N'
        ans.append(ret)
    print(*ans)
    
if __name__ == "__main__":
    main()