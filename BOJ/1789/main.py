import sys
sys.setrecursionlimit(10**6)

def solve(n, prev):
    if n < 0:
        return -1
    ret = 0
    k = prev + 1
    while True:
        ret = solve(n - k, k) + 1
        if ret != -1:
            break
        k += 1
    return ret
    

def main():
    n = int(input())
    ans = solve(n, 0)
    print(ans)

if __name__ == "__main__":
    main()
