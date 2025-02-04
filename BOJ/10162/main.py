import sys
input = sys.stdin.readline

def check_invalid(n) -> None:
    if n % 10 != 0:
        print(-1)
        exit(0)

micro = [300, 60, 10]

n = int(input())
check_invalid(n)

for time in micro:
    print(n // time, end=" ")
    n %= time
