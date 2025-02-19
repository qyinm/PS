def main():
    _, _ = map(int, input().split())
    a = set(list(map(int, input().split())))
    b = set(list(map(int, input().split())))

    ans = []
    for ea in a:
        if ea not in b:
            ans.append(ea)
    
    ans.sort()
    print(len(ans))
    if len(ans) > 0:
        print(*ans)

if __name__ == "__main__":
    main()