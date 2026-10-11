
from qiskit.transpiler import CouplingMap
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit_aer.noise import (
    NoiseModel,
    depolarizing_error,
    ReadoutError
)


def get_processor_a():
    """Create the 5-qubit baseline processor."""

    edges = [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 4]
    ]

    coupling_map = CouplingMap(couplinglist=edges)

    backend = GenericBackendV2(
        num_qubits=5,
        coupling_map=coupling_map,
        basis_gates=['cx', 'id', 'rz', 'sx', 'x']
    )

    noise_model = NoiseModel()

    # Single-qubit gate errors.
    single_qubit_error = depolarizing_error(0.0005, 1)

    noise_model.add_all_qubit_quantum_error(
        single_qubit_error,
        ['sx', 'x']
    )

    # Two-qubit gate errors.
    two_qubit_error = depolarizing_error(0.005, 2)

    noise_model.add_all_qubit_quantum_error(
        two_qubit_error,
        ['cx']
    )

    # Measurement errors.
    readout_error = ReadoutError([
        [0.99, 0.01],
        [0.01, 0.99]
    ])

    noise_model.add_all_qubit_readout_error(readout_error)

    return {
        "backend": backend,
        "coupling_map": coupling_map,
        "noise_model": noise_model,
        "qubits": 5,
        "name": "Processor A"
    }


def get_processor_b():
    """Create the 7-qubit processor with a different topology and noise profile."""

    edges = [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 4],
        [1, 5],
        [3, 6]
    ]

    coupling_map = CouplingMap(couplinglist=edges)

    backend = GenericBackendV2(
        num_qubits=7,
        coupling_map=coupling_map,
        basis_gates=['cx', 'id', 'rz', 'sx', 'x']
    )

    noise_model = NoiseModel()

    # Single-qubit gate errors.
    single_qubit_error = depolarizing_error(0.001, 1)

    noise_model.add_all_qubit_quantum_error(
        single_qubit_error,
        ['sx', 'x']
    )

    # Two-qubit gate errors.
    two_qubit_error = depolarizing_error(0.01, 2)

    noise_model.add_all_qubit_quantum_error(
        two_qubit_error,
        ['cx']
    )

    # Measurement errors.
    readout_error = ReadoutError([
        [0.98, 0.02],
        [0.02, 0.98]
    ])

    noise_model.add_all_qubit_readout_error(readout_error)

    return {
        "backend": backend,
        "coupling_map": coupling_map,
        "noise_model": noise_model,
        "qubits": 7,
        "name": "Processor B"
    }


processor_a = get_processor_a()
processor_b = get_processor_b()
