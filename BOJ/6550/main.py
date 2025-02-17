from collections import deque

try:
    while True:
        a, b= input().split()
        b = deque(list(b))

        answer = 'Yes'
        idx = 0
        while idx < len(a):
            if len(b) == 0:
                answer = 'No'
                break
            while len(b) > 0 and a[idx] != b[0]:
                b.popleft()
            if len(b) > 0 and b[0] == a[idx]:
                b.popleft()
                idx += 1
        print(answer)
        
except Exception as e:
    pass