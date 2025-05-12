# 1. Impor library
from ultralytics import YOLO
import cv2

# --- ALUR EKSEKUSI PROGRAM ---

# 2. Muat Model YOLO untuk Segmentasi
# Model akan diunduh otomatis jika belum ada (membutuhkan internet).
# Pastikan Anda menggunakan model segmentasi yang sesuai (misalnya, yolo11n-seg.pt).
# Anda dapat menemukan model YOLOv11 di: https://docs.ultralytics.com/models/yolo11/
model = YOLO('models/yolo11n-seg.pt') # Ganti dengan nama model segmentasi YOLOv11 Anda jika berbeda

# 3. Tentukan Sumber Input
# Menggunakan URL gambar sebagai input untuk segmentasi.
source_input = 'https://ultralytics.com/images/bus.jpg'
# Alternatif: gambar lokal 'path/to/image.jpg' atau webcam `0`.

# 4. Lakukan Prediksi Segmentasi Objek dan Simpan Hasil
# Menjalankan prediksi segmentasi pada 'source_input'.
# - `conf=0.25`: Ambang batas kepercayaan deteksi objek sebelum segmentasi.
# - `save=True`: Menyimpan gambar hasil anotasi (dengan masker segmentasi).
# - `project='output_segmentation'`: Menyimpan hasil dalam direktori 'output_segmentation'.
# - `name='run_seg'`: Membuat subdirektori 'run_seg' (atau 'run_seg2', dst.) di dalam 'output_segmentation'.
results = model.predict(
    source=source_input,
    conf=0.25,
    save=True,
    project='output_segmentation', # Direktori output diubah untuk membedakan dengan deteksi
    name='run_seg' # Nama run diubah untuk membedakan
)
# 'results' berisi list objek hasil prediksi, termasuk masker segmentasi.
# Gambar anotasi disimpan di 'output_segmentation/run_segX/'.

# 5. Proses dan Tampilkan Hasil Segmentasi
# Mengambil hasil prediksi pertama (karena inputnya satu gambar).
if not results:
    print("Tidak ada hasil prediksi segmentasi. Keluar.")
    exit()
result = results[0]

# 5.a. Dapatkan Gambar dengan Anotasi Segmentasi
# `result.plot()` menghasilkan gambar NumPy (BGR) dengan masker segmentasi yang digambar.
annotated_image = result.plot()

# 5.b. Tampilkan Gambar Hasil Segmentasi
# Menampilkan gambar beranotasi menggunakan OpenCV.
cv2.imshow("YOLO Object Segmentation Result", annotated_image)
cv2.waitKey(0) # Menunggu tombol ditekan untuk menutup jendela gambar.

# 6. Bersihkan
# Menutup semua jendela OpenCV.
cv2.destroyAllWindows()

# Selesai. Hasil disimpan dan telah ditampilkan.
print(f"Proses segmentasi selesai. Hasil disimpan di: {result.save_dir}")