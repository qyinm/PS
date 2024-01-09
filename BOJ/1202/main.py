from collections import deque
import sys, heapq
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    
    jewel = []
    bags = []
    
    for _ in range(n):
        weigh, cost = map(int, input().split())
        heapq.heappush(jewel, (weigh, cost))
    for _ in range(k):
        l = int(input())
        bags.append(l)
    ans = 0
    jewel.sort()
    jewel = deque(jewel)
    bags.sort()
    q = []
    for limit in bags:
        while jewel and jewel[0][0] <= limit:
            (weigh, cost) = jewel.popleft()
            heapq.heappush(q, -cost)
        if q:
            ans -= heapq.heappop(q)
    print(ans)
    
if __name__ == "__main__":
    main()
