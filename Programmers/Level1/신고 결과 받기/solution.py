def solution(id_list, report, k):
    answer = []
    fromto = {id: [] for id in id_list}
    repotcnt = {id: 0 for id in id_list}
    for re in report:
        reporter, reported = re.split()
        if reported in fromto[reporter]:
            continue
        repotcnt[reported] += 1
        fromto[reporter].append(reported)
    
    for fromm in fromto:
        cnt = 0
        for f in fromto[fromm]:
            if repotcnt[f] >= k:
                cnt += 1
        answer.append(cnt)
    
    return answer
