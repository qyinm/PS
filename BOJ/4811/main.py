import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def main(n):
    cache = [[-1] * (n + 1) for _ in range(n + 1)]

    def solve(one_capsule, half_capsule):
        if one_capsule < 0 or half_capsule < 0:
            return 0
        if one_capsule == 0 and half_capsule == 0:
            return 1
        if cache[one_capsule][half_capsule] != -1:
            return cache[one_capsule][half_capsule]

        cache[one_capsule][half_capsule] = 0
        cache[one_capsule][half_capsule] = solve(
            one_capsule - 1, half_capsule + 1
        ) + solve(one_capsule, half_capsule - 1)

        return cache[one_capsule][half_capsule]

    print(solve(n, 0))


if __name__ == "__main__":
    while (n := int(input())) != 0:
        main(n)
