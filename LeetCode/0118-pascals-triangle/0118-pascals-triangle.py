class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for numRow in range(1, numRows):
            t = [1]
            for i in range(numRow-1):
                t.append(triangle[-1][i] + triangle[-1][i+1])
            t.append(1)
            triangle.append(t)
        return triangle