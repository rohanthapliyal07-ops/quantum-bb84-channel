from qiskit.transpiler import CouplingMap
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit_aer.noise import NoiseModel, depolarizing_error

def get_processor_a():
    """Processor A: 5 qubits, fixed baseline graph, synthetic noise model."""
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    coupling_map = CouplingMap(couplinglist=edges)
    backend = GenericBackendV2(num_qubits=5, coupling_map=coupling_map, basis_gates=['cx', 'id', 'rz', 'sx', 'x'])
    
    noise_model = NoiseModel()
    noise_model.add_all_qubit_quantum_error(depolarizing_error(0.0005, 1), ['sx', 'x', 'rz'])
    noise_model.add_all_qubit_quantum_error(depolarizing_error(0.005, 2), ['cx'])
    
    return {"backend": backend, "coupling_map": coupling_map, "noise_model": noise_model, "qubits": 5}

def get_processor_b():
    """Processor B: 7 qubits, heavy-hex-inspired graph, contemporary baseline."""
    edges = [[0, 1], [1, 2], [2, 3], [3, 4], [1, 5], [3, 6]]
    coupling_map = CouplingMap(couplinglist=edges)
    backend = GenericBackendV2(num_qubits=7, coupling_map=coupling_map, basis_gates=['cx', 'id', 'rz', 'sx', 'x'])
    
    noise_model = NoiseModel()
    noise_model.add_all_qubit_quantum_error(depolarizing_error(0.001, 1), ['sx', 'x', 'rz'])
    noise_model.add_all_qubit_quantum_error(depolarizing_error(0.01, 2), ['cx'])
    
    return {"backend": backend, "coupling_map": coupling_map, "noise_model": noise_model, "qubits": 7}

# Module-level instances for direct import
processor_a = get_processor_a()
processor_b = get_processor_b()