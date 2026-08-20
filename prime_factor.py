def prime_factors(n):
    factors = []

    # Check for factor 2
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2

    # Check odd factors
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
        i += 2

    # If remaining n is a prime number greater than 2
    if n > 2:
        factors.append(n)

    return factors


n = int(input("Enter a number: "))
result = prime_factors(n)

print(*result)