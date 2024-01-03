def main():
    data = [*input()]
    sw = 1
    temp = ''
    ans = 0
    for d in data:
        if d == '-' or d == '+':
            ans += sw * int(temp)
            temp = ''
        else: 
            temp += d
        if d == '-' and sw == 1:
            sw *= -1
    if temp != '':
        ans += sw * int(temp)
    print(ans)

if __name__ == "__main__":
    main()
