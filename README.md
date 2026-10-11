# 🔐 Quantum Secure Communication Channel using BB84

### Because sharing secrets is easy. Sharing them securely is the actual problem.

Welcome to a little experiment where quantum mechanics meets cybersecurity, Alice has something to say to Bob, and Eve is politely advised to mind her own business.

This project implements the **BB84 Quantum Key Distribution (QKD) protocol** using Python and Qiskit. It demonstrates how two parties can establish a shared secret key using quantum states, estimate transmission errors, and use the resulting key to encrypt and decrypt classical messages.

We also throw two simulated quantum processors into the mix to see how their connectivity and noise characteristics affect quantum circuit execution.

**Spoiler:** Having more qubits doesn't automatically make you better. Just like having more RAM doesn't make you a better programmer.

---

## 🧠 What Are We Actually Building?

Imagine Alice wants to send Bob a secret message.

The internet is full of curious people. Eve is one of them.

Instead of directly sending Bob the encryption key, Alice and Bob use the BB84 protocol to generate a shared secret key through quantum communication.

The interesting part?

If someone tries to observe a quantum state in the wrong basis, quantum measurement can introduce detectable errors.

In other words, quantum mechanics gives us a way to detect certain kinds of eavesdropping.

**Our mission:** Simulate this process, measure the errors, and investigate how different processor architectures perform.

---

## ⚛️ The BB84 Protocol

Proposed by Charles Bennett and Gilles Brassard in 1984, BB84 is one of the foundational protocols in quantum cryptography.

Here's how our implementation works:

1. **Alice gets random:** Generates random binary bits and randomly selects Z or X bases.
2. **Qubit preparation:** Alice encodes her bits using quantum gates.
3. **Bob makes his choices:** Bob independently selects measurement bases.
4. **Measurement time:** Bob measures the received qubits.
5. **Basis reconciliation:** Alice and Bob compare their basis choices. Matching bases survive; mismatches get discarded.
6. **QBER estimation:** They reveal a random sample of matching bits to estimate the error rate. Those test bits are discarded.
7. **Candidate key generation:** The remaining bits become candidate shared keys.

The error metric:

\[
QBER = \frac{\text{Errors in test bits}}{\text{Total test bits}}
\]

A lower QBER generally indicates better agreement between Alice's and Bob's measurements.

Eve, meanwhile, has made the situation considerably more complicated.

---

## 🖥️ Meet the Processors

We created two synthetic quantum processor configurations. Different qubit counts, different connectivity, different noise profiles.

Basically, a quantum computing face-off.

| Specification | Processor A | Processor B |
|---|---:|---:|
| Qubits | 5 | 7 |
| Connectivity | Centralised | Chain with branches |
| Single-qubit error | 0.0005 | 0.001 |
| Two-qubit error | 0.005 | 0.01 |
| Readout error | 1% | 2% |

Both processors use Qiskit's `GenericBackendV2` and Qiskit Aer for simulation.

**Important:** These are simulated configurations, not real quantum computers. No actual quantum hardware was harmed during this experiment.

---

## 🔬 Two Experiments, One Repository

### 1. BB84 Quantum Key Distribution

Our main experiment.

We simulate 1,500 qubits per trial and perform three trials on each processor configuration.

We investigate:

- QBER.
- Sifted and candidate key lengths.
- Agreement between Alice's and Bob's candidate keys.
- Circuit depth.
- Gate count.
- Experiment execution time.

### 2. GHZ-Based Architecture Benchmark

Here's where processor connectivity gets its own spotlight.

Since our BB84 circuits operate on individual qubits, they don't meaningfully exercise multi-qubit connectivity.

So we introduce a separate five-qubit GHZ-state experiment.

We compare:

- Transpiled circuit depth.
- Total gate count.
- CX gate count.
- SWAP gate count.
- Frequency of expected correlated GHZ measurement outcomes.

Why GHZ?

Because sometimes you need to bring multiple qubits together to see what a processor is really capable of.

---

## 💬 Alice Has Something to Say

The project also includes an interactive message transmission demonstration.

Alice enters a message. The BB84 protocol generates candidate keys. If the keys match and are long enough, the message is encrypted using XOR.

\[
C = M \oplus K
\]

Bob then decrypts it:

\[
M = C \oplus K
\]

The message is converted from UTF-8 text into binary before encryption.

No mysterious black box. Just bits, quantum circuits and a little bit of XOR magic.

---

## 📊 What Does the Project Generate?

Our experiments automatically produce results.

| File | Purpose |
|---|---|
| `metrics.csv` | Individual BB84 trial results |
| `summary.csv` | Processor performance summary |
| `architecture_metrics.csv` | GHZ architecture benchmark |
| `qber_comparison.png` | QBER comparison graph |
| `architecture_comparison.png` | CX gate count comparison |

Graphs and CSVs are stored in the `results/` directory.

---

## 🗂️ Project Structure

```text
quantum-bb84-channel/
│
├── processors/
│   ├── __init__.py
│   └── hardware.py
│
├── results/
│   ├── figures/
│   │   ├── qber_comparison.png
│   │   └── architecture_comparison.png
│   │
│   └── tables/
│       ├── metrics.csv
│       ├── summary.csv
│       └── architecture_metrics.csv
│
├── src/
│   └── qkd.py
│
├── main.ipynb
├── requirements.txt
└── README.md
```

---

## ⚙️ Getting Started

Want to run it yourself? Excellent. Curiosity is a good habit.

### 1. Clone the repository

```bash
git clone https://github.com/rohanthapliyal07-ops/quantum-bb84-channel.git
```

### 2. Enter the project directory

```bash
cd quantum-bb84-channel
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate it (Windows)

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Launch Jupyter

```bash
jupyter notebook
```

Open `main.ipynb`, run the experiment and let the qubits do their thing.

---

## 🛠️ Tech Stack

- **Python** – The brains behind the operation.
- **Qiskit** – Building and transpiling quantum circuits.
- **Qiskit Aer** – Simulating quantum computers and noise.
- **Pandas** – Making experimental data manageable.
- **Matplotlib** – Turning numbers into graphs.
- **Jupyter Notebook** – Where all the experiments come together.

---

## 🚧 Current Limitations & Future Work

Let's be honest: a simulation is not a magical security certificate.

Our current implementation is an educational demonstration, not a production-ready QKD system.

Future improvements:

- Simulating Eve's interception and measurement attacks.
- Implementing error correction.
- Adding privacy amplification.
- Authenticating the classical communication channel.
- Studying QBER under different noise conditions.
- Exploring finite-key security.
- Building a graphical interface for Alice and Bob.
- Extending processor architecture comparisons.

Also, XOR encryption alone doesn't magically make something a secure One-Time Pad. That requires a truly random, secret, sufficiently long key that is never reused.

We're here to learn quantum security, not accidentally invent quantum insecurity.

---

## 🎯 The Bigger Picture

This project explores the intersection of quantum computing and cybersecurity.

It aims to demonstrate how quantum mechanics can support secure key distribution and how processor architecture and noise influence simulated quantum circuit behaviour.

Because the future of cybersecurity might be quantum.

And Eve probably isn't going anywhere.

---

**Built with Python, Qiskit, and an unreasonable number of qubits.**

*Alice sends. Bob measures. Eve regrets asking.* 🔐
