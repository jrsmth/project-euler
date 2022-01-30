# coding=utf-8
# Problem 4: https://projecteuler.net/problem=4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n):
    return True if str(n) == str(n)[::-1] else False

def findLargestPalindrome():
    pals = []
    for x in range(999, 99, -1):
        for y in range(999, 99, -1):
            if(isPalindrome(x * y)): 
                pals.append(x*y)
    return max(pals)

print(findLargestPalindrome())
            

