import time
import sys
from modules.encoders import base64_encode, base64_decode
from modules.ciphers import caesar_cipher, reverse_text
from modules.hashers import sha256_hash

# === MATRIX STYLE SETTINGS ===
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
6. Exit
""", delay=0.005)

def processing_banner(operation_name):
    typewriter(f"\n>> Opening module: {operation_name}...", delay=0.02)
    time.sleep(0.3)
    typewriter(">> Processing input...\n", delay=0.02)
    time.sleep(0.3)

def main():
    banner()
    while True:
        menu()
        choice = input(GREEN + "Choose an option: " + RESET).strip()

        if choice == '6':
            typewriter("Sealing PandoraBox... For now... Goodbye, agent.\n", delay=0.02)
            break

        text = input(GREEN + "Enter text: " + RESET)

        operation_map = {
            '1': ('Base64 Encode', base64_encode),
            '2': ('Base64 Decode', base64_decode),
            '3': ('Caesar Cipher', caesar_cipher),
            '4': ('Reverse Text', reverse_text),
            '5': ('SHA256 Hash', sha256_hash),
        }

        if choice in operation_map:
            operation_name, function = operation_map[choice]
            processing_banner(operation_name)
            result = function(text)
            fastprint("✦ Result:")
            print()
            typewriter(result, delay=0.002)
            print("\n" + "-" * 40 + "\n")
        else:
            typewriter("Invalid choice. Try again.\n", delay=0.01)

if __name__ == "__main__":
    main()