import sys
input = sys.stdin.readline

n = int(input())
MOD = 1000000007
matrix = [[1, 1], [1, 0]]

def mx_sq(m, c):
    ret = [[0, 0], [0, 0]]
     
    ret[0][0] = (m[0][0] * c[0][0] + m[0][1] * c[1][0]) % MOD
    ret[0][1] = (m[0][0] * c[0][1] + m[0][1] * c[1][1]) % MOD
    ret[1][0] = (m[1][0] * c[0][0] + m[1][1] * c[1][0]) % MOD
    ret[1][1] = (m[1][0] * c[0][1] + m[1][1] * c[1][1]) % MOD
    return ret
    
def div(n, mm):
    if n == 1:
        return mm
    if n % 2 == 0:
        tmp = div(n // 2, mm)
        return mx_sq(tmp, tmp)
    else:
        return mx_sq(mm, div(n - 1, mm))
        
print(div(n, matrix)[0][1])