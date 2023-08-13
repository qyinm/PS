n = int(input())

dataSet = []
scoreSet = []

for i in range(n):
    data = list(map(int, input().split()))
    dataSet.append(data)

for i in range(n):
    score = 0
    for j in range(n):
        if i != j and dataSet[i][0] < dataSet[j][0] and dataSet[i][1] < dataSet[j][1]:
            score += 1
    score+=1
    scoreSet.append(score)
print(" ".join(map(str, scoreSet)))