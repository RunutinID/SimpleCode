# RemoveBackground

## Deskripsi
Proyek RemoveBackground adalah skrip Python sederhana yang menggunakan pustaka `rembg` untuk menghapus latar belakang dari gambar. Skrip ini membaca gambar, mengonversinya menjadi array NumPy, dan kemudian menghapus latar belakang menggunakan pustaka `rembg`. Hasilnya disimpan sebagai gambar baru tanpa latar belakang.

## Instalasi
1. Pastikan Anda telah menginstal Python di sistem Anda.
2. Install pustaka yang dibutuhkan dengan menjalankan perintah berikut:

   ```bash
   pip install rembg Pillow
   ```

## Penggunaan
1. Gantilah direktori ke tempat Anda menyimpan skrip Python dan gambar yang akan diolah.
2. Buka terminal dan jalankan skrip menggunakan perintah berikut:

   ```bash
   python main.py
   ```

3. Program akan membaca gambar (`nuurr.png`), menghapus latar belakang, dan menyimpan hasilnya sebagai gambar baru (`nuurr-rb.png`).

## Contoh Kode
Berikut adalah contoh kode Python untuk menggunakan RemoveBackground:

```python
import rembg
from PIL import Image
import numpy as np

def remove_background(input_image_path, output_image_path):
    input_image = Image.open(input_image_path)
    input_array = np.array(input_image)
    output_array = rembg.remove(input_array)
    output_image = Image.fromarray(output_array)
    output_image.save(output_image_path)

if __name__ == "__main__":
    input_path = "nuurr.png"
    output_path = "nuurr-rb.png"

    remove_background(input_path, output_path)
```

Pastikan untuk mengganti `nuurr.png` dengan path gambar yang ingin Anda proses dan menyesuaikan nama gambar keluaran sesuai kebutuhan.

---

Selamat menggunakan RemoveBackground! Jika Anda memiliki pertanyaan atau butuh bantuan lebih lanjut, jangan ragu untuk bertanya.