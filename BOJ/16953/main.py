from collections import deque

start, end = map(int, input().split())

weights = [(2, 0), (10, 1)]
q = deque([(start, 1)])
visited = set()
visited.add(start)

while q:
    curr, step = q.popleft()

    if curr == end:
        print(step)
        exit(0)

    for w, b in weights:
        nxt = curr * w + b
        if nxt > end or nxt in visited:
            continue
        visited.add(nxt)
        q.append((nxt, step + 1))

print(-1)