import sys
input = lambda: sys.stdin.readline()

n, m, k = 0, 0, 0
energy = []
field = []
tree = []

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [0, 1, -1, 1, -1, 1 ,-1 ,0]

def spring_and_summer():
	global n, tree, field
	for i in range(n):
		for j in range(n):
			if tree[i][j] == []:
				continue
			tree[i][j].sort()
			for t in range(len(tree[i][j])):
				if tree[i][j][t] <= field[i][j]:
					field[i][j] -= tree[i][j][t]
					tree[i][j][t] += 1
				else:
					# 사실상여름
					for die_tree in tree[i][j][t:]:
						field[i][j] += die_tree // 2
					tree[i][j] = tree[i][j][:t]
					break

def fall():
	global n, tree, dx, dy
	for i in range(n):
		for j in range(n):
			if tree[i][j] == []:
				continue
			for t in tree[i][j]:
				if t % 5 != 0:
					continue
				for k in range(8):
					nr = i + dy[k]
					nc = j + dx[k]
					if nr < 0 or nr >= n or nc < 0 or nc >= n:
						continue
					tree[nr][nc].append(1)

def winter():
	for i in range(n):
		for j in range(n):
			field[i][j] += energy[i][j]

def init_data():
	global n, m, k, energy, field, tree

	n, m, k = map(int, input().split())
	energy = [[*map(int, input().split())] for _ in range(n)]
	field = [[5 for _ in range(n)] for _ in range(n)]
	tree = [[[] for _ in range(n)] for _ in range(n)]

	for _ in range(m):
		row, col, val = map(int, input().split())
		tree[row-1][col-1].append(val)

def main():
	global k
	init_data()
	for _ in range(k):
		spring_and_summer()
		fall()
		winter()
	ans = 0
	for tre in tree:
		for tr in tre:
			ans += len(tr)
	print(ans)

main()
