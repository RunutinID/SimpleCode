# 1. Impor library
from ultralytics import YOLO
import cv2

# --- ALUR EKSEKUSI PROGRAM ---

# 2. Muat Model YOLO untuk OBB
# Pastikan 'models/yolo11n-obb.pt' adalah path ke model YOLOv11 yang telah dilatih untuk OBB.
# Model akan diunduh otomatis jika merupakan model resmi Ultralytics dan belum ada.
# Jika ini adalah model kustom Anda, pastikan path-nya benar.
# Contoh nama model OBB: 'yolo11n-obb.pt' atau path ke model OBB kustom Anda.
model_path = 'models/yolo11n-obb.pt' # GANTI DENGAN PATH MODEL OBB ANDA
print(f"Memuat model OBB dari: {model_path}")
model = YOLO(model_path)
print("Model OBB berhasil dimuat.")

# 3. Tentukan Sumber Input
# Menggunakan URL gambar sebagai input untuk deteksi OBB.
source_input = 'https://ultralytics.com/images/boats.jpg' # Anda mungkin ingin menggunakan gambar yang lebih cocok untuk OBB
# Alternatif: gambar lokal 'path/to/image.jpg'.
print(f"Sumber input diatur ke: {source_input}")

# 4. Lakukan Prediksi OBB dan Simpan Hasil
# Menjalankan prediksi OBB pada 'source_input'.
# - `conf=0.25`: Ambang batas kepercayaan deteksi.
# - `save=True`: Menyimpan gambar hasil anotasi OBB.
# - `project='output_obb'`: Menyimpan hasil dalam direktori 'output_obb'.
# - `name='run_obb'`: Membuat subdirektori 'run_obb' (atau 'run_obb2', dst.) di dalam 'output_obb'.
print("Melakukan prediksi OBB...")
results = model.predict(
    source=source_input,
    conf=0.25,
    save=True,
    project='output_obb', # Direktori output diubah untuk OBB
    name='run_obb'         # Nama run diubah untuk OBB
)
# 'results' berisi list objek hasil prediksi OBB. Gambar anotasi disimpan di 'output_obb/run_obbX/'.
print("Prediksi OBB selesai.")

# 5. Proses dan Tampilkan Hasil
# Mengambil hasil prediksi pertama (karena inputnya satu gambar).
if not results:
    print("Tidak ada hasil prediksi OBB. Keluar.")
    exit()
result = results[0] # Mengambil hasil pertama dari list

# 5.a. Dapatkan Gambar dengan Anotasi OBB
# `result.plot()` menghasilkan gambar NumPy (BGR) dengan deteksi OBB yang digambar.
print("Membuat gambar dengan anotasi OBB...")
annotated_image = result.plot()

# 5.b. Tampilkan Gambar Hasil Deteksi OBB
# Menampilkan gambar beranotasi OBB menggunakan OpenCV.
print("Menampilkan gambar hasil deteksi OBB...")
cv2.imshow("YOLO OBB Detection Result", annotated_image)
cv2.waitKey(0) # Menunggu tombol ditekan untuk menutup jendela gambar.

# 6. Bersihkan
# Menutup semua jendela OpenCV.
cv2.destroyAllWindows()

# Selesai. Hasil disimpan dan telah ditampilkan.
# Path penyimpanan juga bisa diakses melalui atribut `save_dir` dari objek result.
save_directory = result.save_dir
print(f"Proses selesai. Hasil OBB disimpan di: {save_directory}")