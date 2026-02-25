import sys
input = sys.stdin.readline

def ant_path_finding(ant_house, ants_count):
    if ants_count >= len(ant_house):
        return 0
    
    ant_house_xs = sorted(ant_house.values())
    n = len(ant_house_xs)
    
    def check(T):
        used = 0
        i = 0
        while i < n and used < ants_count:
            used += 1
            j = i
            while j + 1 < n and ant_house_xs[j + 1] - ant_house_xs[i] <= T:
                j += 1
            i = j + 1
        return i == n
    
    lo, hi = 0, ant_house_xs[-1] - ant_house_xs[0]
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid
    return hi

def main():
    q = int(input())
    ant_house = dict()
    next_id = 1
    answer = 0
    for _ in range(q):
        comm, k, *xs = map(int, input().split())
        
        match comm:
            case 100:
                for idx, x in enumerate(xs):
                    ant_house[idx + 1] = x
                next_id = len(xs) + 1
            case 200:
                ant_house[next_id] = k
                next_id += 1
            case 300:
                ant_house.pop(k)
            case 400:
                answer = ant_path_finding(ant_house, k)
                print(answer)

if __name__ == "__main__":
    main()
