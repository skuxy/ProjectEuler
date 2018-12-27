# Project Euler: Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# worst.function.name.ever.

def n_evenly_divisible_by_n_to_check(n, n_to_check=20):
    for i in range(1, n_to_check + 1):
        if n % i != 0:
            return False
    return True


# Answer: 232792560
# to optimize, check only every 20th number, beginning with 20 :)
if __name__ == "__main__":
    number = 20
    while not n_evenly_divisible_by_n_to_check(number):
        number += 20
    print("Number evenly divisible by all number from 1 to 20 is " + str(number))
