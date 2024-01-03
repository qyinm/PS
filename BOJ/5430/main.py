import sys
input = sys.stdin.readline
from collections import deque

def logic(queue, cmd):
    sw = 1
    for c in cmd:
        match c:
            case 'R':
                sw *= -1
            case 'D':
                if sw == 1:
                    queue.popleft()
                else:
                    queue.pop()
    if sw == -1:
        queue.reverse()
    return '['+','.join(queue)+']'

def main():
    tc = int(input())
    for _ in range(tc):
        cmd = [*input().rstrip()]
        length = int(input())
        array = input().rstrip().replace('[', '').replace(']', '').split(',')
        array = [*array]
        if cmd.count('D') > length:
            print("error")
            continue
        queue = deque(array)
        print(logic(queue, cmd))
        
if __name__ == "__main__":
    main()
    
