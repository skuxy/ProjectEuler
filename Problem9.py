# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


if __name__ == "__main__":

    # until 500, because the number is surely below that line
    for i in range(100, 500):
        for j in range(100, 500):
            for z in range(100, 500):
                if is_pythagorean_triplet(i, j, z) and i + j + z == 1000:
                    print("Sought triple is: " + str((i, j, z)))
                    print(i * j * z)
