def countOfCharacters(str1):
    count = {} 
    
    for x in str1:
        if x not in count:
            count[x] = 1
        else:
            count[x] = count[x] + 1
            
    
    
    return count


res = countOfCharacters("abccdefgg")

print(res)