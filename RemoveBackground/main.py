import rembg
from PIL import Image
import numpy as np

def remove_background(input_image_path, output_image_path):
    # Baca gambar
    input_image = Image.open(input_image_path)

    # Konversi gambar ke array NumPy
    input_array = np.array(input_image)

    # Hapus latar belakang menggunakan rembg
    output_array = rembg.remove(input_array)

    # Konversi array kembali ke gambar PIL
    output_image = Image.fromarray(output_array)

    # Simpan gambar tanpa latar belakang
    output_image.save(output_image_path)

if __name__ == "__main__":
    input_path = "nuurr.png"  # Ganti dengan path gambar masukan Anda
    output_path = "nuurr-rb.png"  # Ganti dengan path gambar keluaran Anda

    remove_background(input_path, output_path)
