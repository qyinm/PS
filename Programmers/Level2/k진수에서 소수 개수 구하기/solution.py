def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    ex = []
    while n != 0:
        ex.append(str(n % k))
        n //= k
        
    numstr = ''.join(ex[::-1])
    nums = [n for n in numstr.split('0') if n]
    nums = [*map(int, nums)]
                
    for num in nums:
        if num == 1:
            continue
        if prime(num):
            answer += 1
    return answer
