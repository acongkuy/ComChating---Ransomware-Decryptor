import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Header besar untuk CrypChunsky
print("""
   _____                 _____ _           _     _             
  / ____|               / ____| |         | |   (_)            
 | |     ___  _ __ ___ | |    | |__   __ _| |_  _ _ __   __ _ 
 | |    / _ \| '_ ` _ \| |    | '_ \ / _` | __| | | '_ \ / _` |
 | |___| (_) | | | | | | |____| | | | (_| | |_| | | | | | (_| |
  \_____\___/|_| |_| |_|\_____|_| |_|\__,_|\__|_| |_| |_|\__, |
                                                          __/ |
                                                         |___/ 
""")

# Fungsi dekripsi AES dengan input dari pengguna
def decrypt_file(encrypted_file_path, decrypted_file_path, key):
    # Membuat kunci 32 byte dari input
    key = hashlib.sha256(key.encode('utf-8')).digest()

    # Membaca file terenkripsi
    with open(encrypted_file_path, 'rb') as enc_file:
        encrypted_data = enc_file.read()

    # Mengambil IV yang ada di bagian depan file
    iv = encrypted_data[:16]  # Ambil 16 byte pertama sebagai IV
    encrypted_data = encrypted_data[16:]  # Sisanya adalah data terenkripsi

    # Inisialisasi cipher dengan AES dan IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Dekripsi data
    try:
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    except ValueError:
        print("Decryption failed. The data may be corrupted or the key is wrong.")
        return

    # Menyimpan data yang sudah didekripsi
    with open(decrypted_file_path, 'wb') as dec_file:
        dec_file.write(decrypted_data)

    print(f"Decryption complete! The decrypted file is saved at: {decrypted_file_path}")

# Fungsi utama yang meminta input dari pengguna di CLI
def main():
    print("Welcome to CrypChunsky Ransomware Decryptor Tool!\n")

    # Meminta input dari pengguna
    encrypted_file_path = input("Enter the path of the encrypted file: ").strip()
    decrypted_file_path = input("Enter the path to save the decrypted file: ").strip()
    key = input("Enter the decryption key: ").strip()

    # Memeriksa apakah file terenkripsi ada
    if not os.path.exists(encrypted_file_path):
        print(f"Error: The encrypted file at {encrypted_file_path} does not exist.")
        return

    # Menjalankan dekripsi
    decrypt_file(encrypted_file_path, decrypted_file_path, key)

# Menjalankan aplikasi
if __name__ == "__main__":
    main()
