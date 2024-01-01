# YouTube MP3 Downloader

Program ini merupakan script sederhana untuk mengunduh audio dari video YouTube dan mengonversinya ke format MP3. Program ini menggunakan pustaka `pytube` untuk mengunduh video dan `pydub` untuk mengonversi audio.

## Diudi menggunakan
- `Python 3.9.18`
- Pustaka `pytube 15.0.0` 
- Pustaka `pydub 0.25.1`

Anda dapat menginstal persyaratan tersebut dengan menjalankan perintah berikut:

```bash
pip install pytube pydub
```

## Cara Menggunakan

1. Clone repositori ini atau unduh file `main.py` dan pastikan Anda memenuhi persyaratan di atas.
2. Jalankan program dengan menjalankan perintah:

    ```bash
    python main.py
    ```

3. Program akan meminta Anda untuk memasukkan URL YouTube. Masukkan URL video yang ingin Anda unduh, atau ketik 'exit' untuk keluar.

4. Program akan mengunduh video, mengonversi audio ke format MP3, dan menyimpannya di direktori saat ini dengan nama berdasarkan judul video.

## Catatan Penting
- Pengunduhan video dari YouTube dapat melanggar kebijakan layanan YouTube. Pastikan Anda mematuhi ketentuan layanan YouTube dan hukum setempat saat menggunakan skrip ini.
- Jika Anda mengalami masalah, pastikan Anda memiliki koneksi internet yang baik dan semua persyaratan terpenuhi.