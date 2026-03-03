def main():
    n, k = map(int, input().split())

    movingwalks = list(map(int, input().split()))
    up_walk = movingwalks[:n]
    down_walk = movingwalks[n:]
    down_walk.reverse()
    peoples = [False] * n
    time = 0
    while down_walk.count(0) + up_walk.count(0) < k:
        # 회전
        tmp = up_walk[-1]
        for i in range(n - 1, 0, -1):
            up_walk[i] = up_walk[i - 1]
        up_walk[0] = down_walk[0]
        for i in range(n - 1):
            down_walk[i] = down_walk[i + 1]
        down_walk[-1] = tmp
        for i in range(n - 1, 0, -1):
            peoples[i] = peoples[i - 1]
        peoples[0] = False
        peoples[n - 1] = False

        # 사람 이동
        for i in range(n - 2, -1, -1):
            if peoples[i] and up_walk[i + 1] != 0 and not peoples[i + 1]:
                peoples[i] = False
                peoples[i + 1] = True
                up_walk[i + 1] -= 1
        if peoples[n - 1]:
            peoples[n - 1] = False
        
        # 사람 추가
        if not peoples[0] and up_walk[0] != 0:
            peoples[0] = True
            up_walk[0] -= 1

        time += 1
    print(time)
if __name__ == "__main__":
    main()
