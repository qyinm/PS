def main():
    money = int(input())
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        money -= a*b
    if money == 0:
        print("Yes")
    else:
        print("No")
    
if __name__ == "__main__":
    main()
