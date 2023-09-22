# Instruksi Penggunaan PyFirmata untuk Arduino Uno

Dalam panduan ini, kami akan membantu Anda menginstal PyFirmata pada Arduino Uno dan menjalankan kode `blink_task.py` yang akan mengendalikan tiga LED sesuai dengan kondisi yang diberikan.

## Langkah 1: Instalasi PyFirmata pada Arduino Uno

1. Buka Arduino IDE pada komputer Anda.
2. Pilih menu "Sketch" (File) -> "Include Library" (Sertakan Perpustakaan).
3. Pilih "Manage Libraries" (Kelola Perpustakaan).
4. Cari "Firmata" menggunakan kotak pencarian.
5. Pilih "Firmata" dari daftar hasil pencarian.
6. Klik tombol "Install" (Instal) untuk menginstal perpustakaan PyFirmata.

## Langkah 2: Unggah StandartFirmata ke Arduino Uno

1. Hubungkan Arduino Uno ke komputer menggunakan kabel USB.
2. Buka Arduino IDE jika belum terbuka.
3. Pilih menu "File" -> "Examples" (Contoh) -> "Firmata" -> "StandardFirmata".
4. Klik tombol "Upload" (Unggah) untuk mengunggah kode StandartFirmata ke Arduino Uno.

## Langkah 3: Jalankan Kode `blink_task.py`

1. Pastikan Arduino Uno masih terhubung ke komputer melalui kabel USB.
2. Buka terminal atau command prompt pada komputer Anda.
3. Pindah ke direktori tempat Anda menyimpan file `blink_task.py` menggunakan perintah `cd`.
4. Jalankan kode `blink_task.py` dengan perintah berikut:
   python blink_task.py
6. Anda akan melihat bahwa tiga LED yang terhubung ke pin 9, 7, dan 6 pada Arduino Uno akan menyala dan mati sesuai dengan kondisi yang diberikan.

Sekarang Anda telah berhasil menginstal PyFirmata pada Arduino Uno dan menjalankan kode `blink_task.py` untuk mengendalikan LED. Anda dapat menggunakan Python dan PyFirmata untuk mengendalikan berbagai perangkat dan sensor yang terhubung ke Arduino Uno.


