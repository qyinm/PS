from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        domino_value = [0] * n
        digit2str = {0: '.', 1: 'R', -1: 'L'}
        str2digit = {'.': 0, 'R': 1, 'L': -1}
        q = deque([])

        for i, domino in enumerate(dominoes):
            if domino == '.':
                continue

            domino_value[i] = str2digit[domino]
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

        return ''.join(digit2str[val] for val in domino_value)
              
