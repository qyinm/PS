def hanoi(n, start, to, via):
    if n == 1:
        print(start, to)
    else:
        hanoi(n-1, start, via, to)
        print(start, to)
        hanoi(n-1, via, to, start)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3, 2)