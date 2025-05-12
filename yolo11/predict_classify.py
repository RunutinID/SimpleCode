# 1. Impor library
from ultralytics import YOLO
import cv2

# --- ALUR EKSEKUSI PROGRAM ---

# 2. Muat Model YOLO untuk Klasifikasi
# Model akan diunduh otomatis jika menggunakan nama model resmi Ultralytics yang mendukung klasifikasi dan belum ada (membutuhkan internet).
# GANTI 'yolo11n-cls.pt' dengan path ke model klasifikasi YOLOv11 Anda.
# Model klasifikasi biasanya memiliki akhiran seperti '-cls.pt'.
# Jika model 'yolo11n.pt' dari kode asli adalah untuk deteksi, Anda memerlukan file model yang berbeda yang telah dilatih untuk klasifikasi menggunakan arsitektur YOLOv11.
# Contoh: model = YOLO('yolo11n-cls.pt') atau model = YOLO('path/to/your/yolo11_classification_model.pt')
try:
    model = YOLO('models/yolo11n-cls.pt') # Ganti dengan model klasifikasi YOLOv11 Anda
except Exception as e:
    print(f"Error saat memuat model: {e}")
    print("Pastikan Anda memiliki model klasifikasi YOLOv11 yang benar (misalnya, 'yolo11n-cls.pt')")
    print("Atau ganti dengan path ke model kustom Anda yang dilatih untuk klasifikasi dengan YOLOv11.")
    exit()

# 3. Tentukan Sumber Input
# Menggunakan URL gambar sebagai input untuk klasifikasi.
source_input = 'https://ultralytics.com/images/bus.jpg' # Contoh gambar, bisa diganti dengan gambar lain
# Alternatif: gambar lokal 'path/to/image.jpg' atau webcam `0`.

# 4. Lakukan Prediksi Kelas dan Simpan Hasil
# Menjalankan prediksi klasifikasi pada 'source_input'.
# - `conf`: Untuk tugas klasifikasi, parameter `conf` pada `predict()` umumnya kurang berpengaruh
#            dibandingkan pada deteksi objek. Hasil utama adalah probabilitas untuk setiap kelas.
# - `save=True`: Menyimpan gambar input dengan label kelas hasil prediksi teratas.
# - `project='output_classification'`: Menyimpan hasil dalam direktori 'output_classification'.
# - `name='run_classify'`: Membuat subdirektori 'run_classify' (atau 'run_classify2', dst.) di dalam 'output_classification'.
results = model.predict(
    source=source_input,
    conf=0.25,  # Ambang kepercayaan, mungkin kurang relevan untuk klasifikasi murni
    save=True,
    project='output_classification', # Disarankan menggunakan direktori berbeda untuk output klasifikasi
    name='run_classify'
)
# 'results' berisi list objek hasil prediksi klasifikasi.
# Gambar dengan label kelas terprediksi disimpan di 'output_classification/run_classifyX/'.

# 5. Proses dan Tampilkan Hasil Klasifikasi
# Mengambil hasil prediksi pertama (karena inputnya satu gambar).
if not results:
    print("Tidak ada hasil prediksi. Keluar.")
    exit()

# result adalah objek tunggal dari list results jika hanya satu gambar diproses
result = results[0]

# 5.a. Dapatkan Informasi Kelas Terprediksi
# result.names adalah kamus yang memetakan indeks kelas ke nama kelas (misalnya, {0: 'kucing', 1: 'anjing'})
# result.probs adalah objek yang menyimpan probabilitas; result.probs.top1 adalah indeks kelas dengan probabilitas tertinggi
# result.probs.top1conf adalah nilai kepercayaan (probabilitas) dari kelas dengan probabilitas tertinggi (top1)
predicted_class_name = "Tidak Diketahui"
confidence_score = 0.0

if result.probs is not None:
    top1_index = result.probs.top1 # Indeks kelas teratas
    confidence_score = result.probs.top1conf.item() # Kepercayaan kelas teratas, dikonversi ke float
    predicted_class_name = result.names[top1_index] # Nama kelas teratas

    print(f"--- Hasil Klasifikasi ---")
    print(f"Gambar Input: {source_input}")
    print(f"Kelas Terprediksi: {predicted_class_name}")
    print(f"Kepercayaan: {confidence_score:.4f}")

    # Opsional: Tampilkan 5 kelas teratas jika diperlukan
    # top5_indices = result.probs.top5
    # top5_confidences = result.probs.top5conf.tolist()
    # print("\nTop 5 Prediksi:")
    # for i, index in enumerate(top5_indices):
    #     print(f"- {result.names[index]}: {top5_confidences[i]:.4f}")
else:
    print("Tidak dapat menemukan probabilitas kelas dalam hasil. Pastikan model adalah model klasifikasi.")
    # Jika tidak ada probabilitas, mungkin model atau task tidak dikonfigurasi dengan benar untuk klasifikasi.

# 5.b. Dapatkan Gambar dengan Anotasi Kelas
# `result.plot()` menghasilkan gambar NumPy (BGR) dengan label kelas yang diprediksi digambar di atasnya.
annotated_image = result.plot() # Ini akan menggambar nama kelas terprediksi pada gambar

# 5.c. Tampilkan Gambar Hasil Klasifikasi
# Menampilkan gambar beranotasi menggunakan OpenCV.
cv2.imshow("YOLO Classification Result", annotated_image)
cv2.waitKey(0) # Menunggu tombol ditekan untuk menutup jendela gambar.

# 6. Bersihkan
# Menutup semua jendela OpenCV.
cv2.destroyAllWindows()

# Selesai. Hasil disimpan dan telah ditampilkan.
# result.save_dir akan berisi path ke direktori tempat gambar anotasi disimpan jika save=True
if hasattr(result, 'save_dir') and result.save_dir:
    print(f"Proses selesai. Hasil disimpan di: {result.save_dir}")
else:
    # Fallback jika save_dir tidak ada, meskipun dengan save=True seharusnya ada.
    print(f"Proses selesai. Gambar anotasi disimpan di direktori '{result.path}' (jika `save=True`). Cek 'output_classification/run_classifyX/'.")