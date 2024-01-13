import sys
input = sys.stdin.readline

ans = [0, 0, 0]

dr = [0, 1, 2, 0, 1, 2, 0, 1, 2]
dc = [0, 0, 0, 1, 1, 1, 2, 2, 2]

paper = []
def recur(row, col, n):
	if n == 1:
		return paper[row][col]
	temp = []
	nxt = n // 3
	for i in range(9):
		nr, nc = row+dr[i]*nxt, col+dc[i]*nxt
		temp.append(recur(nr, nc, nxt))
	is_same = all(t == temp[0] and t != 3 for t in temp)

	if is_same:
		return temp[0]

	for t in temp:
		if t < 3:
		    ans[t+1] += 1
	return 3


def main():
	global paper

	n = int(input())

	paper = [[*map(int, input().split())] for _ in range(n)]
	k = recur(0, 0, n)
	if k < 3:
		ans[k+1] += 1
	for a in ans:
		print(a)

if __name__ == "__main__":
	main()
