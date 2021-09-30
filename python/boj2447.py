import sys
sys.setrecursionlimit(10**6)

def solveStar(x, y, n):
    if n == 1:
        stars[x][y] = '*'
        return
    div = n // 3
    solveStar(x, y, div)
    solveStar(x+div, y, div)
    solveStar(x+div+div, y, div)
    solveStar(x, y+div, div)
    solveStar(x+div+div, y+div, div)
    solveStar(x, y+div+div, div)
    solveStar(x+div, y+div+div, div)
    solveStar(x+div+div, y+div+div, div)

n = int(input())
stars = [[" " for i in range(n)] for i in range(n)]
solveStar(0, 0, n)
for star in stars:
    print(''.join(star))