import sys
input = sys.stdin.readline

def main():
    chey = [True] * 1000001
    for i in range(2, 1001):
        if not chey[i]:
            continue
        for j in range(i+i, 1000001, i):
            chey[j] = False
    
    while True:
        num = int(input())
        if num == 0:
            break
        flag = True
        for i in range(2, num//2+1):
            if not chey[i]:
                continue
            if not chey[num-i]:
                continue
            print(f'{num} = {i} + {num-i}')
            flag = False
            break
        if flag:
            print("Goldbach's conjecture is wrong.")
if __name__ == "__main__":
    main()
