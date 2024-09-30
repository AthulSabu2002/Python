def canSum(target, arr, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for i in arr:
        rem = target - i
        if canSum(rem, arr, memo) == True:
            memo[target] = True
            return True

    memo[target] = False
    return False

print(canSum(7, [2, 3]))
