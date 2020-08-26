import shor1, rsa
n, e = rsa.rsaKeyGen()
print("Public key pair: "+str(n)+', '+str(e))
d = shor1.rsaCrack(n, e, shor1.simbackend)
print("Cracked pkey: "+str(d))
