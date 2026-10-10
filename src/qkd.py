from qiskit import QuantumCircuit
import random

def generate_bb84_job(n_bits=300):
    """Generates random Alice/Bob bits/bases and a list of 1-qubit circuits."""
    alice_bits = [random.randint(0, 1) for _ in range(n_bits)]
    alice_bases = [random.randint(0, 1) for _ in range(n_bits)] # 0: Z-basis, 1: X-basis
    bob_bases = [random.randint(0, 1) for _ in range(n_bits)]
    
    circuits = []
    for i in range(n_bits):
        qc = QuantumCircuit(1, 1, name=f"bb84_bit_{i}")
        
        # 1. Alice prepares the qubit
        if alice_bits[i] == 1:
            qc.x(0)
        if alice_bases[i] == 1:
            qc.h(0)
            
        # 2. Bob measures in his chosen basis
        if bob_bases[i] == 1:
            qc.h(0)
        qc.measure(0, 0)
        
        circuits.append(qc)
        
    return circuits, alice_bits, alice_bases, bob_bases

def calculate_qber(alice_bits, alice_bases, bob_bases, bob_results):
    """Calculates Sifted Key and Quantum Bit Error Rate (QBER)."""
    sifted_key_alice = []
    sifted_key_bob = []
    errors = 0
    matches = 0
    
    for a_bit, a_base, b_base, b_res in zip(alice_bits, alice_bases, bob_bases, bob_results):
        if a_base == b_base:  # Bases match (Sifting step)
            matches += 1
            sifted_key_alice.append(a_bit)
            sifted_key_bob.append(int(b_res))
            if a_bit != int(b_res):
                errors += 1
                
    qber = (errors / matches) if matches > 0 else 0.0
    return qber, sifted_key_alice, sifted_key_bob

def encrypt_message(message, key):
    """Encrypts a string message using the quantum sifted key via XOR."""
    message_bytes = message.encode('utf-8')
    binary_message = ''.join(format(byte, '08b') for byte in message_bytes)
    
    if len(key) < len(binary_message):
        raise ValueError("Sifted key is too short for this message! Increase n_bits.")
        
    ciphertext = []
    for i in range(len(binary_message)):
        encrypted_bit = int(binary_message[i]) ^ key[i]
        ciphertext.append(encrypted_bit)
        
    return ciphertext, len(binary_message)

def decrypt_message(ciphertext, key, original_length):
    """Decrypts the ciphertext using Bob's sifted key."""
    binary_message = []
    for i in range(original_length):
        decrypted_bit = ciphertext[i] ^ key[i]
        binary_message.append(str(decrypted_bit))
        
    binary_string = "".join(binary_message)
    byte_array = bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))
    
    return byte_array.decode('utf-8', errors='ignore')