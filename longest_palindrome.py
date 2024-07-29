class Solution:
    def longestPalindrome(self, s: str) -> str:
        k = len(s)
        count = 0
        for i in range(0, k+1):
            for j in range(i+1, k+1):
                word = s[i:j]
                if word == word[::-1]:
                    if count < len(word):
                        count = len(word)
                        fin_word = word
                            
        return fin_word
    
s = Solution()
n = s.longestPalindrome('babaaabbaaa')
print(n)