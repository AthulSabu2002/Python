# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]

from typing import List


class PascalsTriangle:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for x in range(numRows):
            dummy_row = [0] + res[-1] + [0]
            row = []
            
            for i in range(len(res[-1]) + 1):
                row.append(dummy_row[i] + dummy_row[i+1])
                
            res.append(row)
        
        return res[numRows]
    
    
    
obj = PascalsTriangle()
res = obj.generate(4)

print(res)