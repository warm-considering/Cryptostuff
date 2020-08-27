import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
from qiskit.aqua.algorithms import Shor
import random as rand
from qiskit import IBMQ
from qiskit.providers.aer import *
from qiskit.aqua import QuantumInstance
from rsa import *
from decimal import *
import time

provider = IBMQ.enable_account(<--INSERT IBM AUTH KEY HERE-->)
#backend_options = {"method": "extended_stabilizer"}
localbackend = StatevectorSimulator()

simbackend = provider.get_backend("ibmq_qasm_simulator")


def rsaCrack(n, e, backend):
    print("Starting Shor's algorithm for n, e = "+str(n)+', '+str(e))
    for i in range(2, n):
        if gcd(n, i) == 1:
            a = i
            print("a chosen as "+str(a))
            break
    s = Shor(n, a)
    s.set_backend(backend)
    t1 = time.time()
    result = s.run()
    print(result)
    t2 = time.time()
    nums = result['factors'][0]
    print("Shor runtime = "+str(t2-t1))
    p, q = nums
    phi = (int(p)-1)*(int(q)-1)
    d = 0.1
    x = 1
    while not d.is_integer():
        d = (1+x*phi)/e
        x += 1
    return int(d)

