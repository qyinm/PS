import sys
sys.setrecursionlimit(987654321)

def dfs(ans, data, visited):
    a, b, c = data[0][1], data[1][1], data[2][1]
    if visited[a][b][c]:
        return
    visited[a][b][c] = True
    if a == 0 and c not in ans:
        ans.add(c)
    
    for i in range(3):
        for j in range(3):
            if data[i][1] == 0:
                continue
            if i == j:
                continue
            if data[j][0] == data[j][1]:
                continue
            prev_i = data[i][1]
            prev_j = data[j][1]
            dist = min(data[i][1], data[j][0] - data[j][1])
            data[i][1] -= dist
            data[j][1] += dist
            dfs(ans, data, visited)
            data[i][1] = prev_i
            data[j][1] = prev_j

def main():
    in_data = list(map(int, input().split()))
    data = []
    for i in in_data:
        data.append([i, 0])
    data[-1][1] = data[-1][0]
    visited = [[[False] * (in_data[2] + 1) for _ in range(in_data[1] + 1)] for _ in range(in_data[0] + 1)]
    ans = set()
    dfs(ans, data, visited)
    ans = list(ans)
    ans.sort()

    print(*ans)

if __name__ == "__main__":
    main()