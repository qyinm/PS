from sys import stdin
import math
input = stdin.readline

def main():
    p3, p4, p0 = map(int, input().split())
    answer = None
    for t4 in range((p0 + p4) // 4, -1, -1):
        need_p4 = t4 * 4
        if p4 > need_p4:
            continue
        left_p0 = p0 - (need_p4 - p4)
        if left_p0 < 0:
            continue
        total_p3 = left_p0 + p3
        if total_p3 % 3 != 0:
            continue
        answer = (total_p3 // 3, t4)
        break
    if answer is None:
        print(-1)
    else:
        print(answer[0], answer[1])
    
if __name__ == "__main__":
    main()