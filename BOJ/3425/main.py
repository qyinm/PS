from enum import Enum
from sys import stdin
input = lambda : stdin.readline().strip()

class Command(Enum):
    NUM = "NUM"
    POP = "POP"
    INV = "INV"
    DUP = "DUP"
    SWP = "SWP"
    ADD = "ADD"
    SUB = "SUB"
    MUL = "MUL"
    DIV = "DIV"
    MOD = "MOD"

def check(stack, command):
    match command:
        case Command.POP.value | Command.INV.value | Command.DUP.value :
            return len(stack) < 1
        case Command.SWP.value | Command.ADD.value | Command.SUB.value | Command.MUL.value:
            return len(stack) < 2
        case Command.DIV.value | Command.MOD.value:
            return stack[-1] == 0 or len(stack) < 2


while True:
    commands = []
    while True:
        command = input()
        if command == 'QUIT':
            exit(0)
        if command == 'END':
            break
        commands.append(command)
    tc = int(input())
    for _ in range(tc):
        base = int(input())
        stack = [base]
        flag = False
        for command in commands:
            if len(command) > 3:
                com, n = command.split(" ")
                stack.append(int(n))
                continue
            match command:
                case Command.POP.value:
                    if check(stack, command):
                        print("ERROR")
                        flag = True
                        break
                    stack.pop()
                case Command.INV.value:
                    if check(stack, command):
                        print("ERROR")
                        flag = True
                        break
                    stack[-1] = -stack[-1]
                case Command.DUP.value:
                    if check(stack, command):
                        print("ERROR")
                        flag = True
                        break
                    stack.append(stack[-1])
                case Command.SWP.value:
                    if check(stack, command):
                        print("ERROR")
                        flag = True
                        break
                    stack[-1], stack[-2] = stack[-2], stack[-1]
                case Command.ADD.value:
                    if check(stack, command):
                        print("ERROR")
                        flag = True
                        break
                    stack.append(stack.pop() + stack.pop())
                case Command.SUB.value:
                    if check(stack, command):
                        print("ERROR")
                        flag = True
                        break
                    stack.append(-stack.pop() + stack.pop())
                case Command.MUL.value:
                    if check(stack, command):
                        print("ERROR")
                        flag = True
                        break
                    stack.append(stack.pop() * stack.pop())
                case Command.DIV.value:
                    if check(stack, command):
                        print("ERROR")
                        flag = True
                        break
                    a, b = stack.pop(), stack.pop()
                    ABSa = abs(a)
                    ABSb = abs(b)
                    div = ABSb // ABSa
                    if a * b < 0:
                        div *= -1
                    stack.append(div)
                case Command.MOD.value:
                    if check(stack, command):
                        print("ERROR")
                        flag = True
                        break
                    a, b = stack.pop(), stack.pop()
                    ABSa = abs(a)
                    ABSb = abs(b)
                    mod = (ABSb % ABSa)
                    if (b < 0):
                        mod *= -1
                    stack.append(mod)
        if not flag:
            if len(stack) != 1 or abs(stack[-1]) > 1e9:
                print("ERROR")
            else:
                print(stack[0])
    print("")
