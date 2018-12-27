# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers

# Numbers are in Problem13input.txt file

if __name__ == "__main__":
    print(str(sum(list(map(int, open("Problem13input.txt").readlines()))))[0:10])
