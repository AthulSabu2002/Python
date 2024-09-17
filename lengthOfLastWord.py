from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        lst = s.split(' ')
        lst = [x for x in lst if x != '']
        
        length = len(lst[-1])
        
        return length
        

s = Solution()
length = s.lengthOfLastWord("   fly me   to   the moon  ")
print(length)