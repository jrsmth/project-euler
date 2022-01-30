# coding=utf-8
# Problem 5: https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

found = False
x = 9699690
divisors = [4, 8, 9, 12, 16, 18, 20]

def test(n):
    for i in range(1,21):
        if not (n % i == 0): 
            return False
    return True

while not (found):
    x+=2
    if(test(x)):
        found = True

print(x)


# Notes

# What about the product of 1..20? -> 2432902008176640000, this is the upper bound

# How can we speed this up? -> larger than 2520, must be even 
# What about the prime numbers? 2, 3, 5, 7, 11, 13, 17, 19 -> must be at least as big as this -> 9699690
# We no longer need to divide by these number in the test either, only [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
# Even this can be reduced: if 2 and 7 are present, 14 is also present -> reduced test list: [4, 8, 9, 12, 16, 18, 20]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# [4, 2x3, 8, 9, 10, 12, 7x2, 5x3, 16, 18, 20]
# ^ this reduction in divisors did not work...

# How long to run? -> well over 2 mins
# ideally it is under 1 min but I'm moving on.