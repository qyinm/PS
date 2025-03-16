import sys, heapq
input = sys.stdin.readline

def logic():
    n = int(input())
    costs = list(map(int, input().split()))

    hq = []
    for i in range(n):
        heapq.heappush(hq, costs[i])
    ans = 0
    while len(hq) > 1:
        a, b = heapq.heappop(hq), heapq.heappop(hq)
        heapq.heappush(hq, a + b)
        ans += (a + b)
    print(ans)

def main():
    tc = int(input())
    
    for _ in range(tc):
        logic()

if __name__ == "__main__":
    main()