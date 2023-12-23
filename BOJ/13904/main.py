import heapq, sys
input = sys.stdin.readline

def main():
    n = int(input())
    heap = []
    data = [[*map(int, input().split())] for _ in range(n)]
    data.sort()
    for k, v in data:
        if len(heap) < k:
            heapq.heappush(heap, v)
        elif heap[0] < v:
            heapq.heappop(heap)
            heapq.heappush(heap, v)

    ans = sum(heap)
    print(ans)

if __name__ == "__main__":
    main()
