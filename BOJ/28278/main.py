n = int(input())
st = []
for _ in range(n):
    q = list(map(int, input().split()))
    if q[0] == 1:
        st.append(q[1])
    elif q[0] == 2:
        if len(st) == 0:
            print(-1)
        else:
            print(st.pop())
    elif q[0] == 3:
        print(len(st))
    elif q[0] == 4:
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif q[0] == 5:
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])