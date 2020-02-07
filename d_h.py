import numpy as np
from sympy import randprime, isprime, nextprime
from secrets import token_bytes
import sys

def mod_exp(a, b, N):
    b = bin(b)[2:]
    r = 1
    for i in range(len(b) - 1, -1, -1):
        r = (r * a ** int(b[i])) % N
        a = (a ** 2) % N
    return r

def make_dh_values():  
    print("generating g, a, and p")                              
    byte_floor = 63
    bit_floor = byte_floor * 8
    floor = np.power(2, bit_floor)
    floor = 2 ** bit_floor
    ceiling = 2 * floor
    g = 5
    a = int.from_bytes(token_bytes(byte_floor), sys.byteorder)
    p = randprime(floor, ceiling)
    p_1 = (p - 1) / 2
    while not isprime(p) and not isprime(p_1):                                
        p = nextprime(p)
        p_1 = (p - 1) / 2
    
    print("g :", g)
    print("a :", a)
    print("p :", p)
    return g, a, p
if __name__ == '__main__':
    
    # g, a, p = make_dh_values()

    # print("calculating g ** a mod p")
    # r = mod_exp(g, a, p)
    # print(r)
    # print(pow(g, a, p))

    # print("passing off stuff")

    a = 45158020556829761526566715715576392226971171334504306649714622565005857730477671732938482361956767937473240537042068826046002048740622296915051672250725
    v_in = 374101353318035325384877924330407926628932622145116106468674117878018335148034162010621982500266120905179821783711506834475123467869151157347117496461
    p = 54233470765699807132834647601416428149958922051760774775293415703747028052046543133967782327341505538314366645343467875720497447641715981000418239354479
    s = mod_exp(v_in, a, p)
    print("secret key:", s)