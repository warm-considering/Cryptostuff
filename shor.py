import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def iqft(n):
    #inverse quantum fourier transform
    qc = QuantumCircuit(n)
    for q in range(n//2):
        qc.swap(q, n-q-1)
    for i in range(n):
        for j in range(i):
            qc.cu1(-np.pi/float(2**(i-j)), j, i)
        qc.h(i)
    qc.name = "iqft"
    return qc


def c_amod15(a, p):
    #controlled mult by a mod 15
    if a not in [2,7,8,11,13]:
        raise ValueError("Invalid a")
    U = QuantumCircuit(4)
    for iteration in range(p):
        if a in [2,13]:
            U.swap(0,1)
            U.swap(1,2)
            U.swap(2,3)
        if a in [7,8]:
            U.swap(2,3)
            U.swap(1,2)
            U.swap(0,1)
        if a == 11:
            U.swap(1,3)
            U.swap(0,2)
        if a in [7,11,13]:
            for q in range(4):
                U.x(q)
        U = U.to_gate()
        U.name = "%i^%i mod 15" % (a, p)
        c_U = U.control()
        return c_U

ncount = 8
a = 2

qc = QuantumCircuit(ncount+4, ncount)

for q in range(ncount):
    qc.h(q)

qc.x(3+ncount)

for q in range(ncount):
    qc.append(c_amod15(a, 2**q), [q] + [i+ncount for i in range(4)])

qc.append(iqft(ncount), range(ncount))

qc.measure(range(ncount), range(ncount))
#qc.draw("text")

backend = Aer.get_backend("qasm_simulator")
results =  execute(qc, backend, shots=1024).result()
counts = results.get_counts()

fig = plt.figure()
ax = fig.add_subplot(111)
plot_histogram(counts, ax=ax)
plt.show()


