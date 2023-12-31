import sys
from collections import deque

input = sys.stdin.readline

def bfs(s, e, graph):
    
    queue = deque([])
    queue.append(s)
    
    visited = [False] * len(graph[0])
    
    while queue:
        cur = queue.popleft()
        if cur == e:
            return True
        for idx, val in enumerate(graph[cur]):
            if val == 0 or visited[idx]:
                continue
            visited[idx] = True
            queue.append(idx)
    
    return False
    

def main():
    n = int(input())
    m = int(input())
    graph = [[*map(int, input().split())] for _ in range(n)]
    course = [*map(int, input().split())]
    for i in range(len(course)-1):
        start, end = course[i], course[i+1]
        if not bfs(start-1, end-1, graph):
            print("NO")
            return
    print("YES")
    
if __name__ == "__main__":
    main()
