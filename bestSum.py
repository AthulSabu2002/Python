def bestSum(target, arr):
    memo = [None] * (target + 1)
    memo[0] = []

    for t in range(1, target + 1):
        for num in arr:
            if num <= t and memo[t - num] is not None:
                combination = memo[t - num] + [num]
                if memo[t] is None or len(combination) < len(memo[t]):
                    memo[t] = combination

    return memo[target]


result = bestSum(8, [1, 4, 5])
print(result)

result = bestSum(1000, [1, 2, 250, 25])
print(result)

