import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
from qiskit.aqua.algorithms import Shor
import random as rand
from qiskit.providers.aer import *
from rsa import *
import time

backend = QasmSimulator()

def rsaCrack(n, e, backend):
    for i in range(1, n):
        if gcd(n, i) == 1:
            a = i
    s = Shor(n, a)
    s.set_backend(backend)
    t1 = time.time()
    result = s.run()
    t2 = time.time()
    print("Shor runtime = "+str(t2-t1))
    p, q = result[0]
    phi = (p-1)*(q-1)
    d = 0.1
    x = 1
    while not d.is_integer():
        d = (1+x*phi)/e
        x += 1
    return int(d)

