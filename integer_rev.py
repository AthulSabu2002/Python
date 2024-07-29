class Solution:
    def reverse(self, x: int) -> int:
        num = x
        
        if num < 0:
            num = num * -1
        
        rev = 0
        
        while num > 0:
            rem = num % 10
            rev = rev * 10 + rem
            num = num // 10
        
        if x < 0:
            rev = rev * -1
            
        if rev > 2**31 or rev < -(2**31):
            return 0
        
        return rev

s = Solution()
n = s.reverse(1563847412)
print(n)   