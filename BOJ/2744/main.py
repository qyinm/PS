s = input()
for ss in s:
    if ss < 'a':
        print(ss.lower(), end='')
    else:
        print(ss.upper(), end='')
        