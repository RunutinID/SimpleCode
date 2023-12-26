# OCR menggunakan Tesseract di Manjaro

## Deskripsi
Proyek ini merupakan skrip sederhana untuk melakukan Optical Character Recognition (OCR) menggunakan Tesseract di lingkungan Manjaro Linux. Skrip membaca teks dari sebuah gambar dan mencetak hasilnya.

## Instalasi Tesseract

### Windows
1. Unduh dan instal Tesseract dari [Tesseract GitHub Releases](https://github.com/tesseract-ocr/tesseract/releases).
2. Saat menginstal, pastikan untuk menambahkan Tesseract ke PATH sistem Anda.

### Linux (Arch)
Pastikan Anda telah menginstal Tesseract di sistem Manjaro Anda dengan perintah berikut:

```bash
sudo pacman -S tesseract tesseract-data-eng
```

## Instalasi Pustaka Python
Instal pustaka Python yang dibutuhkan dengan menjalankan perintah:

```bash
pip install pytesseract Pillow
```

## Penggunaan
1. Gantilah direktori ke tempat Anda menyimpan skrip Python dan gambar yang akan di-OCR.

2. Buka terminal dan jalankan skrip menggunakan perintah berikut:

   ```bash
   python main.py
   ```

3. Program akan membaca gambar (`test1.jpg`), melakukan OCR, dan mencetak hasilnya.

## Contoh Kode
Berikut adalah contoh kode Python untuk melakukan OCR menggunakan Tesseract di Manjaro:

```python
import pytesseract
from PIL import Image

# Sesuaikan dengan path instalasi Tesseract di Manjaro
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def perform_ocr(image_path):
    # Buka gambar menggunakan PIL
    img = Image.open(image_path)

    # Lakukan OCR pada gambar
    text = pytesseract.image_to_string(img)

    # Cetak hasil OCR
    print("Hasil OCR:")
    print(text)

if __name__ == "__main__":
    image_path = "test1.jpg"  # Ganti dengan path gambar yang ingin di-OCR

    perform_ocr(image_path)
```

Pastikan untuk mengganti `test1.jpg` dengan path gambar yang ingin Anda proses.

---

Selamat menggunakan Tesseract OCR. 
Jika Anda memiliki pertanyaan atau mengalami masalah, jangan ragu untuk bertanya.