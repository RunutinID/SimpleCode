import cv2

def deteksi_wajah(foto_path):
    # Membaca gambar dari file
    foto = cv2.imread(foto_path)

    # Mengonversi gambar menjadi skala abu-abu (grayscale)
    foto_abu = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

    # Menggunakan klasifikasi wajah pre-trained dari OpenCV
    klasifikasi_wajah = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Mendeteksi wajah dalam gambar
    wajah = klasifikasi_wajah.detectMultiScale(foto_abu, scaleFactor=1.1, minNeighbors=5)

    # Menggambar kotak pembatas di sekitar wajah yang terdeteksi
    for (x, y, w, h) in wajah:
        cv2.rectangle(foto, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Menampilkan gambar dengan kotak pembatas wajah
    cv2.imshow('Deteksi Wajah', foto)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ganti 'nama_foto.jpg' dengan nama file foto yang ingin Anda gunakan
deteksi_wajah('nuurr.png')
