import streamlit as st                      # Streamlit untuk membuat aplikasi web
import matplotlib.pyplot as plt             # Matplotlib untuk visualisasi chart manual
import pandas as pd                         # Pandas untuk mengelola data dalam DataFrame

st.title("Bar Chart")                       # Menampilkan judul halaman
st.subheader("Kelompok 4")                  # Menampilkan subjudul kelompok
st.markdown("""
            **1. Erina Nurul Hodijah - 0110112113**
            
            **2. Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294**
            
            **3. Mohammad Ramdhani - 0110122083**
            """)                             # Menampilkan daftar nama anggota kelompok

# data
data = {                                     # Dictionary yang berisi jurusan & jumlah mahasiswa
    'Jurusan': ['Ilmu komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science'],
    'Jumlah Mahasiswa': [120, 150, 100, 80]
}
df = pd.DataFrame(data)                      # Mengubah dictionary menjadi DataFrame agar lebih mudah divisualisasikan

# streamlit bar chart
st.title('Basic Bar Chart - Jumlah Mahasiswa Per Jurusan')   # Judul chart Streamlit
st.bar_chart(df.set_index('Jurusan'))                        # Menampilkan bar chart otomatis dari Streamlit

st.title('Basic Bar Chart Menggunakan Matplotlib')           # Judul chart Matplotlib
fig, ax = plt.subplots()                                     # Membuat figure dan axis untuk chart
ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color='skyblue')   # Membuat bar chart manual
ax.set_title('Jumlah Mahasiswa per Jurusan')                 # Judul chart
ax.set_xlabel('Jurusan')                                     # Label sumbu X
ax.set_ylabel('Jumlah Mahasiswa')                            # Label sumbu Y

st.pyplot(fig)                                               # Menampilkan chart Matplotlib ke Streamlit

st.title('Kustomisasi Bar Chart')                            # Judul chart kustom
fig, ax = plt.subplots()                                     # Membuat figure baru
colors = ['blue', 'green', 'orange', 'purple']               # Daftar warna untuk setiap bar
bars = ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color=colors)  # Membuat bar chart berwarna
ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color=colors)         # Bar chart kedua (duplikasi dari kode asli)
ax.set_title('Jumlah Mahasiswa per Jurusan')                 # Judul chart
ax.set_xlabel('Jurusan')                                     # Label sumbu X
ax.set_ylabel('Jumlah Mahasiswa')                            # Label sumbu Y

for bar in bars:                                             # Loop untuk menambahkan angka di atas bar
    ax.text(bar.get_x() + bar.get_width() / 2,               # Posisi horizontal (tengah bar)
            bar.get_height() + 5,                            # Posisi vertikal sedikit di atas bar
            str(bar.get_height()),                           # Nilai tinggi bar (ditampilkan sebagai teks)
            ha='center')                                     # Rata tengah teks

st.pyplot(fig)                                               # Menampilkan chart kustom

# multiple Bar Chart
st.title('Multiple Bar Chart')                               # Judul chart multiple bar

# data tambahan
data_2023 = [120, 150, 100, 80]                              # Data per tahun 2023
data_2024 = [140, 160, 110, 90]                              # Data per tahun 2024

x = range(len(data['Jurusan']))                              # Posisi bar untuk setiap jurusan
width = 0.4                                                  # Lebar bar

fig, ax = plt.subplots()                                     # Membuat figure baru
ax.bar(x, data_2023, width=width, label='2023', color='skyblue')   # Bar untuk tahun 2023
ax.bar([p + width for p in x], data_2024, width=width, label='2024', color='orange')  # Bar tahun 2024 disebelahnya

ax.set_title('Jumlah Mahasiswa per Jurusan (2023 vs 2024)')  # Judul chart
ax.set_xlabel('Jurusan')                                     # Label sumbu X
ax.set_ylabel('Jumlah Mahasiswa')                            # Label sumbu Y
ax.set_xticks([p + width / 2 for p in x])                    # Posisi label agar berada di tengah dua bar
ax.set_xticklabels(data['Jurusan'])                          # Label jurusan di sumbu X
ax.legend()                                                  # Menampilkan legenda tahun

st.pyplot(fig)                                               # Menampilkan chart Multiple Bar
