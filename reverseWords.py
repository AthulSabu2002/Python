def reverse(str1):
    str2 = ""
    l = len(str1) - 1
    
    for i in range(l, -1, -1):
        str2 = str2 + str1[i]
        
    return str2

res = reverse("I am Athul")
print(res)