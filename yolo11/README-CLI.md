# 📘 Panduan Penggunaan YOLO11 dengan Ultralytics CLI

Ultralytics menyediakan antarmuka baris perintah (CLI) yang memudahkan penggunaan model YOLO11 untuk berbagai tugas visi komputer. Dengan perintah `yolo`, Anda dapat melakukan pelatihan, prediksi, validasi, ekspor, dan lainnya langsung dari terminal tanpa perlu menulis kode Python.

---

## 📂 Struktur Perintah Dasar

```bash
yolo [TASK] MODE [ARGS]
```

* **TASK** *(opsional)*: Menentukan jenis tugas visi komputer yang akan dilakukan, seperti deteksi objek (`detect`), segmentasi (`segment`), klasifikasi (`classify`), estimasi pose (`pose`), atau deteksi objek berorientasi (`obb`). Jika tidak ditentukan, Ultralytics akan mencoba menginferensikan tugas berdasarkan nama model.
* **MODE** *(wajib)*: Menentukan mode operasi seperti pelatihan (`train`), validasi (`val`), prediksi (`predict`), ekspor (`export`), pelacakan (`track`), atau benchmarking (`benchmark`).
* **ARGS** *(opsional)*: Pasangan `argumen=nilai` untuk mengonfigurasi perilaku perintah. Ditulis dalam format `arg=val` dan dipisahkan spasi. Hindari `--` atau koma.

### 🔍 Contoh Perintah

```bash
# Melatih model deteksi objek selama 50 epoch
yolo detect train data=dataset.yaml model=yolo11n.pt epochs=50 imgsz=640

# Melakukan prediksi segmentasi
yolo segment predict model=yolo11n-seg.pt source=path/to/image.jpg

# Mengekspor model klasifikasi ke ONNX
yolo export model=yolo11n-cls.pt format=onnx imgsz=224,224
```

### 🧰 Daftar Argumen Umum (`ARGS`)

* `model`: Jalur ke model (contoh: `yolo11n.pt`)
* `data`: File konfigurasi dataset (contoh: `dataset.yaml`)
* `epochs`: Jumlah epoch pelatihan (contoh: `100`)
* `imgsz`: Ukuran gambar (contoh: `640`, `640,480`)
* `batch`: Ukuran batch (contoh: `16`)
* `lr0`: Learning rate awal
* `source`: Jalur input gambar, folder, video, webcam, atau URL
* `conf`: Ambang kepercayaan untuk prediksi (contoh: `0.25`)
* `format`: Format ekspor (`onnx`, `torchscript`, `coreml`, dll.)

---

## 🧠 Task (Tugas)

Menentukan jenis tugas yang akan dijalankan oleh model YOLO11:

* `detect`: Deteksi objek
* `segment`: Segmentasi gambar
* `classify`: Klasifikasi gambar
* `pose`: Estimasi pose tubuh
* `obb`: Deteksi objek berorientasi

### 📌 Contoh Penggunaan Task

```bash
# Deteksi objek
yolo detect predict model=yolo11n.pt source=path/to/image.jpg

# Segmentasi gambar
yolo segment predict model=yolo11n-seg.pt source=path/to/image.jpg

# Klasifikasi gambar
yolo classify predict model=yolo11n-cls.pt source=path/to/image.jpg

# Estimasi pose
yolo pose predict model=yolo11n-pose.pt source=path/to/image.jpg

# Deteksi objek berorientasi
yolo obb predict model=yolo11n-obb.pt source=https://ultralytics.com/images/boats.jpg
```

---

## 📅 Source (Sumber Data Input)

Menentukan sumber data yang akan digunakan oleh model.

### ✅ Jenis Source yang Didukung

* Gambar tunggal:

  ```bash
  source=path/to/image.jpg
  ```
* Folder gambar:

  ```bash
  source=path/to/folder/
  ```
* Video lokal:

  ```bash
  source=path/to/video.mp4
  ```
* Streaming (RTSP, HTTP):

  ```bash
  source=rtsp://username:password@ip/stream
  ```
* Webcam:

  ```bash
  source=0
  ```
* URL gambar/video:

  ```bash
  source=https://ultralytics.com/images/bus.jpg
  ```

---

## 💾 Output Management (Manajemen Hasil)

Default output disimpan ke:

```
runs/{task}/{mode}
```

Contoh:

* `runs/detect/predict`
* `runs/classify/predict`

### 🩹 Argumen Output

* `save=True`: Simpan gambar/video hasil
* `show=True`: Tampilkan hasil (GUI)
* `project=folder`: Simpan di folder tertentu
* `name=subfolder`: Nama subfolder dalam `project`

```bash
yolo classify predict model=yolo11n-cls.pt source=sample/image.jpg save=True project=outputs name=classification
```

### 🎥 Menyimpan Output Video & Streaming

```bash
# Video lokal
yolo detect predict model=yolo11n.pt source=video/input.mp4 save=True

# Webcam
yolo detect predict model=yolo11n.pt source=0 save=True

# RTSP
yolo detect predict model=yolo11n.pt source=rtsp://... save=True
```

---

## ⚙️ Mode (Mode Operasi)

Menentukan operasi yang dijalankan terhadap model:

* `train`: Melatih model
* `val`: Validasi model
* `predict`: Prediksi gambar/video
* `export`: Ekspor model ke format lain
* `track`: Pelacakan objek
* `benchmark`: Uji performa model

### 📌 Contoh Penggunaan Mode

```bash
# Melatih
yolo train model=yolo11n.pt data=dataset.yaml epochs=100 imgsz=640

# Validasi
yolo val model=yolo11n.pt data=dataset.yaml

# Prediksi
yolo predict model=yolo11n.pt source=path/to/image.jpg

# Ekspor
yolo export model=yolo11n.pt format=onnx imgsz=640

# Tracking
yolo track model=yolo11n.pt source=path/to/video.mp4

# Benchmark
yolo benchmark model=yolo11n.pt data=dataset.yaml imgsz=640
```

---

## 🧹 Model

Varian model YOLO11 yang tersedia:

* `yolo11n.pt`: Model kecil, ringan
* `yolo11s.pt`: Ringan dan cepat
* `yolo11m.pt`: Akurasi sedang
* `yolo11l.pt`: Akurasi tinggi
* `yolo11x.pt`: Akurasi maksimum

---

## 📹 Media Source

* [Livecam Four Corners](https://youtu.be/2X27I6BAJcI)
* [Sydney Street Walk 4K](https://youtu.be/HRg1gJi6yqc)
* [Ultralytics Boat Image](https://ultralytics.com/images/boats.jpg)

---

## 🔗 Referensi

* Dokumentasi Ultralytics: [https://docs.ultralytics.com/](https://docs.ultralytics.com/)
* GitHub Ultralytics: [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)
* Konfigurasi CLI: [https://docs.ultralytics.com/usage/cfg/](https://docs.ultralytics.com/usage/cfg/)
