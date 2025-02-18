def getPi(P):
    pi = [0] * len(P)
    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = pi[j-1]
        if P[i] == P[j]:
            j += 1
            pi[i] = j
    return pi        

def KMP(find_n, input_n):
    P = 'I' + 'OI'*find_n
    input_data = list(input())
    pi = getPi(P)
    ans = 0
    j = 0
    for i in range(input_n):
        while j > 0 and input_data[i] != P[j]:
            j = pi[j - 1]
        if input_data[i] == P[j]:
            if j == len(P) - 1:
                ans += 1
                j = pi[j]
            else:
                j += 1
    print(ans)

def main():
    find_n = int(input())
    input_n = int(input())
    KMP(find_n, input_n)

if __name__ == "__main__":
    main()