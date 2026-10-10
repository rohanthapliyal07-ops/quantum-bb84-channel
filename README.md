# ⚛️ Quantum-Secured Communication Channel (BB84)

> *"Entangling qubits so you don't have to."*

Welcome to the **BB84 Quantum Key Distribution (QKD) Simulator**—a clean, modular Qiskit implementation that generates unhackable keys across simulated quantum hardware, detects eavesdroppers in real-time, and encrypts custom user messages with One-Time Pad (OTP) precision.

---

## 🚀 Why This Exists

Classical encryption is living on borrowed time. When fault-tolerant quantum computers arrive, standard asymmetric algorithms like RSA and ECC will be as secure as a screen door on a submarine.

This repository implements the **BB84 Protocol**, proving that quantum mechanics—specifically the No-Cloning Theorem and Heisenberg's Uncertainty Principle—is the ultimate cryptographic firewall.

### 💡 Key Features

* **⚛️ Core BB84 Circuit Engine**: Modular state preparation ($|0\rangle, |1\rangle, |+\rangle, |-\rangle$), basis choice matching, and measurement in Qiskit.
* **⚡ Hardware Noise Simulation**: Realistic noise modeling using `Qiskit Aer` to evaluate Quantum Bit Error Rate ($\text{QBER}$) across simulated processors.
* **📊 Automated Analytics**: Dynamic calculation and automated reporting of $\text{QBER}$ and sifted key lengths directly to CSV tables and Matplotlib plots.
* **🔒 Interactive OTP Encryption**: Real-time user input conversion to binary, One-Time Pad (XOR) encryption using the generated quantum key, and flawless receiver decryption.

---

## 🛠️ Repository Architecture

```text
quantum-bb84-channel/
│
├── processors/
│   ├── __init__.py
│   └── hardware.py       # Quantum noise backend configurations
│
├── results/
│   ├── figures/          # Exported QBER comparative plots
│   └── tables/           # Metric output CSVs
│
├── src/
│   ├── __init__.py
│   └── qkd.py            # Core BB84 state prep & basis matching logic
│
├── main.ipynb            # Interactive execution notebook & live OTP demo
├── requirements.txt      # Dependency manifest
└── README.md             # Project documentation
```

---

## ⚡ Quickstart

### 1. Clone & Install
```bash
git clone https://github.com/rohanthapliyal07-ops/quantum-bb84-channel.git
cd quantum-bb84-channel
pip install -r requirements.txt
```

### 2. Run the Engine
Open `main.ipynb` in VS Code or Jupyter Notebook:
1. **Run All Cells** to simulate qubit transmission across noisy vs. ideal backends.
2. Enter your secret message into the interactive cell at the bottom to watch the One-Time Pad encrypt and decrypt your text in real-time!

---

## 📊 Live Metrics & Quantum Realism

Because quantum measurement is fundamentally probabilistic, run metrics vary dynamically across executions. Noise simulation models real-world decoherence, giving authentic hardware results:

| Processor | QBER (%) | Sifted Key Length (bits) |
| :--- | :--- | :--- |
| **Processor A (Noisy)** | `~0.135%` | `~740` |
| **Processor B (Ideal)** | `0.000%` | `~740` |

---

## 🛡️ Eavesdropper Detection Rule

If an eavesdropper (Eve) attempts an intercept-resend attack on the channel, state collapse immediately spikes the error rate:

$$\text{QBER} > 11\% \implies \text{ABORT KEY (Eve Intercepted!)} \quad 🚨$$

---

## 🧰 Tech Stack

* **Quantum Backend**: `qiskit>=1.0.0`, `qiskit-aer>=0.14.0`
* **Data & Analytics**: `pandas`, `matplotlib`
* **Environment**: Jupyter Notebook / VS Code

---

*Built with ⚛️ for the hackathon. Remember: If someone measures your qubits early, tell them to stop observing your boundaries.*
