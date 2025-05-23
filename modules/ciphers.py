def caesar_cipher(text, shift=3):
    result = ''
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def reverse_text(text):
    return text[::-1]
