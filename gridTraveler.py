memo = {}

def gridTraveler(m, n):
    key = str(m) + ', ' + str(n)

    if key in memo:
        return memo[key]
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1

    memo[key] = gridTraveler(m - 1, n) + gridTraveler(m, n - 1)
    return memo[key]
    
res = gridTraveler(18, 18)
print(res)