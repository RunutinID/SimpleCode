# 1. Impor library
from ultralytics import YOLO
import cv2

# --- ALUR EKSEKUSI PROGRAM ---

# 2. Muat Model YOLO
# Model akan diunduh otomatis jika belum ada (membutuhkan internet).
model = YOLO('models/yolo11n.pt')

# 3. Tentukan Sumber Input
# Menggunakan URL gambar sebagai input untuk deteksi.
source_input = '0'
# Alternatif: gambar lokal 'path/to/image.jpg' atau webcam `0`.

# 4. Lakukan Prediksi Objek dan Simpan Hasil
# Menjalankan prediksi pada 'source_input'.
# - `conf=0.25`: Ambang batas kepercayaan deteksi.
# - `save=True`: Menyimpan gambar hasil anotasi.
# - `project='output'`: Menyimpan hasil dalam direktori 'output'.
# - `name='run'`: Membuat subdirektori 'run' (atau 'run2', 'run3', dst.) di dalam 'output'.
results = model.predict(
    source=source_input,
    conf=0.25,
    save=True,
    project='output',
    name='run'
)
# 'results' berisi list objek hasil prediksi. Gambar anotasi disimpan di 'output/runX/'.

# 5. Proses dan Tampilkan Hasil
# Mengambil hasil prediksi pertama (karena inputnya satu gambar).
if not results:
    print("Tidak ada hasil prediksi. Keluar.")
    exit()
result = results[0]

# 5.a. Dapatkan Gambar dengan Anotasi
# `result.plot()` menghasilkan gambar NumPy (BGR) dengan deteksi yang digambar.
annotated_image = result.plot()

# 5.b. Tampilkan Gambar Hasil Deteksi
# Menampilkan gambar beranotasi menggunakan OpenCV.
cv2.imshow("YOLO Object Detection Result", annotated_image)
cv2.waitKey(0) # Menunggu tombol ditekan untuk menutup jendela gambar.

# 6. Bersihkan
# Menutup semua jendela OpenCV.
cv2.destroyAllWindows()

# Selesai. Hasil disimpan dan telah ditampilkan.
print(f"Proses selesai. Hasil disimpan di: {result.save_dir}")