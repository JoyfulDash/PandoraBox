import hashlib
import urllib.request
import os

def load_wordlist(filename="10k-most-common.txt", url=None):
    if not os.path.exists(filename):
        if url:
            print("Wordlist not found locally. Downloading from internet...")
            try:
                urllib.request.urlretrieve(url, filename)
                print("Download complete.")
            except Exception as e:
                raise FileNotFoundError(f"Could not download wordlist: {e}")
        else:
            raise FileNotFoundError(f"Wordlist '{filename}' not found and no URL provided.")
    
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        return [line.strip() for line in file.readlines()]

def brute_force_md5(target_hash, wordlist):
    for word in wordlist:
        hashed = hashlib.md5(word.encode()).hexdigest()
        if hashed == target_hash:
            return word
    return None

def brute_force_sha256(target_hash, wordlist):
    for word in wordlist:
        hashed = hashlib.sha256(word.encode()).hexdigest()
        if hashed == target_hash:
            return word
    return None
