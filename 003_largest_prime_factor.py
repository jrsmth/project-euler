# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

x = 600851475143
divisor = 2

while(x != 1):
    if(x % divisor == 0):
        x /= divisor
    else:
        divisor+=1

print(divisor)




### NOTES 

# Take 100

# Is 100 div by 2: yes
# Is 50 div by 2: yes
# Is 25 div by 2. No
# Is 25 div by 3: no
# Is 25 div by 4: no
# Is 25 div by 5: yes
# Is 5 div by 5: yes
# Current = 1
# Therefore: 100 = {2,2,5,5}

# Are all of these factors prime?
# Yes I think so.
# I can prove it implicitly, take 24 = 8 * 3, 8 is not prime but we would have decomposed 8 into twos already
# Proof by contradiction:
# Let’s assume there is a number in our list that isn’t prime. That means we could put it though our filter and decompose it into more primes. 
# Is X div by 2? No bc we tested all 2’s
# Is X div by 3? No because we tested all 3’s
# And etc all the way to X-1, hence X must be prime because we can’t get any factors out of it.