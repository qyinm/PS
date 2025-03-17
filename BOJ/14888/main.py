from itertools import permutations

def main():
    input()
    nums = list(map(int, input().split()))
    operators_count = list(map(int, input().split()))
    operators = ['+', '-', '*', '/']
    in_operators = []
    maxx = -1e10
    minn = 1e10

    for i in range(4):
        for _ in range(operators_count[i]):
            in_operators.append(operators[i])
    
    len_operators = len(in_operators)
    combs = permutations(in_operators, len_operators)
    for comb in combs:
        
        result = nums[0]
        for i in range(len_operators):
            if comb[i] == '+':
                result += nums[i+1]
            elif comb[i] == '-':
                result -= nums[i+1]
            elif comb[i] == '*':
                result *= nums[i+1]
            else:
                if result < 0:
                    result = -(abs(result) // nums[i+1])
                else:
                    result = result // nums[i+1]
        maxx = max(maxx, result)
        minn = min(minn, result)

    print(maxx)
    print(minn)

if __name__ == "__main__":
    main()