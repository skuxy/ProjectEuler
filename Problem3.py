# Project Euler: Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# Erastothenes's algorithm
def prime_sieve(limit):
    isPrime = {}

    isPrime[1] = False
    for i in range(2, limit + 1):
        isPrime[i] = True

    checkLimit = int(limit ** 0.5) + 1
    for i in range(2, checkLimit):
        if isPrime[i]:
            for factor in range(2, limit + 1):
                j = i * factor
                if (j > limit): break
                isPrime[j] = False

    primes = []
    for i in range(1, limit + 1):
        if isPrime[i]:
            primes.append(i)

    return primes


# Return a list of the prime factors for a natural number.
def trial_division(n):
    if n < 2:
        return []
    prime_factors = []
    for p in prime_sieve(int(n ** 0.5) + 1):
        if p * p > n: break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1:
        prime_factors.append(n)
    return prime_factors

if __name__ == "__main__":
    print(max(trial_division(600851475143)))