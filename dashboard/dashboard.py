import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Menambahkan icon sepeda pada sidebar
st.set_page_config(page_title='Bike Sharing Analysis', page_icon='🚴', layout="wide")

# Sidebar
st.sidebar.title("Tren Penyewaan 🚲")

# Sidebar Widgets
selected_month = st.sidebar.selectbox("Pilih Bulan untuk Melihat Data", 
                                      ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 
                                       'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'])
show_trends = st.sidebar.checkbox('Tampilkan Tren Penyewaan Sepeda Harian', value=True)
show_correlation = st.sidebar.checkbox('Tampilkan Korelasi Antar Variabel', value=True)

# Streamlit App Title and Information
st.title('Proyek Analisis Data: Bike Sharing 🚴')
st.markdown("""
- **Nama:** Sulthan Farras Razin
- **Email:** sulthanrazin@apps.ipb.ac.id
- **ID Dicoding:** sulthanrazin

### Pendahuluan
Aplikasi ini memvisualisasikan data penyewaan sepeda dari sistem 'Bike Sharing'. Analisis dilakukan untuk memahami tren penyewaan sepeda sepanjang tahun dan berbagai faktor yang memengaruhi permintaan penyewaan.
""")

# Membaca file CSV
day = pd.read_csv("day.csv")
hour = pd.read_csv("hour.csv")

# Konversi kolom tanggal ke datetime
day['dteday'] = pd.to_datetime(day['dteday'])
hour['dteday'] = pd.to_datetime(hour['dteday'])  # Convert 'dteday' column in hour DataFrame

# Business Question 1: Total rentals in January 2010
st.subheader("Total Peminjaman pada Januari 2010")
jan_2010 = day[(day['yr'] == 0) & (day['mnth'] == 1)]['cnt'].sum()
st.write(f"Total peminjaman pada bulan Januari 2010: **{jan_2010}**")

# Menambahkan icon sepeda
st.markdown(f"**Total Peminjaman pada Januari 2010: 🚴 {jan_2010} sepeda**")

# Business Question 2: Peak rental hour throughout the year
st.subheader("Jam Teramai Sepanjang Tahun")
peak_hour = hour.groupby('hr')['cnt'].sum().idxmax()

# Convert to 12-hour format with AM/PM
peak_hour_12 = f"{peak_hour % 12 or 12} {'PM' if peak_hour >= 12 else 'AM'}"
st.write(f"Jam teramai sepanjang tahun: **{peak_hour_12}**")

# Business Question 3: Rentals comparison on weekdays vs weekends
st.subheader("Rata-rata Peminjaman Sepeda: Hari Kerja vs Akhir Pekan")
day['is_weekend'] = day['weekday'].apply(lambda x: 1 if x >= 5 else 0)
avg_weekday = day[day['is_weekend'] == 0]['cnt'].mean()
avg_weekend = day[day['is_weekend'] == 1]['cnt'].mean()
st.write(f"Rata-rata peminjaman sepeda pada hari kerja: **{avg_weekday:.2f}**")
st.write(f"Rata-rata peminjaman sepeda pada akhir pekan: **{avg_weekend:.2f}**")

# Improved Plotting the trends
if show_trends:
    st.subheader("Tren Penyewaan Sepeda Harian")
    plt.figure(figsize=(12, 6))
    
    # Gunakan seaborn untuk plot yang lebih rapi
    sns.lineplot(x=day['dteday'], y=day['cnt'], color='skyblue', linewidth=2)
    
    plt.title('Tren Penyewaan Sepeda Harian', fontsize=16)
    plt.xlabel('Tanggal', fontsize=14)
    plt.ylabel('Jumlah Penyewaan', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True)
    st.pyplot(plt)

    st.markdown("**Grafik di atas menunjukkan tren penyewaan sepeda harian sepanjang tahun.**")
    st.markdown("Terlihat ada pola tertentu, seperti peningkatan penyewaan di musim panas.")

# Peak Hour Visualization: Bar Chart
st.subheader("Jumlah Peminjaman per Jam")
hour_rentals = hour.groupby('hr')['cnt'].sum().reset_index()
fig_hour = px.bar(hour_rentals, x='hr', y='cnt', title='Jumlah Peminjaman per Jam',
                  labels={'hr': 'Jam', 'cnt': 'Jumlah Peminjaman'},
                  color_discrete_sequence=['#FF6F61'])
fig_hour.update_layout(xaxis_title='Jam', yaxis_title='Jumlah Peminjaman', title_x=0.5)
st.plotly_chart(fig_hour)

