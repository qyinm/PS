import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def solve(s, e):
    if len(e) == len(s):
        if s == e:
            print(1)
            exit(0)
        else:
            return 0
    b = 0
    a = 0
    if e[0] == 'B':
        b = solve(s, e[1::][::-1])
    if e[-1] == 'A':
        a = solve(s, e[:-1])
    return max(b, a)
    
def main():
    s = input().rstrip()
    e = input().rstrip()

    ans = solve(s, e)
    print(ans)

if __name__ == "__main__":
    main()
