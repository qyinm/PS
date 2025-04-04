def main():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [0] * n
    time = 1
    while sum(arr) > 0:
        for i in range(n):
            if arr[i] == 0:
                continue
            arr[i] -= 1
            if arr[i] == 0:
                ans[i] = time
            time += 1
    print(*ans)

if __name__ == "__main__":
    main()