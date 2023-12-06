import heapq
import sys
input = sys.stdin.readline

def solution(n, heap):
    ans = 0
    
    if n < 2:
        return 0
    
    while len(heap) >= 2:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        ans += a + b
        heapq.heappush(heap, a + b)
    
    return ans

def main():
    n = int(input())
    heap = []
    for _ in range(n):
        num = int(input())
        heapq.heappush(heap, num)
    
    ans = solution(n, heap)
    print(ans)
    
if __name__ == "__main__":
    main()