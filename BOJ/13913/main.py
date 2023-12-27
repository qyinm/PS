from collections import deque

def acc(cmd, num):
    match cmd:
        case 0:
            return num - 1
        case 1:
            return num + 1
        case 2:
            return num // 2

def main():
    n, k = map(int, input().split())
    cache = [[-1, -1] for _ in range(1000001)]
    queue = deque([])
    queue.append(k)

    cache[k][0] = 0
    while queue:
        cur = queue.popleft()
        if cur == n:
            break
        l = cur % 2
        for i in range(3 - l):
            nxt = acc(i, cur)
            if nxt < 0 or nxt > 1000000 or cache[nxt][0] != -1:
                continue
            cache[nxt][0] = cache[cur][0] + 1
            cache[nxt][1] = cur
            queue.append(nxt)
    print(cache[n][0])
    while cache[n][0] != -1:
        print(n, end=" ")
        n = cache[n][1]
    
if __name__ == "__main__":
    main()
