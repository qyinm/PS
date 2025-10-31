from sys import stdin
input = stdin.readline

# slump: (D | E)F+(slump | G)
# -> slum: (D | E)F+
# -> new_slump: slum+G
# slimp: A(H | B?new_slumpC)

def is_slump(s):
    if len(s) < 3 or s[0] not in ('D', 'E'):
        return False

    index = 1
    while index < len(s) and s[index] == 'F':
        index += 1

    if index == len(s):
        return False

    return s[index] == 'G' and index == len(s) - 1 or is_slump(s[index:])

def is_slimp(s):
    if len(s) < 2 or s[0] != 'A':
        return False

    if len(s) == 2:
        return s[1] == 'H'

    if s[-1] != 'C':
        return False

    return is_slimp(s[2:-1]) if s[1] == 'B' else is_slump(s[1:-1])

def is_slurpy(s):
    for index in range(2, len(s)):
        if is_slimp(s[:index]) and is_slump(s[index:]):
            return True
    return False

def main():
    n = int(input().strip())
    for _ in range(n):
        s = input().strip()
        print('YES' if is_slurpy(s) else 'NO')

if __name__ == "__main__":
    main()