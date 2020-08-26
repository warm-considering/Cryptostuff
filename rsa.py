import numpy as np
import random as rand

global d #private key

def gcd(a, b): #this is very cool
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def modExp(a, b ,n): #compute a^b (mod n)
    if n == 1:
        return 0
    else:
        r = 1
        a = a % n
        while b > 0:
            if b % 2 == 1:
                r = (r*a) % n
            b = b >> 1
            a = (a**2) % n
        return r

def testPrime(n):
    a = 0
    while a < n:
        a+=1
        if gcd(a,n) != 1:
            continue
        elif modExp(a, n-1, n) == 1:
            continue
        else:
            return False
    return True

def rsaKeyGen():
    global d
    p = rand.randint(12, 20)
    while testPrime(p) == False:
        p = rand.randint(12, 20)
    '''q = rand.randint(1, 10)
    while testPrime(q) == False or q == p:
        q = rand.randint(2, 10)'''
    q = 7

    n = p*q
    phi = (p-1)*(q-1)
    
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            e = i
            break
        else:
            continue
    d = 0.1
    x = 1
    while not d.is_integer():
        d = (1 +x*phi)/e
        x+=1
    d = int(d)
    print("Calculated pkey: "+str(d))
    return (n, e)

def rsaEnc(msg, pkey):
    n, e = pkey
    msg = msg.upper()
    chars = list(msg)
    
    encchars = [str(modExp( ord(m), e, n ) )  for m in chars]
    return encchars

def rsaDec(encarr, n):
    global d
    decarr = [chr(modExp(int(c), d, n)) for c in encarr]
    msg = ""
    return msg.join(decarr)


