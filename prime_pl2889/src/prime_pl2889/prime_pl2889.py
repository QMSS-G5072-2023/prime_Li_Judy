{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
}

import math

def is_prime(n):

    """
the function is used to determine whether the number is prime
if it is prime, the output will be True
otherwise it will be False

the user example:

is_prime(5)
True

is_prime(6)
False

    """


    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
