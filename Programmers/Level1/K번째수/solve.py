def solution(array, commands):
    answer = []
    
    for command in commands:
        tempA = array[command[0]-1:command[1]]
        tempA.sort()
        answer.append(tempA[command[2]-1])
        
    return answer