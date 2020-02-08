import numpy as np
from sympy import randprime, isprime, nextprime
from secrets import token_bytes
import sys
import argparse

byte_floor = 63
byte_len = 8

def mod_exp(a, b, N):
  b = bin(b)[2:]
  r = 1
  for i in range(len(b) - 1, -1, -1):
      r = (r * a ** int(b[i])) % N
      a = (a ** 2) % N
  return r

def make_g():
  return 5

def make_a():
  byte_floor = 63
  return int.from_bytes(token_bytes(byte_floor), sys.byteorder)

def make_p():  
  global byte_floor, byte_len
  print("\ngenerating g, a, and p")                              
  bit_floor = byte_floor * byte_len
  floor = np.power(2, bit_floor)
  floor = 2 ** bit_floor
  ceiling = 2 * floor
  p = randprime(floor, ceiling)
  p_1 = (p - 1) / 2
  while not isprime(p) and not isprime(p_1):                                
      p = nextprime(p)
      p_1 = (p - 1) / 2
    
  return p
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Executing diffie-helman with specific parameters')
  parser.add_argument('-g', type=int, help="Generator for DH", default=None)
  parser.add_argument('-a', type=int, help="Exponent value", default=None)
  parser.add_argument('-p', type=int, help="Mod value", default=None)
  args = parser.parse_args()
  if not args.g:
    args.g = make_g()
  if not args.a:
    args.a = make_a()
  if not args.p:
    args.p = make_p()
  g = args.g
  a = args.a 
  p = args.p
  
  print("Values being used ::")
  print("g :", g)
  print("a :\n", a)
  print("p :\n", p)
  print("\n")

  r = mod_exp(g, a, p)
  print("g ** a mod p == \n", r)
  print("pow(g, a, p) == \n", pow(g, a, p), "\n")