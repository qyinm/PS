def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key = lambda x: len(x))
    for _s in s:
        data = _s.split(",")
        for d in data:
            if int(d) not in answer:
                answer.append(int(d))
    
    
    return answer
