import time
import sys
from modules.encoders import base64_encode, base64_decode
from modules.ciphers import caesar_cipher, reverse_text
from modules.hashers import sha256_hash
from modules.bruteforce import load_wordlist, brute_force_sha256, brute_force_md5

# === SETTINGS ===
GREEN = "\033[92m"
RESET = "\033[0m"

def typewriter(text, delay=0.01):
    for char in text:
        sys.stdout.write(GREEN + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fastprint(text):
    print(GREEN + text + RESET)

def banner():
    typewriter(r"""
    .---------------------------------------.
   /           _____________________       /|
  +---------------------------------------+ |
  |  |  █ █ █ █ █ █ █ █ █ █ █ █ █ █ █  |  | |
  |  |  █ █ █ █ █ █ █ █ █ █ █ █ █ █ █  |  | |
  |  |  █ █ █ █       ◉       █ █ █ █  |  | |
  |  |  █ █ █ █ █ █ █ █ █ █ █ █ █ █ █  |  | |
  |  |  █ █ █ █ █ █ █ █ █ █ █ █ █ █ █  |  | |
  |  |______________________________|  |  |
  +---------------------------------------+/

                 Cyber-Jot
    """, delay=0.001)

    typewriter(":: PandoraBox v1.0 — Unleash the Data ::\n", delay=0.02)
    time.sleep(0.4)
    typewriter("Loading transformation modules... [OK]", delay=0.02)
    time.sleep(0.3)
    typewriter("Initializing terminal interface... [OK]\n", delay=0.02)
    time.sleep(0.3)

def menu():
    typewriter("""
=== PandoraBox Tools ===
1. Base64 Encode
2. Base64 Decode
3. Caesar Cipher (+3)
4. Reverse Text
5. SHA256 Hash
6. Brute Force
7. Exit
""", delay=0.005)

def processing_banner(operation_name):
    typewriter(f"\n>> Opening module: {operation_name}...", delay=0.02)
    time.sleep(0.3)
    typewriter(">> Processing input...\n", delay=0.02)
    time.sleep(0.3)

def main():
    banner()
    valid_choices = {'1', '2', '3', '4', '5', '6', '7'}

    while True:
        menu()
        choice = input(GREEN + "Choose an option: " + RESET).strip()

        if choice not in valid_choices:
            typewriter("Invalid choice. Try again.\n", delay=0.01)
            continue

        if choice == '7':
            typewriter("Sealing PandoraBox... For now... Goodbye, agent.\n", delay=0.02)
            break

        if choice == '6':
            typewriter("Select hash type to brute force:\n1. SHA256\n2. MD5\n", delay=0.01)
            hash_choice = input(GREEN + "Enter number: " + RESET).strip()

            if hash_choice == '1':
                hash_type = "sha256"
            elif hash_choice == '2':
                hash_type = "md5"
            else:
                typewriter("Invalid hash type choice. Try again.\n", delay=0.01)
                continue

            target = input(GREEN + f"Enter {hash_type.upper()} hash to crack: " + RESET).strip()

            try:
                wordlist = load_wordlist()
            except FileNotFoundError as e:
                fastprint(f"Error: {e}")
                continue

            typewriter(f"Attempting {len(wordlist)} passwords...\n", delay=0.01)
            start = time.time()

            if hash_type == "sha256":
                found = brute_force_sha256(target, wordlist)
            else:
                found = brute_force_md5(target, wordlist)

            end = time.time()

            if found:
                fastprint(f"\nPassword found: {found}")
            else:
                fastprint("\nPassword not found in list.")

            fastprint(f"Completed in {end - start:.2f} seconds\n")
            continue

        # General tools
        text = input(GREEN + "Enter text: " + RESET)

        operation_map = {
            '1': ('Base64 Encode', base64_encode),
            '2': ('Base64 Decode', base64_decode),
            '3': ('Caesar Cipher', caesar_cipher),
            '4': ('Reverse Text', reverse_text),
            '5': ('SHA256 Hash', sha256_hash),
        }

        operation_name, function = operation_map[choice]
        processing_banner(operation_name)
        result = function(text)
        fastprint("Result:\n")
        typewriter(result, delay=0.002)
        print("\n" + "-" * 40 + "\n")

if __name__ == "__main__":
    main()