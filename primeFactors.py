def prime_factors(n):
    factors = set()
    
    d = 2
    while n > 1:
        while n % d == 0:
            factors.add(d)
            n = n // d
        
        d = d + 1
        if d * d > n:
            if n > 1:
                factors.add(n)
            break
    
    return list(factors)
        

number = 3000
print(f"The prime factors of {number} are: {prime_factors(number)}")