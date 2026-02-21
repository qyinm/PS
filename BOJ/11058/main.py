import sys

input = sys.stdin.readline


def main():
    n = int(input())

    cache = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i <= 3:
            cache[i] = cache[i-1] + 1
            continue
        
        cache[i] = max(
            cache[i-1] + 1,
            max(cache[j] * (i-j-1) for j in range(i-2))
        )

    print(cache[n])

if __name__ == "__main__":
    main()
