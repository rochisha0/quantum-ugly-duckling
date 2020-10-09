import numpy as np
from qiskit import execute, QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.providers.aer import QasmSimulator

# Import from Qiskit Aer noise module
from qiskit.providers.aer.noise import NoiseModel
from qiskit.providers.aer.noise import QuantumError, ReadoutError
from qiskit.providers.aer.noise import pauli_error

## Applying bit flip error
def get_noise():
    p_reset = 0.03
    p_meas = 0.1
    p_gate1 = 0.05

    # QuantumError objects
    error_reset = pauli_error([('X', p_reset), ('I', 1 - p_reset)])
    error_meas = pauli_error([('X',p_meas), ('I', 1 - p_meas)])
    error_gate1 = pauli_error([('X',p_gate1), ('I', 1 - p_gate1)])
    error_gate2 = error_gate1.tensor(error_gate1)

    # Add errors to noise model
    noise_bit_flip = NoiseModel()
    noise_bit_flip.add_all_qubit_quantum_error(error_reset, "reset")
    noise_bit_flip.add_all_qubit_quantum_error(error_meas, "measure")
    noise_bit_flip.add_all_qubit_quantum_error(error_gate1, ["u1", "u2", "u3"])
    noise_bit_flip.add_all_qubit_quantum_error(error_gate2, ["cx"])

    return noise_bit_flip

def random_number():

    circ = QuantumCircuit(4)
    simulator = QasmSimulator()

    #NQRNS Circuit
    for i in range(200):
        circ.u3(0,0,0,0)
        circ.u3(0,0,0,1)
        circ.u3(0,0,0,2)
        circ.u3(0,0,0,3)
        circ.cx(0,1)
        circ.cx(1,2)
        circ.cx(0,2)
        circ.cx(0,3)
        circ.cx(1,3)
        circ.cx(2,3)
        circ.barrier()

    circ.measure_all()

    noise_bit_flip = get_noise()
    #get output
    job = execute(circ, simulator,
              basis_gates=noise_bit_flip.basis_gates,
              noise_model=noise_bit_flip, shots= 1)
    result_bit_flip = job.result()
    counts_bit_flip = result_bit_flip.get_counts(0)


    num=list(counts_bit_flip.keys())[0]
    num = int(num, 2)
   

    return num

