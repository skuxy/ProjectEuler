# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers

# Numbers are in Problem13input.txt file

if __name__ == "__main__":
    list_of_nums = list(map(int, open("Problem13input.txt").readlines()))
    print(str(sum(list_of_nums))[0:10])
