import os
import getpass
import hashlib
import py7zr
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag
import argparse

def derive_key(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

def compress_file(file_path: str) -> str:
    compressed_path = file_path + '.arc'
    with py7zr.SevenZipFile(compressed_path, 'w') as archive:
        archive.write(file_path, os.path.basename(file_path))
    os.remove(file_path)
    return compressed_path

def decompress_file(file_path: str) -> str:
    decompressed_path = file_path[:-4]  # Remove '.arc' extension
    with py7zr.SevenZipFile(file_path, 'r') as archive:
        archive.extractall(path=os.path.dirname(decompressed_path))
    os.remove(file_path)
    return decompressed_path

def encrypt_file(file_path: str, password: str) -> str:
    salt, nonce = os.urandom(16), os.urandom(12)
    key = derive_key(password, salt)
    aesgcm = AESGCM(key)
    encrypted_path = file_path + '.enc'
    try:
        with open(file_path, 'rb') as f, open(encrypted_path, 'wb') as out:
            out.write(salt + nonce + aesgcm.encrypt(nonce, f.read(), None))
        os.remove(file_path)
        return encrypted_path
    except Exception as e:
        print(f"Error encrypting file {file_path}: {e}")
        return None

def decrypt_file(file_path: str, password: str) -> str:
    decrypted_path = file_path[:-4]  # Remove '.enc' extension
    try:
        with open(file_path, 'rb') as f:
            salt, nonce, enc_data = f.read(16), f.read(12), f.read()
        key = derive_key(password, salt)
        aesgcm = AESGCM(key)
        with open(decrypted_path, 'wb') as out:
            out.write(aesgcm.decrypt(nonce, enc_data, None))
        os.remove(file_path)
        return decrypted_path
    except InvalidTag:
        print(f"Error: Invalid password or corrupted file: {file_path}")
    except Exception as e:
        print(f"Error decrypting file {file_path}: {e}")
    return None

def process_file(file_path: str, password: str, encrypt: bool):
    if encrypt:
        if not file_path.endswith('.enc'):
            compressed_path = compress_file(file_path)
            if compressed_path:
                encrypt_file(compressed_path, password)
    else:
        if file_path.endswith('.enc'):
            decrypted_path = decrypt_file(file_path, password)
            if decrypted_path:
                decompress_file(decrypted_path)

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt 'proxy-providers.txt'")
    parser.add_argument("action", choices=['e', 'd'], help="e - encrypt, d - decrypt")
    args = parser.parse_args()

    password = getpass.getpass("Enter the password: ")
    file_paths = ['proxy-providers.txt', 'proxy-custom.txt']
    
    for file_path in file_paths:

        if args.action == 'e':
            if os.path.exists(file_path):
                process_file(file_path, password, encrypt=True)
            else:
                print(f"File '{file_path}' does not exist.")
        elif args.action == 'd':
            encrypted_path = file_path + '.arc.enc'
            if os.path.exists(encrypted_path):
                process_file(encrypted_path, password, encrypt=False)
            else:
                print(f"Encrypted file '{encrypted_path}' does not exist.")

if __name__ == "__main__":
    main()