def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def palindromic_substrings_score(s):
    score = 0
    palindromes = set()
    
    for i in range(len(s)):

        even_palindrome = expand_around_center(s, i, i + 1)
        if even_palindrome:
            palindromes.add(even_palindrome)
        
        odd_palindrome = expand_around_center(s, i, i)
        if odd_palindrome:
            palindromes.add(odd_palindrome)

    for palindrome in palindromes:
        l = len(palindrome)
        if l == 5:
            score += 10
        elif l == 4:
            score += 5
            
    return score


result = palindromic_substrings_score()
print(result)
