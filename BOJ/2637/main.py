import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = 0

def dp(n,cache, relation):
    if cache[n][0] != -1:
        return cache[n]
    cache[n] =  [0 for i in range(N+1)]
    if not relation[n]:
        try:
            cache[n][n] = 1
        except:
            print(n)
            exit(0)
        return cache[n]
    
    for num, cnt in relation[n].items():
        ret = dp(num, cache, relation)[1:]
        for i, r in enumerate(ret):
            try:
                cache[n][i+1] += r * cnt
            except Exception:
                print(i, r)
                exit(0)
    
    return cache[n]
    
    
def main():
    global N
    n = int(input())
    N = n
    relation = [{} for _ in range(n+1)]
    cache = [[-1] * (n+1) for _ in range(n+1)]
    query = int(input())
    for _ in range(query):
        parent, child, cnt = map(int, input().split())
        relation[parent][child] = cnt
    ans = dp(n, cache, relation)[1:]
    
    for i, val in enumerate(ans):
        if val < 1:
            continue
        print(i+1, val)
    
    
if __name__ == "__main__":
    main()
