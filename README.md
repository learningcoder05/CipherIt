# CipherIt 🔐

A lightweight Linux command-line utility built in Python for securely encrypting and decrypting files using **Fernet authenticated symmetric encryption**. CipherIt was developed as a cybersecurity learning project to demonstrate practical cryptography, Linux CLI development, filesystem automation, and secure software engineering.

---

## Features

* 🔒 Secure file encryption and decryption using Fernet
* 🐧 Linux-friendly command-line interface
* 📁 Recursive directory traversal
* 📄 Single file and directory support
* 🔑 Automatic encryption key generation
* 📊 Progress bar with execution timing
* ⚡ Lightweight and easy to use
* 🛠️ Simple argument-based CLI

---

## Technologies Used

* Python 3
* Cryptography (Fernet)
* tqdm
* argparse
* os
* time

---

## Project Structure

```text
CipherIt/
│
├── ciphertool.py
├── requirements.txt
├── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/learningcoder05/CipherIt.git
cd CipherIt
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Usage

### Encrypt

```bash
python3 ciphertool.py \
    --path /path/to/files \
    --key ./keys \
    --encrypt
```

### Decrypt

```bash
python3 ciphertool.py \
    --path /path/to/files \
    --key ./keys/thekey.key \
    --decrypt
```

---

## Command Line Arguments

| Argument          | Description                                         |
| ----------------- | --------------------------------------------------- |
| `-p`, `--path`    | File or directory to process                        |
| `-k`, `--key`     | Key directory (encryption) or key file (decryption) |
| `-e`, `--encrypt` | Encrypt the specified target                        |
| `-d`, `--decrypt` | Decrypt the specified target                        |

---

## Example

### Encryption

```text
============================================================

 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗     ██╗████████╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗    ██║╚══██╔══╝
██║     ██║██████╔╝███████║█████╗  ██████╔╝    ██║   ██║
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗    ██║   ██║
╚██████╗██║██║     ██║  ██║███████╗██║  ██║    ██║   ██║
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝   ╚═╝

============================================================

[+] Starting encryption...

Encrypting: 100%|████████████████████████████| 25/25

[✓] Successfully encrypted 25 files in 0.82 seconds.
```

---

## Learning Objectives

This project was developed to strengthen practical skills in:

* Linux command-line application development
* Python scripting and automation
* Applied cryptography
* Recursive filesystem traversal
* Secure file handling
* CLI application design
* Error handling and input validation

---

## Future Improvements

* Rich terminal interface
* Password-derived key support (PBKDF2/Argon2)
* Configuration file support
* Logging
* File integrity verification
* Digital signatures
* Multi-threaded processing
* Package distribution via `pip`

---

## Disclaimer

CipherIt is an educational project intended to demonstrate cryptographic concepts and command-line application development. It is not intended to replace production-grade encryption software or enterprise key-management solutions.

---

## License

This project is licensed under the MIT License.
