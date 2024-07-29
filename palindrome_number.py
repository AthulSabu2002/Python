class Solution:
    def isPalindrome(self, x: int) -> bool:
      
        k = len(str(x)) - 1
        c = str(x)
        left = 0
        right = k
      
        while left < right:
            if c[left] != c[right]:
                return False
            left = left + 1
            right = right - 1
        return True

        
        
        
s = Solution()
res = s.isPalindrome(0)
print(res)