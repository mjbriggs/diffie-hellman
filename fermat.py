import random
from math import ceil
from math import floor


def prime_test(N, k):
	# This is main function, that is connected to the Test button. You don't need to touch it.
	return fermat(N,k), miller_rabin(N,k)


def mod_exp(x, y, N):                            # O(n^3)
    # You will need to implement this function and change the return value.   
    if y == 0:
        return 1
    z = mod_exp(x, floor(y/2), N)
    if y % 2 == 0:
        return (z**2) % N
    else: 
        return (x*(z**2)) % N
	

def fprobability(k):
    # You will need to implement this function and change the return value.   
    return 1 - (1 / (2**k))


def mprobability(k):
    # You will need to implement this function and change the return value.   
    return 1 - (1 / (4**k))


def fermat(N,k):                                # O(n^4)
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    if(N == 1):                                 # O(1)
        return 'prime'
    i = 0
    b = N - 1
    a = -1
    random.seed()
    while i < k:                                # O(n)
        a = random.randint(1, b)
        if(mod_exp(a, b, N) != 1):              # O(n^3)
            return 'composite'
        i += 1
           
    return 'prime'


def miller_rabin(N,k):                          # O(n^5)
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    b = N - 1
    const_b = N - 1
    i = 0 
    a = -1
    while i < k:                            # O(n)
        a = random.randint(1, const_b)
        b = N - 1
        while b > 1:                        # O(1)
            me = mod_exp(a, b, N)           # O(n^3)
            if(me == const_b):              # O(1)
                b = 0
            elif me != 1:                   # O(1)
                return 'composite'
            b = floor(b/2)
        i += 1
    return 'prime'
