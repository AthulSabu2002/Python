class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        pairs = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        for c in pairs:
            print(c)
        
        return len(arr) == 0

s = Solution()
result = s.isValid("(}")                
print(result)             