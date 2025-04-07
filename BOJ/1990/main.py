import sys
input = sys.stdin.readline

limit = 10_000_000

def main():
    f, t = map(int, input().split())
    chey = [False] * (limit + 1)

    for i in range(2, int(limit ** 0.5 + 1)):
        if chey[i] == True:
            continue
        chey[i] = False
        for j in range(i + i, limit + 1, i):
            chey[j] = True

    for number in range(f, t + 1):
        if number > limit:
            break
        str_number = str(number)

        if str_number == str_number[::-1]:
            if not chey[number]:
                print(number)
    print(-1)

if __name__ == "__main__":
    main()