import sys
sys.setrecursionlimit(10**6)

def dfs(start: int, link: list, visited: list):
    if visited[start]:  return
    visited[start] = True

    dfs(link[start] - 1, link, visited)
        

def find_cycle():
    n = int(input())
    link = list(map(int, input().split()))
    visited = [False] * (n)

    cnt = 0
    for s in range(n):
        if visited[s]:  continue
        dfs(s, link, visited)
        cnt += 1
    
    return cnt

def main():
    tc = int(input())
    for _ in range(tc):
        print(find_cycle())

if __name__ == "__main__":
    main()