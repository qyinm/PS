import sys, heapq

input = sys.stdin.readline

def main():
    n = int(input())
    problem = []
    for _ in range(n):
        data = [*map(int, input().split())]
        heapq.heappush(problem, data)
    problem.sort()
    lamen = []
    init = problem[0][0]
    
    while problem:
        if problem[0][0] > init:
            init = problem[0][0]
        if len(lamen) < init:
            heapq.heappush(lamen, heapq.heappop(problem)[1])
        else:
            heapq.heappushpop(lamen, heapq.heappop(problem)[1])
    print(sum(lamen))
  
if __name__ == "__main__":
    main()
