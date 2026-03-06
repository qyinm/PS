import sys
input = sys.stdin.readline

from itertools import combinations
from collections import deque

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    peoples = [(r, c) for r in range(n) for c in range(n) if board[r][c] == 1]
    hospitals = [(r, c) for r in range(n) for c in range(n) if board[r][c] == 2]
    hospital_count = len(hospitals)
    people_count = len(peoples)

    dist = [[0] * hospital_count for _ in range(people_count)]
    for i in range(people_count):
        for j in range(hospital_count):
            dist[i][j] = abs(peoples[i][0] - hospitals[j][0]) + abs(peoples[i][1] - hospitals[j][1])

    minn = 1e9
    
    combs = list(combinations(list(range(hospital_count)), hospital_count - m))

    for comb in combs:
        cannot_hospitals = set(comb)
        summ = 0
        for i in range(people_count):
            min_dist = 1e9
            for j in range(hospital_count):
                if j not in cannot_hospitals:
                    min_dist = min(min_dist, dist[i][j])
            summ += min_dist
        minn = min(minn, summ)
    print(minn)
if __name__ == "__main__":
    main()
