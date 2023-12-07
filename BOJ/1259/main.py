def solution(number):
    number_s = str(number)
    if number_s == number_s[::-1]:
        return "yes"
    return "no"

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        ans = solution(n)
        print(ans)
    
if __name__ == "__main__":
    main()
