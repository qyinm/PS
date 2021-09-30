import sys
input = sys.stdin.readline

t = int(input())

data = []

for _ in range(t):
    temp = input().split()
    for i in range(len(temp)):
        tempString = temp[i][::-1]
        temp[i] = tempString
    data.append(temp)

for i in range(t):
    string = ' '.join(data[i])
    print(string)
