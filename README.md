# Proyek Analisis Data: Bike Sharing

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis dataset Bike Sharing yang mencakup peminjaman sepeda selama beberapa tahun. Melalui analisis ini, kita dapat mengetahui pola penggunaan sepeda pada hari kerja dan akhir pekan, jam tersibuk, serta tren peminjaman sepeda sepanjang waktu.

## Fitur Utama
- **Total Peminjaman pada Januari 2010:** Menampilkan total peminjaman sepeda di bulan Januari 2010.
- **Jam Teramai Sepanjang Tahun:** Menunjukkan jam dengan peminjaman sepeda terbanyak sepanjang tahun.
- **Perbandingan Peminjaman Sepeda:** Membandingkan rata-rata peminjaman sepeda antara hari kerja dan akhir pekan.
- **Tren Penyewaan Sepeda Harian:** Visualisasi tren peminjaman sepeda harian dari dataset yang disediakan.
- **Distribusi Peminjaman Sepeda per Jam dan Bulan:** Menggunakan histogram dan pie chart untuk menggambarkan distribusi peminjaman sepeda berdasarkan jam dan bulan.

## Instalasi
1. Buat environment baru menggunakan conda dan install dependencies:
    ```bash
    conda create --name bike-sharing python=3.11.4
    conda activate bike-sharing
    pip install streamlit pandas matplotlib numpy seaborn plotly
    ```

2. Clone repository atau salin file Python dan dataset ke local directory.

3. Pindah ke folder `dashboard` untuk menjalankan aplikasi:
    ```bash
    cd dashboard
    ```

4. Jalankan aplikasi Streamlit menggunakan perintah berikut:
    ```bash
    streamlit run dashboard.py
    ```

## File dan Dataset
- `day.csv`: Dataset yang berisi informasi harian tentang peminjaman sepeda.
- `hour.csv`: Dataset yang berisi informasi peminjaman sepeda per jam.
- `dashboard.py`: Kode Python utama yang mengimplementasikan analisis data dan visualisasi menggunakan Streamlit.

## Penggunaan
1. **Total Peminjaman pada Januari 2010**
   - Menampilkan total peminjaman sepeda di bulan Januari 2010.
   
2. **Jam Teramai Sepanjang Tahun**
   - Menampilkan jam dengan peminjaman sepeda paling banyak dalam format AM/PM.
   
3. **Rata-rata Peminjaman pada Hari Kerja vs Akhir Pekan**
   - Membandingkan rata-rata peminjaman sepeda pada hari kerja dan akhir pekan menggunakan bar chart.
   
4. **Tren Penyewaan Sepeda Harian**
   - Visualisasi tren peminjaman sepeda harian menggunakan line chart.
   
5. **Distribusi Peminjaman Sepeda**
   - Histogram distribusi peminjaman sepeda per kategori seperti bulan, hari, dan kecepatan angin.
   
6. **Korelasi Antar Variabel**
   - Heatmap korelasi antar variabel dalam dataset.

## Teknologi yang Digunakan
- **Python:** Bahasa pemrograman utama.
- **Streamlit:** Framework untuk membuat aplikasi web interaktif.
- **Pandas:** Digunakan untuk manipulasi dan analisis data.
- **Matplotlib dan Seaborn:** Untuk visualisasi data dalam bentuk grafik.
- **Plotly:** Library untuk visualisasi interaktif.

## Hasil Analisis
- Pada bulan Januari 2010, terdapat total peminjaman sebanyak `38189` sepeda.
- Jam peminjaman sepeda paling ramai terjadi pada `4 PM`.
- Rata-rata peminjaman sepeda lebih tinggi pada hari kerja dibandingkan akhir pekan.

