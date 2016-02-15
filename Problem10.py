# Project Euler: Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# using algorithm from Problem 3
from Problem3 import is_prime, list_of_primes

if __name__ == "__main__":
    print(sum(list_of_primes(2000000, is_prime(2000000))))
