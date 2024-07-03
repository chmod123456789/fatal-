from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def write_key_to_file(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(key_filename):
    return open(key_filename, 'rb').read()

def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    with open(filename + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    os.remove(filename)  # Opsional: Hapus file asli setelah dienkripsi

if __name__ == "__main__":
    key = generate_key()
    write_key_to_file(key, 'encryption.key')  # Simpan kunci dengan aman
    key = load_key('encryption.key')

    file_to_encrypt = 'PUSAT_DATA_NASIONAL.txt'  # Ganti dengan nama file yang ingin Anda enkripsi
    encrypt_file(file_to_encrypt, key)
