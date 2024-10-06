def process_string(s):
    result = []
    for char in s:
        if char != '#':
            result.append(char)
        elif result:
            result.pop()
    
    res = ''.join(result)
    print(res)
    return res 

def compare_strings(s1, s2):
    return process_string(s1) == process_string(s2)


print(compare_strings("abc###", "##"))  # True
print(compare_strings("ab##", "c#d#"))  # True
print(compare_strings("a##c", "#a#c"))  # True
print(compare_strings("a#c", "b"))