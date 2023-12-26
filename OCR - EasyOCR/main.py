import easyocr

# Inisialisasi pembaca dengan bahasa Inggris
reader = easyocr.Reader(['en'])

# Baca teks dari gambar
result = reader.readtext('test1.png')

# Cetak hasil OCR
print(result)