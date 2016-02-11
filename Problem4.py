#Project Euler: Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(num):
    length = len(num)
    for i in range(int(length/2)):
        if num[i] != num[length-i-1]:
            return False
    return True

#so I can return from double loop
#YOLO
def findBiggest():
    lon = [] #list of numbers
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            number = str(i*j)
            if isPalindrome(number):
                lon.append(int(number))
    return(str(max(lon)))

if __name__ == "__main__":
    print(findBiggest())