def solve():
    m = int(input())
    di = {}
    for _ in range(m):
        v, k = input().split()
        if k not in di:
            di[k] = []
        di[k].append(v)
    
    ans = 1
    for k, v in di.items():
        ans *= len(v) + 1
    print(ans - 1)

def main():
    n = int(input())
    
    for _ in range(n):
        solve()

if __name__ == "__main__":
    main()