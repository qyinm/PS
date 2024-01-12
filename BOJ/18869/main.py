import sys
input = sys.stdin.readline

def bs(low, high, target, arr):
    while low+1 < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid
        else:
            high = mid
    return low

def main():
    m, n = map(int, input().split())

    univ = [[*map(int, input().split())] for _ in range(m)]
    cop_univ = [sorted(univ[i][:])for i in range(m)]
    index = [[] for _ in range(m)]
    for idx, uni in enumerate(univ):
        for u in uni:
            loc = bs(-1, n, u, cop_univ[idx])
            index[idx].append(loc)
    
    chk = [False] * m
    cnt = 0
    for i in range(m-1):
        for j in range(i+1, m):
            flag = True
            for p in range(n):
                if index[i][p] != index[j][p]:
                    flag = False
                    break
            if flag:
                cnt += 1
    print(cnt)
if __name__ == "__main__":
    main()
