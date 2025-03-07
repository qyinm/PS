class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangles = [[1]]
        for i in range(1, rowIndex+1):
            t = [1]
            for j in range(i-1):
                t.append(triangles[-1][j] + triangles[-1][j+1])
            t.append(1)
            triangles.append(t)
        return triangles[-1]