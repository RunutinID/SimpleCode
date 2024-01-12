import qrcode

def generate_qr_code(data, output_path):
    # Membuat objek QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Menambahkan data ke QRCode
    qr.add_data(data)
    qr.make(fit=True)

    # Membuat objek Image dari QRCode
    img = qr.make_image(fill_color="black", back_color="white")

    # Menyimpan QRCode sebagai file gambar
    img.save(output_path)

if __name__ == "__main__":
    # Data yang akan disematkan dalam QR code
    qr_data = "https://pypi.org/project/qrcode/"

    # Path untuk menyimpan QR code (ganti dengan path yang diinginkan)
    output_path = "qrcode_pypi.png"

    # Generate QR code
    generate_qr_code(qr_data, output_path)

    print(f"QR code telah dibuat dan disimpan di: {output_path}")