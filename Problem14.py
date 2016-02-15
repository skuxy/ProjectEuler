# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million

# seems like a nice recursion

chain = []


def collatz_seq(n):
    global chain
    chain.append(n)
    if n == 1:
        return len(chain)
    elif n % 2 == 0:
        return collatz_seq(int(n / 2))
    else:
        return collatz_seq(3 * n + 1)


if __name__ == "__main__":
    number = 1000000
    max = 0
    ind = 0
    while (number > 1):
        chain = []
        new = collatz_seq(number)
        if (new > max):
            ind = number
            max = new
        number -= 1
    print(ind)
