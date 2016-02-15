# Project Euler: Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

# modifying Erastothenes algorithm from Problem 3

def is_prime(a):
    return all(a % i for i in xrange(2, a))


if __name__ == "__main__":
    number = 3
    nth_prime = 1
    while (True):
        if all(number % i for i in xrange(2, number)):
            nth_prime += 1
        if nth_prime == 10001:
            break
        number += 2
    print(number)
