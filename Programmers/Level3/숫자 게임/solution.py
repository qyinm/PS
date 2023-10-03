def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    bIdx = 0
    for i in range(len(A)):
        while bIdx < len(B) and B[bIdx] <= A[i]:
            bIdx += 1
        if bIdx >= len(B):  break
        answer += 1
        bIdx += 1
        
    return answer
