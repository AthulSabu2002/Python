memo = {
        1: 1,
        2: 1
    }

def fib(num):
    if num in memo:
        return memo[num]
    else:
        memo[num] = fib(num - 1) + fib(num - 2)
        return memo[num]

n = fib(50)
print(n)
