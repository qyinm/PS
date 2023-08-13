n = int(input())

for x in range(n):
    x, y = map(int,input().split())
    d= y-x
    s=d
    s**=0.5
    s=int(s)
    s=s**2+s
    if d<=2:
        print(1)
    elif d**0.5 == int(d**0.5):
        s=d**0.5
        s=int(s)
        s=2*s-1
        print(s) 
    elif d<=s:
        s=d**0.5
        s=int(s)
        s=2*s
        print(s)
    else:
        s=d**0.5
        s=int(s)+1
        s=2*s-1
        print(s)
        
