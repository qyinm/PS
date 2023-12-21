MOD = int(1e9 + 7)

def main():
    n = int(input())
    cache = [0] * (n + 1)
    cache[0] = 1
    
    for i in range(1, n+1):
        if i == 1:
            cache[i] = 1
            continue
        cache[i] = (cache[i-1] + cache[i-2] + 1) % MOD
    print(cache[n])
    
if __name__ == "__main__":
    main()