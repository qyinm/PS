import sys

N = int(input())
stack = []

def push(n):
    stack.append(n)

def top():
    if empty():
        return -1
    else:
        return stack[-1]

def empty():
    return size() == 0

def ppop():
    if empty():
        return -1
    else:
        return stack.pop()
def rempty():
    if size():
        return 0
    else:
        return 1

def size():
    return len(stack)


for _ in range(N):
    In = sys.stdin.readline().split()
    
    if In[0] == 'push':
        push(In[1])
    elif In[0] == 'top':
        print(top())
    elif In[0] == 'pop':
        print(ppop())
    elif In[0] == 'size':
        print(size())
    elif In[0] == 'empty':
        print(rempty())


'''
import sys
N = int(input())
stack = []
for _ in range(N):
    In = sys.stdin.readline().split()
    
    if In[0] == 'push':
        stack.append(int(In[1]))
    elif In[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif In[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif In[0] == 'size':
        print(len(stack))
    elif In[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
'''