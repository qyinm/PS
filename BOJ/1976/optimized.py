import sys

input = sys.stdin.readline

def dfs(idx, qualify, group, graph):
    
    group[idx] = qualify
    for nxt, val in enumerate(graph[idx]):
        if val == 0 or group[nxt] != -1:
            continue
        dfs(nxt, qualify, group, graph)
    

def main():
    n = int(input())
    m = int(input())
    graph = [[*map(int, input().split())] for _ in range(n)]
    course = [*map(int, input().split())]
    group = [-1] * n
    
    for i in range(n):
        if group[i] != -1:
            continue
        dfs(i, i, group, graph)
    for i in range(m-1):
        s, e = course[i], course[i+1]
        if group[s-1] != group[e-1]:
            print("NO")
            return
    print("YES")
    
if __name__ == "__main__":
    main()
