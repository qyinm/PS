def solution(diffs, times, limit):
    answer = 0
    n = len(diffs)
    max_level = max(diffs)
    left, right = 1, max_level
    
    while left <= right:
        time = 0
        prev_time = 0
        level = (left + right) // 2
        for idx in range(n):
            time += times[idx] + max(0, diffs[idx] - level) * (prev_time + times[idx])
            prev_time = times[idx]
        if time <= limit:
            right = level - 1
            answer = level
        else:
            left = level + 1
            
    return answer