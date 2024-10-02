from typing import List

class MinimumTotal:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        if m == 0:
            return 0
            
        for i in range(m - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        
        return triangle[0][0]

obj = MinimumTotal()
res = obj.minimumTotal([[-1], [2, 3], [1, -1, -3]])
print(res)
