def solution(N, stages):
    answer = []
    stage_players = [0 for _ in range(N+1)]
    
    all = len(stages)
    
    for stage in stages:
        if stage <= N:
            stage_players[stage] += 1
    stage_list = []
    
    for i in range(1, N+1):
        if (all == 0) :
            all = 1
        
        stage = [-stage_players[i]/all, i]
        stage_list.append(stage)
        all -= stage_players[i]
        

    stage_list.sort()
    answer = [i[1] for i in stage_list]
    
    return answer
