# RGB to XYZ
Transformasi dari ruang warna RGB (Red, Green, Blue) ke ruang warna XYZ adalah suatu proses untuk mengubah representasi warna citra dari satu ruang warna ke ruang warna yang lain. Ruang warna XYZ adalah suatu ruang warna absolute, yang berarti bahwa setiap warna diwakili oleh suatu koordinat yang unik dalam ruang warna tersebut, tanpa ketergantungan pada perangkat keras atau perangkat lunak tertentu.

Proses transformasi RGB ke XYZ dapat dilakukan dengan menggunakan matriks transformasi yang telah ditentukan sebelumnya. Matriks ini menggambarkan hubungan linier antara nilai-nilai intensitas warna dalam ruang warna RGB dengan nilai-nilai intensitas dalam ruang warna XYZ.

Ruang warna XYZ memiliki tiga komponen utama: X, Y, dan Z. Koordinat X, Y, dan Z merepresentasikan suatu warna dalam ruang warna XYZ. Transformasi dari RGB ke XYZ dapat dijelaskan dengan rumus matematis berikut:

\[ \begin{bmatrix} X \\ Y \\ Z \end{bmatrix} = \begin{bmatrix} R \\ G \\ B \end{bmatrix} \times M \]

Di mana:
- \( \begin{bmatrix} R \\ G \\ B \end{bmatrix} \) adalah vektor kolom nilai intensitas warna dalam ruang warna RGB.
- \( M \) adalah matriks transformasi yang telah ditentukan sebelumnya.

Matriks transformasi \( M \) dapat bervariasi tergantung pada standar atau spesifikasi yang digunakan. Standar yang umum digunakan adalah standar CIE 1931, di mana matriks transformasi untuk transformasi RGB ke XYZ adalah sebagai berikut:

\[ M = \begin{bmatrix} 0.4124564 & 0.3575761 & 0.1804375 \\ 0.2126729 & 0.7151522 & 0.0721750 \\ 0.0193339 & 0.1191920 & 0.9503041 \end{bmatrix} \]

Dengan menggunakan matriks transformasi ini, kita dapat mengalikan vektor \( \begin{bmatrix} R \\ G \\ B \end{bmatrix} \) dengan matriks \( M \) untuk mendapatkan vektor \( \begin{bmatrix} X \\ Y \\ Z \end{bmatrix} \), yang merepresentasikan warna dalam ruang warna XYZ. Hasil transformasi ini dapat digunakan untuk berbagai keperluan analisis warna dan pemrosesan citra.

# RGB to HS
Transformasi dari ruang warna RGB (Red, Green, Blue) ke ruang warna HS (Hue, Saturation) melibatkan konversi dari representasi warna berbasis warna primer (RGB) ke representasi warna berdasarkan sifat warna seperti nuansa (Hue) dan saturasi (Saturation). Ruang warna HS lebih terkait dengan persepsi manusia terhadap warna daripada ruang warna RGB.

Dalam ruang warna HS:

- **Hue (H):** Mewakili jenis warna atau nuansa. Hue diukur dalam derajat dan dapat memiliki nilai antara 0° hingga 360°, mencakup seluruh spektrum warna seperti merah, hijau, biru, dll.

- **Saturation (S):** Menunjukkan intensitas atau kejenuhan warna. Nilai saturasi berkisar antara 0 hingga 1, di mana 0 menghasilkan warna abu-abu (tidak berwarna) dan 1 menunjukkan warna yang penuh kejenuhan.

Transformasi dari RGB ke HS biasanya melibatkan konversi dari nilai intensitas warna merah, hijau, dan biru ke nilai Hue dan Saturation. Algoritma yang umum digunakan melibatkan beberapa perhitungan trigonometri.

Perlu diingat bahwa transformasi ini dapat bervariasi tergantung pada implementasi dan spesifikasi yang digunakan. Dengan konversi ini, Anda mendapatkan citra yang direpresentasikan dalam ruang warna HS yang dapat digunakan untuk analisis warna atau pemrosesan lebih lanjut.