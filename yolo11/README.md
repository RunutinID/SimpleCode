# Dokumentasi YOLOv11

## Gambaran Umum
Direktori ini berisi skrip untuk melakukan berbagai tugas visi komputer menggunakan model YOLOv11. Setiap skrip dirancang untuk tugas tertentu, seperti deteksi objek, klasifikasi gambar, deteksi bounding box berorientasi, estimasi pose, dan segmentasi objek.

---

## Skrip

### 1. Deteksi Objek (`predict_detect.py`)
Skrip ini mendeteksi objek dalam gambar atau video menggunakan model YOLOv11.

- **Model**: `models/yolo11n.pt`
- **Input**: URL gambar, gambar lokal, atau webcam.
- **Output**: Gambar beranotasi disimpan di `output/runX/`.

**Cara Penggunaan**:
```bash
python predict_detect.py
```

---

### 2. Klasifikasi Gambar (`predict_classify.py`)
Skrip ini mengklasifikasikan gambar ke dalam kategori yang telah ditentukan menggunakan model YOLOv11.

- **Model**: `models/yolo11n-cls.pt`
- **Input**: URL gambar, gambar lokal, atau webcam.
- **Output**: Gambar beranotasi dengan label kelas hasil prediksi disimpan di `output_classification/run_classifyX/`.

**Cara Penggunaan**:
```bash
python predict_classify.py
```

---

### 3. Deteksi Bounding Box Berorientasi (`predict_obb.py`)
Skrip ini mendeteksi bounding box berorientasi (OBB) untuk objek dalam gambar.

- **Model**: `models/yolo11n-obb.pt`
- **Input**: URL gambar atau gambar lokal.
- **Output**: Gambar beranotasi dengan OBB disimpan di `output_obb/run_obbX/`.

**Cara Penggunaan**:
```bash
python predict_obb.py
```

---

### 4. Estimasi Pose (`predict_pose.py`)
Skrip ini mengestimasi pose manusia dalam gambar atau video.

- **Model**: `models/yolo11n-pose.pt`
- **Input**: URL gambar, gambar lokal, atau webcam.
- **Output**: Gambar beranotasi dengan estimasi pose disimpan di `output_pose/run_poseX/`.

**Cara Penggunaan**:
```bash
python predict_pose.py
```

---

### 5. Segmentasi Objek (`predict_segment.py`)
Skrip ini melakukan segmentasi objek untuk menghasilkan masker pada objek yang terdeteksi.

- **Model**: `models/yolo11n-seg.pt`
- **Input**: URL gambar, gambar lokal, atau webcam.
- **Output**: Gambar beranotasi dengan masker segmentasi disimpan di `output_segmentation/run_segX/`.

**Cara Penggunaan**:
```bash
python predict_segment.py
```

---

## Prasyarat
1. **Python**: Pastikan Python 3.8 atau lebih baru telah terinstal.
2. **Dependensi**: Instal pustaka yang diperlukan menggunakan pip:
   ```bash
   pip install ultralytics opencv-python
   ```
3. **Model**: Pastikan model YOLOv11 yang sesuai tersedia di direktori `models/`. Jika tidak, skrip akan mencoba mengunduhnya secara otomatis.

---

## Catatan
- Koneksi internet diperlukan untuk mengunduh model jika belum tersedia.
- Output disimpan di direktori khusus tugas di dalam folder `output/`.
- Gunakan gambar atau video yang relevan dengan tugas untuk hasil yang optimal.