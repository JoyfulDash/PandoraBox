import sys
import hashlib
import os
import urllib.request

WORDLIST_FILE = "10k-most-common.txt"
WORDLIST_URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt"

def load_wordlist(filename=WORDLIST_FILE, fallback_url=WORDLIST_URL):
    """
    Load a wordlist from the given filename in the module directory.
    If not found locally and fallback_url is provided, download it.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)

    if not os.path.isfile(filepath):
        if fallback_url:
            try:
                print(f"Downloading wordlist from {fallback_url}...")
                urllib.request.urlretrieve(fallback_url, filepath)
                print("Download complete.")
            except Exception as e:
                raise FileNotFoundError(f"Failed to download wordlist: {e}")
        else:
            raise FileNotFoundError(f"Wordlist '{filename}' not found and no URL provided.")

    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def brute_force_sha256(target_hash, wordlist):
    total = len(wordlist)
    for i, password in enumerate(wordlist, 1):
        sys.stdout.write(f"\rTrying password {i}/{total}: {password}   ")
        sys.stdout.flush()
        if hashlib.sha256(password.encode()).hexdigest() == target_hash:
            print(f"\nPassword found after trying {i} passwords!")
            return password
    print("\nPassword not found in list.")
    return None

def brute_force_md5(target_hash, wordlist):
    total = len(wordlist)
    for i, password in enumerate(wordlist, 1):
        sys.stdout.write(f"\rTrying password {i}/{total}: {password}   ")
        sys.stdout.flush()
        if hashlib.md5(password.encode()).hexdigest() == target_hash:
            print(f"\nPassword found after trying {i} passwords!")
            return password
    print("\nPassword not found in list.")
    return None