from collections import deque

isPrime = [True] * 10000

for i in range(2, 10000):
    if not isPrime[i]:
        continue
    for j in range(i + i, 10000, i):
        isPrime[j] = False

def bfs(start, to):
    q = deque()
    visited = [-1] * 10000
    q.append(start)
    visited[start] = 0

    while len(q) > 0:
        curr = q.popleft()
        
        if curr == to:
            return visited[curr]
        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0:
                    continue
                curr_list = list(str(curr))
                next_number_str = curr_list
                next_number_str[i] = str(j)
                next_number = int(''.join(next_number_str))

                if not isPrime[next_number] or visited[next_number] != -1:
                    continue
                visited[next_number] = visited[curr] + 1
                q.append(next_number)
                #print(f"next_number: {next_number}")
        
def solve():
    start, to = map(int, input().split())
    print(bfs(start, to))

def main():
    tc = int(input())

    for _ in range(tc):
        solve()

if __name__ == "__main__":
    main()