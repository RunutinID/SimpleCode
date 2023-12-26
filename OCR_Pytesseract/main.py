import pytesseract
from PIL import Image

def perform_ocr(image_path):
    # Buka gambar menggunakan PIL
    img = Image.open(image_path)

    # Lakukan OCR pada gambar
    text = pytesseract.image_to_string(img)

    # Cetak hasil OCR
    print("Hasil OCR:")
    print(text)

if __name__ == "__main__":
    image_path = "test1.jpg"  # Ganti dengan path gambar yang ingin di-OCR

    perform_ocr(image_path)