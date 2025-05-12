# 1. Impor library
from ultralytics import YOLO
import cv2

# --- ALUR EKSEKUSI PROGRAM ---

# 2. Muat Model YOLO untuk Estimasi Pose
# Model akan diunduh otomatis jika belum ada dan tersedia di repositori Ultralytics (membutuhkan internet).
# Pastikan Anda memiliki file model 'yolo11n-pose.pt' atau nama model pose YOLOv11 yang sesuai.
model = YOLO('models/yolo11n-pose.pt') # Model diubah ke model estimasi pose

# 3. Tentukan Sumber Input
# Menggunakan URL gambar sebagai input untuk estimasi pose.
# Untuk hasil terbaik estimasi pose, gunakan gambar yang berisi orang.
source_input = '0' # Anda mungkin ingin mengganti ini dengan gambar yang berisi orang
# Alternatif: gambar lokal 'path/to/image_with_person.jpg' atau webcam `0`.

# 4. Lakukan Prediksi Pose dan Simpan Hasil
# Menjalankan prediksi pose pada 'source_input'.
# - `conf=0.25`: Ambang batas kepercayaan deteksi pose.
# - `save=True`: Menyimpan gambar hasil anotasi pose.
# - `project='output_pose'`: Menyimpan hasil dalam direktori 'output_pose'.
# - `name='run_pose'`: Membuat subdirektori 'run_pose' (atau 'run_pose2', dst.) di dalam 'output_pose'.
results = model.predict(
    source=source_input,
    conf=0.25,
    save=True,
    project='output_pose', # Direktori proyek diubah untuk membedakan dengan output deteksi objek
    name='run_pose'       # Nama run diubah
)
# 'results' berisi list objek hasil prediksi pose. Gambar anotasi disimpan di 'output_pose/run_poseX/'.

# 5. Proses dan Tampilkan Hasil
# Mengambil hasil prediksi pose pertama (karena inputnya satu gambar).
if not results:
    print("Tidak ada hasil prediksi pose. Keluar.")
    exit()
result = results[0]

# 5.a. Dapatkan Gambar dengan Anotasi Pose
# `result.plot()` menghasilkan gambar NumPy (BGR) dengan pose (kerangka dan keypoints) yang digambar.
annotated_image_pose = result.plot()

# 5.b. Tampilkan Gambar Hasil Estimasi Pose
# Menampilkan gambar beranotasi pose menggunakan OpenCV.
cv2.imshow("YOLO Pose Estimation Result", annotated_image_pose)
cv2.waitKey(0) # Menunggu tombol ditekan untuk menutup jendela gambar.

# 6. Bersihkan
# Menutup semua jendela OpenCV.
cv2.destroyAllWindows()

# Selesai. Hasil disimpan dan telah ditampilkan.
# result.save_dir akan berisi path tempat gambar dan hasil lainnya disimpan.
print(f"Proses estimasi pose selesai. Hasil disimpan di: {result.save_dir}")