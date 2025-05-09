Tentu! Berikut adalah **README** yang telah diperbarui dengan nama **"ComChating"** seperti yang kamu inginkan.

---

# ComChating - Ransomware Decryptor

**ComChating** adalah alat dekripsi ransomware berbasis **Python** yang memungkinkan kamu untuk mendekripsi file yang terenkripsi menggunakan **AES**. Alat ini dirancang untuk mempermudah proses dekripsi dengan meminta input interaktif di **CLI** (Command Line Interface).

### **Fitur**:

* **Dekripsi File AES** menggunakan kunci simetris yang diberikan.
* **Mudah digunakan** dengan antarmuka berbasis teks di CLI.
* **Mendukung Linux, macOS, dan Windows**.

---

## **Prasyarat**

Sebelum mulai, pastikan kamu memiliki hal berikut:

* **Python 3.6+** terinstal di sistem kamu.
* **pip** untuk mengelola paket Python.
* **pycryptodome** (pustaka Python untuk enkripsi AES).

---

## **Instalasi**

### **1. Instal Python dan pip**

Jika kamu belum memiliki **Python** atau **pip** terinstal, berikut adalah cara untuk menginstalnya:

* **Linux (Ubuntu/Debian)**:

  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```

* **macOS**:
  Install Homebrew terlebih dahulu jika belum ada:

  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  brew install python
  ```

* **Windows**:
  Unduh dan instal Python 3 dari [python.org](https://www.python.org/downloads/), pastikan untuk memilih opsi **Add Python to PATH** saat instalasi.

---

### **2. Membuat Virtual Environment (Disarankan)**

Untuk memastikan instalasi Python yang bersih dan terisolasi, kami sangat menyarankan untuk menggunakan **virtual environment**. Ikuti langkah-langkah di bawah ini untuk membuat dan mengaktifkan virtual environment.

1. **Instal `python3-venv`** (jika belum terpasang):

   * **Linux (Ubuntu/Debian)**:

     ```bash
     sudo apt install python3-venv
     ```
   * **macOS** dan **Windows**: Virtual environment sudah terinstal secara default di Python 3.

2. **Buat virtual environment**:
   Di direktori proyek kamu, jalankan:

   ```bash
   python3 -m venv comchating-env
   ```

3. **Aktifkan virtual environment**:

   * **Linux/macOS**:

     ```bash
     source comchating-env/bin/activate
     ```
   * **Windows**:

     ```bash
     comchating-env\Scripts\activate
     ```

4. **Pastikan virtual environment aktif**:
   Setelah aktivasi, prompt terminal kamu akan berubah menunjukkan bahwa kamu berada di dalam virtual environment.

---

### **3. Instal pycryptodome**

Setelah virtual environment aktif, instal **pycryptodome**, pustaka Python yang digunakan untuk enkripsi dan dekripsi:

```bash
pip install pycryptodome
```

---

### **4. Mengunduh dan Menjalankan ComChating**

1. **Clone Repository**:
   Jika belum meng-clone repository ini, lakukan dengan perintah berikut:

   ```bash
   git clone https://github.com/acongkuy/ComChating---Ransomware-Decryptor
   cd comchating
   ```

2. **Jalankan ComChating**:
   Setelah berada di dalam direktori proyek, jalankan alat dekripsi dengan perintah:

   ```bash
   python comchating.py
   ```

---

## **Penggunaan**

Setelah menjalankan perintah di atas, kamu akan diminta untuk memberikan input sebagai berikut:

### **Input yang diperlukan**:

1. **Enter the path of the encrypted file**:

   * Masukkan path lengkap ke **file terenkripsi** yang ingin kamu dekripsi.
   * Misalnya: `/path/to/encrypted/file` (Linux/macOS) atau `C:\Users\Username\Downloads\encrypted_file.txt` (Windows).

2. **Enter the path to save the decrypted file**:

   * Masukkan path lengkap untuk **menyimpan file yang didekripsi**.
   * Misalnya: `/path/to/decrypted/file` (Linux/macOS) atau `C:\Users\Username\Downloads\decrypted_file.txt` (Windows).

3. **Enter the decryption key**:

   * Masukkan **kunci dekripsi** yang digunakan saat ransomware mengenkripsi file.
   * Pastikan untuk menggunakan kunci yang benar.

Contoh output:

```bash
   _____                 _____ _           _     _             
  / ____|               / ____| |         | |   (_)            
 | |     ___  _ __ ___ | |    | |__   __ _| |_  _ _ __   __ _ 
 | |    / _ \| '_ ` _ \| |    | '_ \ / _` | __| | | '_ \ / _` |
 | |___| (_) | | | | | | |____| | | | (_| | |_| | | | | | (_| |
  \_____\___/|_| |_| |_|\_____|_| |_|\__,_|\__|_| |_| |_|\__, |
                                                          __/ |
                                                         |___/ 

Welcome to ComChating Ransomware Decryptor Tool!

Enter the path of the encrypted file: /path/to/encrypted/file
Enter the path to save the decrypted file: /path/to/decrypted/file
Enter the decryption key: my_decryption_key

Decryption complete! The decrypted file is saved at: /path/to/decrypted/file
```

---

## **FAQ (Pertanyaan yang Sering Diajukan)**

### **Q1: Apa itu ComChating?**

ComChating adalah alat untuk mendekripsi file yang terenkripsi oleh ransomware yang menggunakan algoritma **AES**.

### **Q2: Bagaimana jika kunci dekripsi saya salah?**

Jika kunci dekripsi salah, dekripsi akan gagal dan pesan kesalahan akan ditampilkan.

### **Q3: Apakah ComChating bekerja di semua sistem operasi?**

ComChating bekerja di **Linux**, **macOS**, dan **Windows** asalkan **Python 3.6+** terinstal.

---

## **Menyumbang**

Jika kamu ingin menyumbang ke pengembangan ComChating, fork repo ini dan buat pull request dengan perubahan yang diinginkan. Kami menyambut kontribusi dan perbaikan bug.

---

**Terima kasih telah menggunakan ComChating!**

---

### **Kesimpulan:**

Ini adalah tutorial lengkap untuk membuat **tools ComChating** di CLI, termasuk cara instalasi dan penggunaannya. Semua langkah ini dioptimalkan untuk lingkungan yang bersih menggunakan **virtual environment** agar menghindari konflik dengan sistem Python yang sudah ada.

Jika ada pertanyaan lebih lanjut atau masalah dengan penggunaan tools, silakan beri tahu saya!

---

Ini adalah versi **README** yang disesuaikan dengan nama **ComChating** dan instruksi yang jelas mengenai instalasi dan penggunaan tools dekripsi ransomware ini. Jika ada tambahan atau perubahan lebih lanjut yang diperlukan, beri tahu saya!
