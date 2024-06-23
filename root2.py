#/usr/bin/python

from math import sqrt
# loading decimal library
from decimal import *

def main():
    n = '2.0'
    getcontext().prec = 80
    a = Decimal(2)
    root2th = sqrt(float(n))
    print(root2th)
    print(a.sqrt())
    print('1.41421356237309504880168872420969807856967187537694807317667973799073247846210703', '=> reference')

if __name__ == '__main__':
    main()
    print('SQRT OVER')
