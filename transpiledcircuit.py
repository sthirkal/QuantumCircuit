from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(5, 'q')
creg_c = ClassicalRegister(5, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.u(pi / 2, 0, 3.141592653589793, qreg_q[0])
circuit.u(pi / 2, 0, 3.141592653589793, qreg_q[1])
circuit.u(pi / 2, 0, 3.141592653589793, qreg_q[2])
circuit.u(pi / 2, 0, 3.141592653589793, qreg_q[3])
circuit.u(pi / 2, 0, 3.141592653589793, qreg_q[4])
circuit.measure(qreg_q[0], creg_c[0])
circuit.measure(qreg_q[1], creg_c[1])
circuit.measure(qreg_q[2], creg_c[2])
circuit.measure(qreg_q[3], creg_c[3])
circuit.measure(qreg_q[4], creg_c[4])
