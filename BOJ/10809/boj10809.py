alpha = "abcdefghijklmnopqrstuvwxyz"
dictt = {}

string = input()
for i in range(len(string)):
    if string[i] not in dictt.keys():
        dictt[string[i]] = i

for a in alpha:
    if a in dictt.keys():
        print(dictt[a], end=" ")
    else:
        print(-1, end=" ")