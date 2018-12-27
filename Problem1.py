# Project Euler: Problem 1:

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def is_multiple_of(number, multiple_of):
    return number % multiple_of is 0


if __name__ == "__main__":
    summa = 0
    for i in range(1000):
        if is_multiple_of(i, 3) or is_multiple_of(i, 5):
            summa += i
    print(summa)
