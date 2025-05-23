import sys
import hashlib
import os

def load_wordlist(filename):
    # Get the absolute directory path where this module resides
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)

    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"Password file not found: {filepath}")

    # Read lines, strip whitespace, exclude empty lines
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def brute_force_sha256(target_hash, wordlist):
    total = len(wordlist)
    for i, password in enumerate(wordlist, 1):
        # Print the current password on the same line (overwrites previous)
        sys.stdout.write(f"\rTrying password {i}/{total}: {password}   ")
        sys.stdout.flush()

        # Hash the password and compare to target
        if hashlib.sha256(password.encode()).hexdigest() == target_hash:
            print(f"\nPassword found after trying {i} passwords!")
            return password

    print("\nPassword not found in list.")
    return None

if __name__ == "__main__":
    target_hash = input("Enter SHA256 hash to crack: ").strip()

    try:
        wordlist = load_wordlist("10k-most-common.txt")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)

    found_password = brute_force_sha256(target_hash, wordlist)
    if found_password:
        print(f"Password is: {found_password}")
    else:
        print("Password not found.")
