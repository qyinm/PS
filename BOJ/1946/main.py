import sys
input = sys.stdin.readline

def logic():
    n = int(input())
    people = []
    for _ in range(n):
        paper, interview = map(int, input().split())
        people.append((paper, interview))
    people.sort()
    #print(people)
    cnt = 0
    minn = people[0][1]
    for i in range(1, n):
        if minn < people[i][1]:
            cnt += 1
        else:   minn = people[i][1]
    
    return n - cnt

def main():
    tc = int(input())
    
    for _ in range(tc):
        print(logic())

if __name__ == "__main__":
    main()