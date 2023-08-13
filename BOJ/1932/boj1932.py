n = int(input())

dpArray = []
valueArray = []
for i in range(n):
    dpArray.append(list(map(int, input().split())))
    valueArray.append([0 for j in range(i+1)])



def dp(array, varray, idx1, idx2):

    if idx1 == n-1:
        return array[idx1][idx2]
    
    if varray[idx1][idx2] != 0:
        return array[idx1][idx2]
    array[idx1][idx2] += max(dp(array, varray, idx1+1, idx2), dp(array, varray, idx1+1, idx2+1))
    varray[idx1][idx2] = 1
    return array[idx1][idx2]
    
ans = dp(dpArray, valueArray, 0, 0)
print(ans)

'''
다른 사람 풀이
n = int(input())
dpArray = [list(map(int, input().split())) for i in range(n)]

for x in range(1, n):
    for y in range(x+1):
        if y == 0:
            dpArray[x][y] = dpArray[x-1][0]
        elif x == y:
            dpArray[x][y] = dpArray[x-1][-1]
        else:
            dpArray[x][y] = max(dpArray[x-1][y-1], dpArray[x-1][y])

print(max(dpArray[-1]))
'''