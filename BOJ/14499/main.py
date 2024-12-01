import sys

input = sys.stdin.readline

class Dice:
    def __init__(self):
        self.up = self.down = self.front = self.back = self.right = self.left = 0

    def command(self, command):
        if command == 1:
            self.turn_left()
        elif command == 2:
            self.turn_right()
        elif command == 3:
            self.turn_up()
        elif command == 4:
            self.turn_down()

    def turn_left(self):
        tmp = self.up
        self.up = self.right
        self.right = self.down
        self.down = self.left
        self.left = tmp
    
    def turn_right(self):
        tmp = self.up
        self.up = self.left
        self.left = self.down
        self.down = self.right
        self.right = tmp
    
    def turn_down(self):
        tmp = self.up
        self.up = self.back
        self.back = self.down
        self.down = self.front
        self.front = tmp

    def turn_up(self):
        tmp = self.up
        self.up = self.front
        self.front = self.down
        self.down = self.back
        self.back = tmp
    
    def update_down(self, new_down):
        self.down = new_down
    
    def get_up(self):
        return self.up

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

game_map = []
dice = Dice()
n, m, r, c, k = map(int, input().split())

for _ in range(n):
    row = list(map(int, input().split()))
    game_map.append(row)

commands = list(map(int, input().split()))

for command in commands:
    
    nr, nc = r + dr[command], c + dc[command]
    if (0 > nr or nr >= n or 0 > nc or nc >= m):
        continue
    
    dice.command(command)
    r, c = nr, nc

    if game_map[r][c] == 0:
        game_map[r][c] = dice.down
    else:
        dice.update_down(game_map[r][c])
        game_map[r][c] = 0    

    print(dice.get_up())
    