# OCR menggunakan EasyOCR

## Instalasi
Pastikan Anda telah menginstal Python dan pip di sistem Anda. Kemudian, jalankan perintah berikut untuk menginstal pustaka yang dibutuhkan:

```bash
pip install easyocr
```

## Teori Dasar
EasyOCR adalah pustaka pengenalan karakter optik (OCR) sederhana dan mudah digunakan. Pustaka ini memanfaatkan model deep learning untuk mengenali teks dalam gambar. Anda dapat menggunakan EasyOCR untuk membaca teks dalam berbagai bahasa.

## Penggunaan
1. Ganti direktori ke tempat Anda menyimpan skrip Python dan gambar yang akan di-OCR.
2. Buka terminal dan jalankan skrip menggunakan perintah berikut:

   ```bash
   python main.py
   ```
3. Program akan membaca gambar (`path_to_image.png`) dan mencetak hasilnya.

## Contoh Kode
Berikut adalah contoh kode Python untuk menggunakan EasyOCR:

```python
import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('path_to_image.jpg', detail=0)
print(result)
```

Pastikan untuk mengganti `path_to_image.png` dengan path gambar yang ingin Anda proses.

---

Selamat menggunakan EasyOCR! Jika Anda mengalami masalah atau memiliki pertanyaan lebih lanjut, jangan ragu untuk menghubungi kami😄
