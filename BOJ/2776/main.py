import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    note1 = list(map(int, input().split()))
    note1.sort()
    
    m = int(input())
    note2 = list(map(int, input().split()))
    
    for i in range(m):
        target = note2[i]
        left = 0
        right = n-1
        
        find = 0
        while left <= right:
            mid = (left + right) // 2
            if note1[mid] == target:
                find = 1
                break
            if note1[mid] < target:
                left = mid + 1
            elif note1[mid] > target:
                right = mid - 1
        print(find)

    