# Weekday vs Weekend Comparison: Bar Chart
st.subheader("Perbandingan Peminjaman: Hari Kerja vs Akhir Pekan")
labels = ['Hari Kerja', 'Akhir Pekan']
values = [avg_weekday, avg_weekend]
fig_weekday_weekend = px.bar(x=labels, y=values, title='Perbandingan Rata-rata Peminjaman',
                              labels={'x': 'Hari', 'y': 'Rata-rata Peminjaman'},
                              color_discrete_sequence=['#FFA07A', '#20B2AA'])
fig_weekday_weekend.update_layout(xaxis_title='Hari', yaxis_title='Rata-rata Peminjaman', title_x=0.5)
st.plotly_chart(fig_weekday_weekend)

# Monthly Rentals Distribution: Pie Chart with month names
st.subheader("Distribusi Peminjaman Bulanan")
monthly_rentals = day.groupby('mnth')['cnt'].sum().reset_index()

# Apply the month_map to convert month numbers to names
month_map = {
    1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April', 5: 'Mei', 6: 'Juni',
    7: 'Juli', 8: 'Agustus', 9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'
}
monthly_rentals['mnth'] = monthly_rentals['mnth'].map(month_map)

fig_pie = px.pie(monthly_rentals, values='cnt', names='mnth', title='Distribusi Peminjaman Bulanan', 
                 labels={'cnt': 'Jumlah Peminjaman', 'mnth': 'Bulan'},
                 color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig_pie)

# Jumlah Penyewaan Sepeda per Bulan (Jan 2011 - Des 2012)
st.subheader("Jumlah Penyewaan Sepeda per Bulan (Jan 2011 - Des 2012)")
bulanan = hour.groupby(pd.Grouper(key='dteday', freq='M')).sum()
plt.figure(figsize=(10, 3))
plt.plot(bulanan.index, bulanan['cnt'], marker='o', linestyle='-')
plt.title('Jumlah Penyewaan Sepeda per Bulan (Jan 2011 - Des 2012)')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewaan')
plt.grid(True)
st.pyplot(plt)

# Histogram Visualisasi Distribusi Peminjaman Sepeda
st.subheader("Distribusi Peminjaman Sepeda")
fitur = ['mnth', 'hr', 'weekday', 'temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered']
for feature in fitur:
    fig = px.histogram(hour,
                       x=feature,
                       y='cnt',
                       color='workingday',
                       title=f'Distribusi {feature} Berdasarkan Hari Kerja vs Akhir Pekan',
                       labels={'cnt': 'Jumlah Peminjaman', feature: feature.capitalize()},
                       color_discrete_sequence=px.colors.qualitative.Set1,
                       barmode='overlay',
                       histnorm='percent'
                       )
    
    # Menambahkan tata letak yang lebih informatif
    fig.update_layout(
        xaxis_title=feature.capitalize(),
        yaxis_title='Persentase Jumlah Peminjaman',
        title_x=0.5,
        bargap=0.2
    )

    # Update tooltip
    fig.update_traces(marker_line_color='black', marker_line_width=1)

    # Tampilkan chart
    st.plotly_chart(fig)

# Diagram Pie Distribusi Peminjaman Sepeda
st.subheader("Distribusi Jumlah Peminjaman Berdasarkan Kategori")
w = ['season', 'yr', 'holiday', 'workingday', 'weathersit']

for feature in w:
    fig = px.pie(
        hour,
        names=feature,
        values='cnt',
        title=f'Distribusi Jumlah Peminjaman Berdasarkan {feature.capitalize()}',
        hover_data=['cnt'],
        color_discrete_sequence=px.colors.qualitative.Set2,
        template='plotly_white'
    )
    st.plotly_chart(fig)

st.markdown("""
### Kesimpulan
1. Jumlah Peminjaman di Januari 2010:
   Total peminjaman sepeda pada bulan Januari 2010 mencapai **38.189**. Angka ini memberikan gambaran aktivitas awal tahun yang signifikan, meskipun sering kali dipengaruhi oleh kondisi cuaca dan suhu yang lebih dingin.

2. Jam Peminjaman Paling Ramai:
   Dari hasil analisis peminjaman per jam, jam 5
   PM (sore hari) adalah waktu yang paling banyak digunakan untuk meminjam sepeda. Ini mengindikasikan bahwa jam pulang kerja menjadi puncak aktivitas peminjaman.

3. Perbandingan Peminjaman di Hari Kerja vs Akhir Pekan:
   Rata-rata peminjaman sepeda per jam di hari kerja lebih tinggi di pagi dan sore hari, terutama saat jam sibuk (7-9 AM dan 5-7 PM), yang menunjukkan penggunaan sepeda untuk perjalanan kerja. Di akhir pekan, distribusi peminjaman lebih merata sepanjang hari.
""")