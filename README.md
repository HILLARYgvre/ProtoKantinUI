# KantinUI 🍛
Website kantin Universitas Indonesia: peta interaktif, menu, denah, filter, dan rute.

## Struktur
- `app.py`            : backend Flask (halaman utama + API)
- `public/index.html` : frontend (HTML/CSS/JS, semua data kantin dummy dibuat di sini)
- `data/data.json`    : data stasiun & kantin untuk API Python
- `requirements.txt`

## Menjalankan di VS Code
1. Buka folder `kantinui` (File > Open Folder)
2. Terminal: `python -m venv venv` lalu aktifkan (`venv\Scripts\activate` di Windows, `source venv/bin/activate` di Mac/Linux)
3. `pip install -r requirements.txt`
4. `python app.py` lalu buka http://localhost:5000
API: `/api/canteens?me=FT&q=ayam&cat=Nasi&max=20000&sort=d`

## Catatan
Data kantin di `index.html` dan `data.json` masih dummy dan belum sinkron. Langkah berikutnya: pindahkan data ke Python supaya frontend memanggil `/api/canteens`.

## Foto asli
Letakkan foto di `public/img/` sesuai nama di `public/img/DAFTAR-FOTO.txt` (mis. `ayam-geprek.jpg`). Kalau belum ada, tampil ilustrasi emoji.
