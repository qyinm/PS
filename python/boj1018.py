A = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
B = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']

def check(board, standard):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] != standard[i][j]:
                cnt += 1
    return cnt

n, m = map(int, input().split())
chess = []

for _ in range(n):
    block = input()
    chess.append(block)
a = 0
b = 0
data=[]
tc = []
for i in range(n - 7):
    for j in range(m - 7):
        tc = [t1[j:j+8] for t1 in chess[i:i+8]]
        a = check(tc, A)
        b = check(tc, B)
        M = min(a, b)
        data.append(M)
print(min(data))
