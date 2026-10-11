
from qiskit import QuantumCircuit
import random
import secrets


def generate_bb84_job(n_bits=300, rng=None):
    """Generate Alice's bits, their bases and the BB84 circuits."""

    if not isinstance(n_bits, int) or isinstance(n_bits, bool) or n_bits <= 0:
        raise ValueError("n_bits must be a positive integer.")

    if rng is None:
        rng = secrets.SystemRandom()

    alice_bits = [rng.randrange(2) for _ in range(n_bits)]
    alice_bases = [rng.randrange(2) for _ in range(n_bits)]
    bob_bases = [rng.randrange(2) for _ in range(n_bits)]

    circuits = []

    for i in range(n_bits):
        qc = QuantumCircuit(1, 1, name=f"bb84_bit_{i}")

        # Alice prepares the state.
        if alice_bits[i] == 1:
            qc.x(0)

        if alice_bases[i] == 1:
            qc.h(0)

        # Bob selects his measurement basis.
        if bob_bases[i] == 1:
            qc.h(0)

        qc.measure(0, 0)
        circuits.append(qc)

    return circuits, alice_bits, alice_bases, bob_bases


def calculate_qber(
    alice_bits,
    alice_bases,
    bob_bases,
    bob_results,
    test_fraction=0.20,
    rng=None
):
    """Estimate QBER and return the candidate keys."""

    lengths = [
        len(alice_bits),
        len(alice_bases),
        len(bob_bases),
        len(bob_results)
    ]

    if len(set(lengths)) != 1:
        raise ValueError("All input lists must have the same length.")

    if not 0 < test_fraction < 1:
        raise ValueError("test_fraction must be between 0 and 1.")

    if rng is None:
        rng = secrets.SystemRandom()

    for bit in alice_bits:
        if bit not in (0, 1):
            raise ValueError("Alice's bits must contain only 0 and 1.")

    for basis in alice_bases + bob_bases:
        if basis not in (0, 1):
            raise ValueError("Basis values must contain only 0 and 1.")

    # Convert measurement results into binary values.
    measured_bits = []

    for result in bob_results:
        value = str(result).strip().replace(" ", "")

        if value not in ("0", "1"):
            raise ValueError(f"Invalid measurement result: {result}")

        measured_bits.append(int(value))

    # Keep only positions where both selected the same basis.
    alice_sifted = []
    bob_sifted = []

    for a_bit, a_basis, b_basis, b_bit in zip(
        alice_bits,
        alice_bases,
        bob_bases,
        measured_bits
    ):
        if a_basis == b_basis:
            alice_sifted.append(a_bit)
            bob_sifted.append(b_bit)

    total_bits = len(alice_sifted)

    if total_bits < 2:
        raise ValueError("Not enough sifted bits to estimate QBER.")

    # Randomly select bits for error estimation.
    test_size = max(1, round(total_bits * test_fraction))
    test_size = min(test_size, total_bits - 1)

    test_indices = set(
        rng.sample(range(total_bits), test_size)
    )

    errors = sum(
        alice_sifted[i] != bob_sifted[i]
        for i in test_indices
    )

    qber = errors / test_size

    # Remove the bits publicly used for testing.
    alice_key = [
        alice_sifted[i]
        for i in range(total_bits)
        if i not in test_indices
    ]

    bob_key = [
        bob_sifted[i]
        for i in range(total_bits)
        if i not in test_indices
    ]

    return qber, alice_key, bob_key


def encrypt_message(message, key):
    """Encrypt a UTF-8 message using a binary key."""

    if not isinstance(message, str):
        raise TypeError("Message must be a string.")

    message_bytes = message.encode("utf-8")

    message_bits = ''.join(
        format(byte, "08b")
        for byte in message_bytes
    )

    if any(bit not in (0, 1) for bit in key):
        raise ValueError("Key must contain only 0 and 1.")

    if len(key) < len(message_bits):
        raise ValueError("Key is too short for this message.")

    ciphertext = [
        int(message_bits[i]) ^ key[i]
        for i in range(len(message_bits))
    ]

    return ciphertext, len(message_bits)


def decrypt_message(ciphertext, key, original_length):
    """Decrypt a message using Bob's copy of the key."""

    if not isinstance(original_length, int) or isinstance(original_length, bool):
        raise ValueError("Invalid message length.")

    if original_length < 0 or original_length % 8 != 0:
        raise ValueError("Message length must be a multiple of 8.")

    if len(ciphertext) < original_length:
        raise ValueError("Ciphertext is too short.")

    if len(key) < original_length:
        raise ValueError("Decryption key is too short.")

    if any(bit not in (0, 1) for bit in ciphertext[:original_length]):
        raise ValueError("Ciphertext must contain only 0 and 1.")

    if any(bit not in (0, 1) for bit in key[:original_length]):
        raise ValueError("Key must contain only 0 and 1.")

    decrypted_bits = [
        str(ciphertext[i] ^ key[i])
        for i in range(original_length)
    ]

    binary_message = ''.join(decrypted_bits)

    message_bytes = bytearray(
        int(binary_message[i:i + 8], 2)
        for i in range(0, len(binary_message), 8)
    )

    return message_bytes.decode("utf-8")
