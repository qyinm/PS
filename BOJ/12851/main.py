from collections import deque
import sys
input = sys.stdin.readline

def main():
    start, target = map(int, input().split())
    
    if start == target:
        print(0)
        print(1)
        return
    
    MAX = 100001
    visited = [-1] * MAX
    count = [0] * MAX
    
    queue = deque([start])
    visited[start] = 0
    count[start] = 1
    
    while queue:
        curr = queue.popleft()
        
        for next_pos in [curr - 1, curr + 1, curr * 2]:
            if next_pos < 0 or next_pos >= MAX:
                continue
            
            if visited[next_pos] == -1:
                visited[next_pos] = visited[curr] + 1
                count[next_pos] = count[curr]
                queue.append(next_pos)
            elif visited[next_pos] == visited[curr] + 1:
                count[next_pos] += count[curr]
    
    print(visited[target])
    print(count[target])

if __name__ == "__main__":
    main()