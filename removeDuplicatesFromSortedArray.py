def removeDuplicates(arr):
    if not arr:
        return 0
    
    j = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    
    return arr[:j + 1]



res = removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

print(res)
        