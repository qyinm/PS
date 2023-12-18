def dp(graph, n):
    minWin = [0, 0, 0]
    maxWin = [0, 0, 0]
    
    for i in range(n):
        minWin0 = graph[i][0] + min(minWin[:2])
        minWin1 = graph[i][1] + min(minWin[:])
        minWin2 = graph[i][2] + min(minWin[1:])
        maxWin0 = graph[i][0] + max(maxWin[:2])
        maxWin1 = graph[i][1] + max(maxWin[:])
        maxWin2 = graph[i][2] + max(maxWin[1:])
        minWin = [minWin0, minWin1, minWin2]
        maxWin = [maxWin0, maxWin1, maxWin2]
        
    print(max(maxWin), min(minWin))

def main():
    n = int(input())
    graph = [[*map(int, input().split())] for _ in range(n)]
    dp(graph, n)
    

if __name__ == "__main__":
    main()
