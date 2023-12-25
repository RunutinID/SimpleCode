# Deteksi Wajah dengan OpenCV

Selamat datang di proyek Deteksi Wajah dengan OpenCV! Repositori ini menyediakan implementasi sederhana deteksi wajah menggunakan OpenCV dan Python.

## Daftar Isi

- [Pendahuluan](#pendahuluan)
- [Teori Deteksi Wajah dengan Haar Cascade](#teori-deteksi-wajah-dengan-haar-cascade)
- [Library yang Digunakan](#library-yang-digunakan)
- [Instalasi Library](#instalasi-library)
- [Menjalankan Kode](#menjalankan-kode)

## Pendahuluan

Proyek ini menunjukkan implementasi deteksi wajah, tugas dasar pengolahan citra, menggunakan OpenCV. Tujuannya adalah memberikan contoh yang jelas dan ringkas untuk memahami konsep teoretis dan menjalankan kode.

## Teori Deteksi Wajah dengan Haar Cascade

Deteksi wajah adalah teknik pengolahan citra yang mengidentifikasi dan menemukan wajah manusia dalam gambar atau video. Dalam proyek ini, kami menggunakan Haar Cascade Classifier, algoritma efektif untuk mendeteksi pola dalam gambar. Klasifier dilatih untuk mengenali fitur wajah, seperti mata, hidung, dan mulut.

## Library yang Digunakan

Library utama yang digunakan dalam proyek ini adalah:
- OpenCV: Library komputer vision populer untuk pengolahan citra.

## Instalasi Library

Untuk menginstal library OpenCV, jalankan perintah berikut di terminal:

```bash
pip install opencv-python
```

## Cara Menjalankan Code
1. Klona repositori ke mesin lokal.
2. Unduh file haarcascade_frontalface_default.xml dari sumber dan letakkan dalam direktori proyek.
3. Program sudah bisa dijalankan