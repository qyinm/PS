from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        domino_value = [0] * n
        q = deque([])
        for i, domino in enumerate(dominoes):
            if domino == '.':
                continue
            if domino == 'R':
                domino_value[i] = 1
            elif domino == 'L':
                domino_value[i] = -1
            q.append((i, domino_value[i]))
        
        while q:
            length = len(q)
            temp_q = deque([])
            for _ in range(length):
                idx, value = q.popleft()

                next_idx = idx + value
                if next_idx < 0 or next_idx >= n:
                    continue
                if domino_value[next_idx] != 0:
                    continue
                
                temp_q.append((next_idx, value))
            
            for ni, v in temp_q:
                domino_value[ni] += v
            while temp_q:
                curr, val = temp_q.popleft()
                if domino_value[curr] != 0:
                    q.append((curr, val))
        ans = []
        for val in domino_value:
            v = None
            if val == 0:
                v = '.'
            elif val == 1:
                v = 'R'
            else:
                v = 'L'
            ans.append(v)
        return ''.join(ans)
              
