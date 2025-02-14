from collections import Counter

s = input().strip()
count = Counter(s)

odd_chars = [ch for ch, cnt in count.items() if cnt % 2 == 1]
if len(odd_chars) > 1:
    print("I'm Sorry Hansoo")
    exit(0)

left_half = []
mid_char = ''

for ch in sorted(count.keys()):
    cnt = count[ch]
    if cnt % 2 == 1:
        mid_char = ch
    left_half.append(ch * (cnt // 2))

left_half = ''.join(left_half)
right_half = left_half[::-1]
palindrome = left_half + mid_char + right_half
print(palindrome)