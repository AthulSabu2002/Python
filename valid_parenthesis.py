from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
            def backtrack(S = '', left = 0, right = 0):
                if len(S) == 2 * n:
                    result.append(S)
                    return
                if left < n:
                    backtrack(S+'(', left + 1, right)
                if right < left:
                    backtrack(S+')', left, right + 1)
            
            result = []
            backtrack()
            return result
        
        
        
s = Solution()
result = s.generateParenthesis(3)
print(result)