n = int(input())
for _ in range(n):
    money = int(input())
    l = [25, 10, 5, 1]
    for ch in l:
        print(money // ch, end=" ")
        money %= ch
    print("")