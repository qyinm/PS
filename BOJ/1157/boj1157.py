import sys

string = input()
string = string.upper()

dictt = {}

if len(string) == 1:
    print(string)
    exit(0)

for s in string:
    if s in dictt.keys():
        dictt[s] += 1
    else:
        dictt[s] = 0

dictt = sorted(dictt.items(), key=lambda x: x[1], reverse=True)

if dictt[0][1] == dictt[1][1]:
    print("?")
else:
    print(dictt[0][0])

