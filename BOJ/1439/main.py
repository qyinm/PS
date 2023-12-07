import sys
input = sys.stdin.readline().strip

def main():
    s = input()
    ans = 0
    
    zero = [v for v in s.split('1') if v]
    one = [v for v in s.split('0') if v]
    ans = min(len(zero), len(one))
    print(ans)

if __name__ == "__main__":
    main()
