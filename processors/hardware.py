
from qiskit.transpiler import CouplingMap
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit_aer.noise import (
    NoiseModel,
    depolarizing_error,
    ReadoutError
)


BASIS_GATES = ['cx', 'id', 'rz', 'sx', 'x']


def get_processor_a():
    """Create the 5-qubit baseline processor."""

    edges = [
        [0, 1], [1, 0],
        [0, 2], [2, 0],
        [0, 3], [3, 0],
        [1, 4], [4, 1]
    ]

    coupling_map = CouplingMap(couplinglist=edges)

    backend = GenericBackendV2(
        num_qubits=5,
        coupling_map=coupling_map,
        basis_gates=BASIS_GATES,
        seed=42
    )

    noise_model = NoiseModel()

    noise_model.add_all_qubit_quantum_error(
        depolarizing_error(0.0005, 1),
        ['sx', 'x']
    )

    noise_model.add_all_qubit_quantum_error(
        depolarizing_error(0.005, 2),
        ['cx']
    )

    noise_model.add_all_qubit_readout_error(
        ReadoutError([
            [0.99, 0.01],
            [0.01, 0.99]
        ])
    )

    return {
        "backend": backend,
        "coupling_map": coupling_map,
        "noise_model": noise_model,
        "qubits": 5,
        "name": "Processor A"
    }


def get_processor_b():
    """Create the 7-qubit processor with a different topology."""

    edges = [
        [0, 1], [1, 0],
        [1, 2], [2, 1],
        [2, 3], [3, 2],
        [3, 4], [4, 3],
        [1, 5], [5, 1],
        [3, 6], [6, 3]
    ]

    coupling_map = CouplingMap(couplinglist=edges)

    backend = GenericBackendV2(
        num_qubits=7,
        coupling_map=coupling_map,
        basis_gates=BASIS_GATES,
        seed=42
    )

    noise_model = NoiseModel()

    noise_model.add_all_qubit_quantum_error(
        depolarizing_error(0.001, 1),
        ['sx', 'x']
    )

    noise_model.add_all_qubit_quantum_error(
        depolarizing_error(0.01, 2),
        ['cx']
    )

    noise_model.add_all_qubit_readout_error(
        ReadoutError([
            [0.98, 0.02],
            [0.02, 0.98]
        ])
    )

    return {
        "backend": backend,
        "coupling_map": coupling_map,
        "noise_model": noise_model,
        "qubits": 7,
        "name": "Processor B"
    }


processor_a = get_processor_a()
processor_b = get_processor_b()
