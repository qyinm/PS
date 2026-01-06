from collections import deque, defaultdict

def solution(points, routes):
    answer = 0
    queue = deque()
    
    for robot_id, route in enumerate(routes):
        start_point = points[route[0]-1]
        queue.append((*start_point, robot_id, 1))

    
    while queue:
        current_step_count = len(queue)
        
        # collision detection 
        position_count = defaultdict(int)
        for robot_state in queue:
            row, col, _, _ = robot_state
            position_count[(row, col)] += 1
        
        answer += sum(1 for s in position_count.values() if s > 1)

        for _ in range(current_step_count):
            row, col, robot_id, next_goal_idx = queue.popleft()
            
            if next_goal_idx == -1:
                continue
                
            next_point_id = routes[robot_id][next_goal_idx] - 1
            next_row, next_col = points[next_point_id]

            if row != next_row:
                row += 1 if row < next_row else -1
            elif col != next_col:
                col += 1 if col < next_col else -1
            
            if row == next_row and col == next_col:
                if next_goal_idx + 1 == len(routes[robot_id]):
                    next_goal_idx = -1
                else:
                    next_goal_idx += 1
            queue.append((row, col, robot_id, next_goal_idx))
    
    return answer