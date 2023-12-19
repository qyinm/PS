import sys

input = sys.stdin.readline

def main():
    a, b = input().split()
    a = sum(list(map(int, a)))
    b = sum(list(map(int, b)))
    print(a*b)
    
if __name__ == "__main__":
    main()
