memo = {}

def howSum(target, arr):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for i in arr:
        rem = target - i
        rem_result = howSum(rem, arr)
        if rem_result is not None:
            memo[target] = rem_result + [i]
            return memo[target]

    memo[target] = None
    return None

result = howSum(7, [2, 3])

print(result)
