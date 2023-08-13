# boj 1918
str = list(input())

bot_prior = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1, ')': 0}
top_prior = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1, ')': 0}
fix_stack = []

def fix_print(s):
    if s != '(':
        print(s, end="")

for s in str:
    if s not in bot_prior.keys():
        fix_print(s)
    else:
        if len(fix_stack) == 0:
            fix_stack.append(s)
        elif s == ')':
            while fix_stack[-1] != '(':
                fix_print(fix_stack.pop())
            if len(fix_stack) != 0:
                fix_stack.pop()
        else:
            while len(fix_stack) != 0 and bot_prior[fix_stack[-1]] >= top_prior[s]:
                fix_print(fix_stack.pop())
            fix_stack.append(s)
for s in fix_stack[::-1]:
    fix_print(s)