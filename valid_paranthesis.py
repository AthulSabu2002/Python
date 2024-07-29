class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        pairs = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        for c in s:
            if c in pairs:
                arr.append(c)
            elif len(arr) == 0 or c != pairs[arr.pop()]:
                return False
        
        return len(arr) == 0

s = Solution()
result = s.isValid("(}")                
print(result)             