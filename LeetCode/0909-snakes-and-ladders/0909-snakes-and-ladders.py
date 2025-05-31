import collections
from typing import List

class Solution:

    def bfs(self, vector_board: List[int], total_cells: int) -> int:

        q = collections.deque()
        q.append((0, 0))


        visited = set()
        visited.add(0) 

        while q:
            curr_idx, steps = q.popleft()


            if curr_idx == total_cells - 1:
                return steps

            for dice_roll in range(1, 7):
                next_potential_idx = curr_idx + dice_roll

                if next_potential_idx >= total_cells:
                    continue
                board_val = vector_board[next_potential_idx]

                actual_destination_idx = next_potential_idx
                if board_val != -1:
                    actual_destination_idx = board_val - 1

                if actual_destination_idx not in visited:
                    visited.add(actual_destination_idx)
                    q.append((actual_destination_idx, steps + 1))
        
        return -1

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        total_cells = n * n

        vector_board = [0] * total_cells
        cell_num = 1 

        for r_idx in range(n - 1, -1, -1):
            if (n - 1 - r_idx) % 2 == 0:
                for c_idx in range(n):
                    vector_board[cell_num - 1] = board[r_idx][c_idx]
                    cell_num += 1
            else:
                for c_idx in range(n - 1, -1, -1):
                    vector_board[cell_num - 1] = board[r_idx][c_idx]
                    cell_num += 1
        
        return self.bfs(vector_board, total_cells)