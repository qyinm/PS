len, M = map(int, input().split())

deck = list(map(int, input().split()))
jack = 0
blackJack = 0
distance = 500000
for i in range(len-2):
    for j in range(i+1, len-1):
        for k in range(j+1, len):
            jack = deck[i] + deck[j] + deck[k]
            if jack <= M and distance > abs(M-jack):
                blackJack = jack
                distance = abs(M-jack)
print(blackJack)