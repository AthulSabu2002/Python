class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = len(s)
        count = 0
        i = 0
        max_count = 0
        
        while i < k:
            count = 0
            start_index = i
            word = ''
            for x in range(start_index, k):
                if s[x] not in word:
                    word = word + s[x]
                    count = count + 1
                else:
                    break
            if max_count < count:
                max_count = count
            i = i + 1       
        return max_count

S = Solution()
n = S.lengthOfLongestSubstring('pwwkew')
print(n)