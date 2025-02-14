import sys
input = sys.stdin.readline

def perm(curr, n, visited, array, ans):
    if len(ans) == 6:
        print(*ans)
        return
    
    for idx in range(curr + 1, n):
        if visited[idx]:    continue

        visited[idx] = True
        ans.append(array[idx])

        perm(idx, n, visited, array, ans)

        ans.pop()
        visited[idx] = False

def logic(n, array):
    visited = [False] * n
    ans = []
    perm(-1, n, visited, array, ans)

def main():
    while True:
        data = list(map(int, input().split()))
        if data[0] == 0:
            break
        logic(data[0], data[1:])
        print()

if __name__ == "__main__":
    main()