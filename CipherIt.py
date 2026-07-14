#!/usr/bin/env python3

import os 
import argparse
from cryptography.fernet import Fernet
from tqdm import tqdm
import time


parser=argparse.ArgumentParser("Encrypt files with Fernet")
parser.add_argument("-p","--path",required=True,help = "The path of files to be encrypted")
parser.add_argument("-k","--key",required=True,type=str,help = "The path where you want the key to be stored")
parser.add_argument("-e","--encrypt",action="store_true",help="Encrypt the files in the specified directory")
parser.add_argument("-d","--decrypt",action="store_true",help="Decrypt the files in the specified directory")
args = parser.parse_args()
if args.encrypt == args.decrypt:
    parser.error("Choose exactly one of --encrypt or --decrypt.")

IGNORE = ["ciphertool.py","thekey.key","os","sys"]
file_paths = []
path = args.path
if os.path.isfile(path):
    file_paths.append(path)

elif os.path.isdir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
									if file not in IGNORE:
										file_paths.append(os.path.join(root, file))
else:
    print("Invalid path.")
    exit(1)
if not file_paths:
    print("[!] No files found.")
    exit(0)
else: 
       print(f"[+] Found {len(file_paths)} file(s).")
						

def show_banner():
	print("=" * 60)
	print(r"""
 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗     ██╗████████╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗    ██║╚══██╔══╝
██║     ██║██████╔╝███████║█████╗  ██████╔╝    ██║   ██║
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗    ██║   ██║
╚██████╗██║██║     ██║  ██║███████╗██║  ██║    ██║   ██║
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝   ╚═╝
""")
	print("=" * 60)
		

def Encrypt():
    start_time = time.perf_counter()

    os.makedirs(args.key, exist_ok=True)

    key = Fernet.generate_key()
    cipher = Fernet(key)

    with open(os.path.join(args.key, "thekey.key"), "wb") as thekey:
        thekey.write(key)

    for file in tqdm(file_paths,
                     desc="Encrypting",
                     unit="file",
                     colour="green"):

        with open(file, "rb") as f:
            contents = f.read()

        encrypted = cipher.encrypt(contents)

        with open(file, "wb") as f:
            f.write(encrypted)

    elapsed = time.perf_counter() - start_time

    print(f"\n[✓] Successfully encrypted {len(file_paths)} files in {elapsed:.2f} seconds.")

def Decrypt():
    start_time = time.perf_counter()

    key_path = args.key

    if os.path.isdir(key_path):
        key_file = os.path.join(key_path, "thekey.key")
    else:
        key_file = key_path

    with open(key_file, "rb") as thekey:
        key = thekey.read()

    cipher = Fernet(key)

    success = 0

    for file in tqdm(file_paths,
                     desc="Decrypting",
                     unit="file",
                     colour="cyan"):

        try:
            with open(file, "rb") as f:
                contents = f.read()

            decrypted = cipher.decrypt(contents)

            with open(file, "wb") as f:
                f.write(decrypted)

            success += 1

        except Exception as e:
            print(f"\n[ERROR] {os.path.basename(file)} : {e}")

    elapsed = time.perf_counter() - start_time
    print(f"\n[✓] Successfully decrypted {success} out of {len(file_paths)} files in {elapsed:.2f} seconds.")

if __name__ == "__main__":
	show_banner()
	if args.encrypt:
		print("[+] Starting encryption...")
		Encrypt()
	elif args.decrypt:
		print("[+] Starting decryption...")
		Decrypt()
	else:
		print("Please specify at least one mode(Encryption/Decryption)")
						
        
  	
