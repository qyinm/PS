def main():
    n = int(input())
    arr = list(map(int, input().split()))
    dp_asc = [1] * n
    dp_desc = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp_asc[i] = max(dp_asc[i], dp_asc[j] + 1)
    
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                dp_desc[i] = max(dp_desc[i], dp_desc[j] + 1)
    ans = max([dp_asc[i] + dp_desc[i] - 1 for i in range(n)])

    print(ans)  

if __name__ == "__main__":
    main()