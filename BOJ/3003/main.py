from sys import stdin
input = stdin.readline

def main():
    chess = [1, 1, 2, 2, 2, 8]
    pieces = list(map(int, input().split()))
    for i in range(6):
        print(chess[i] - pieces[i], end=' ')

if __name__ == "__main__":
    main()