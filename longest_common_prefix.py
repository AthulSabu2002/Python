from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        ans = ""
        first = strs[0]
        last = strs[-1]
        
        for i in range(min(len(first), len(last))):
            if first[i]!=last[i]:
                return ans
            ans = ans + first[i]
        
s = Solution()
c = s.longestCommonPrefix(["dog","racecar","car"])
print(c)