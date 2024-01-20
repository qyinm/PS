import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

width = 0
n = 0
notes = []
cache = []

def dp(note, curWidth):
    if curWidth > width:
        return float('inf')
    if note == n-1:
        return 0
    if cache[note][curWidth] != -1:
        return cache[note][curWidth]
    rest = (width - curWidth)

    nxtCol = dp(note+1, curWidth+notes[note+1]+1)
    nxtRow = rest**2 + dp(note+1, notes[note+1])
    cache[note][curWidth] = min(nxtRow, nxtCol)
    
    return cache[note][curWidth]

def main():
    global n, width, notes, cache
    n, width = map(int, input().split())
    cache = [[-1] * (width+1) for _ in range(n)]
    for _ in range(n):
        notes.append(int(input()))
    ans = dp(0, notes[0])
    print(ans)
    
if __name__ == "__main__":
    main()
