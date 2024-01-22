import heapq

def main():
    x = int(input())
    pq = [64]
    while True:
        ssum = sum(pq)
        if ssum <= x:
            break
        mmin = heapq.heappop(pq)
        lo = mmin//2
        hi = mmin - lo
        if ssum - lo >= x:
            heapq.heappush(pq, hi)
        elif ssum - hi >= x:
            heapq.heappush(pq, lo)
        else:
            heapq.heappush(pq, lo)
            heapq.heappush(pq, hi)

    print(len(pq))
main()
