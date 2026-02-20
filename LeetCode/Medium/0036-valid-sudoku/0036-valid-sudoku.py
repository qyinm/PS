class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidSubBlock(startPoint: Tuple[int, int], board: List[List[str]]) -> bool:
            sy, sx = startPoint
            dup_set = set()
            for y in range(sy, sy + 3):
                for x in range(sx, sx + 3):
                    value = board[y][x]
                    if value == ".":
                        continue
                    if value in dup_set:
                        return False
                    dup_set.add(value)
            
            return True

        def isValidRow(start_row: int, board: List[List[str]]) -> bool:
            sr = start_row
            dup_set = set()

            for value in board[sr]:
                if value == ".":
                    continue
                if value in dup_set:
                    return False
                dup_set.add(value)
            
            return True

        def isValidCol(start_col: int, board: List[List[str]]) -> bool:
            sc = start_col
            dup_set = set()

            for row in range(9):
                value = board[row][sc]
                if value == ".":
                    continue
                if value in dup_set:
                    return False
                dup_set.add(value)
            
            return True

        sub_block_range = [0, 3, 6]
        for i in sub_block_range:
            for j in sub_block_range:
                if isValidSubBlock((i, j), board) == False:
                    return False
        
        for row in range(9):
            if isValidRow(row, board) == False:
                return False
        
        for col in range(9):
            if isValidCol(col, board) == False:
                return False

        return True