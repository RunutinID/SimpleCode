# Pembuat PDF dengan WeasyPrint

Script ini digunakan untuk membuat dokumen PDF menggunakan library WeasyPrint. Contoh ini menunjukkan cara membuat file README.md untuk suatu proyek hipotetis yang disebut "YouTube MP3 Downloader."

## Persyaratan
- Python 3.9.18
- WeasyPrint 52.5

Anda dapat menginstal dependensi yang diperlukan dengan menjalankan perintah berikut:

```bash
pip install WeasyPrint
```

## Penggunaan

1. Clone repositori ini atau unduh file `main.py` dan pastikan Anda telah menginstal dependensi yang diperlukan.

2. Jalankan skrip dengan menjalankan perintah berikut:

    ```bash
    python main.py
    ```

3. Skrip akan meminta Anda untuk memasukkan konten berupa *`Judul`* dan *`Isi`*.

4. Setelah Anda memberikan konten, skrip akan membuat file PDF dengan nama *`{Judul}.pdf`* berisi informasi yang diformat dengan baik.