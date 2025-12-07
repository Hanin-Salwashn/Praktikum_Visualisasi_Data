import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dataset dasar
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

# Dataset penjualan hari kerja dan akhir pekan
penjualan_weekdays = [50, 60, 70, 90, 100, 110, 130, 150, 180]
penjualan_weekend = [40, 50, 60, 70, 80, 90, 100, 110, 120]

# Dataset analisis lebih lanjut (3 variabel)
data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Cokelat' : [40, 45, 50, 55, 60, 65, 70, 75, 80],
    'Penjualan_Vanila'  : [82, 80, 78, 76, 77, 80, 82, 85, 88],
    'Penjualan_Stroberi': [55, 50, 55, 60, 65, 60, 65, 70, 72],
    'Kelembapan'        : [40, 45, 50, 55, 60, 65, 70, 75, 80]
}

# Konversi ke dataframe
df = pd.DataFrame(data)

# Sidebar menu pilihan visualisasi
option = st.sidebar.selectbox(
    "Pilih contoh scatter plot",
    (
        "Basic Scatter Plot",
        "Kustomisasi Scatter Plot",
        "Multiple Scatter Plot",
        "Analisis dengan Scatter Plot"
    )
)

# Identitas kelompok
st.title("Bar Chart")                       # Menampilkan judul halaman
st.subheader("Kelompok 4")                  # Menampilkan subjudul kelompok
st.markdown("""
            **1. Erina Nurul Hodijah - 0110112113**
            
            **2. Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294**
            
            **3. Mohammad Ramdhani - 0110122083**
            """)   

# Fungsi 1: Basic Scatter Plot
def basic_scatter():
    st.subheader("1. Basic Scatter Plot")
    fig, ax = plt.subplots()

    ax.scatter(suhu, penjualan)  # scatter dasar tanpa kustomisasi
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')

    st.pyplot(fig)

# Fungsi 2: Kustomisasi Scatter Plot
def custom_scatter():
    st.subheader("2. Kustomisasi Scatter Plot")
    fig, ax = plt.subplots()

    # scatter dengan warna oranye, ukuran besar, edgecolor, dan transparansi
    ax.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black', alpha=0.7)
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.grid(True)  # menampilkan grid

    st.pyplot(fig)

# Fungsi 3: Multiple Scatter Plot
def multiple_scatter():
    st.subheader("3. Multiple Scatter Plot")
    fig, ax = plt.subplots()

    # scatter untuk hari kerja
    ax.scatter(suhu, penjualan_weekdays, color='green', label='Hari Kerja', s=80)

    # scatter untuk akhir pekan
    ax.scatter(suhu, penjualan_weekend, color='purple', label='Akhir Pekan', s=80)

    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.grid(True)
    ax.legend()  # menampilkan legenda

    st.pyplot(fig)

# Fungsi 4: Analisis Scatter Plot (3 variabel)
def scatter_3_variabel():
    st.subheader("4. Analisis dengan Scatter Plot")

    # User memilih jenis es krim
    jenis_eskrim = st.selectbox(
        'Pilih Jenis Es Krim',
        ['Cokelat', 'Vanila', 'Stroberi']
    )

    # Pilih kolom sesuai jenis es krim
    if jenis_eskrim == 'Cokelat':
        penjualan_jenis = df['Penjualan_Cokelat']
    elif jenis_eskrim == 'Vanila':
        penjualan_jenis = df['Penjualan_Vanila']
    else:
        penjualan_jenis = df['Penjualan_Stroberi']

    # Menampilkan data
    st.subheader("Data Penjualan dan Suhu")
    st.dataframe(df)

    # Membuat scatter dengan warna berdasarkan kelembapan
    fig, ax = plt.subplots()
    scatter = ax.scatter(
        df['Suhu'],
        penjualan_jenis,
        c=df['Kelembapan'],      # warna mengikuti nilai kelembapan
        s=100,                   # ukuran titik
        cmap='coolwarm',         # colormap
        alpha=0.7
    )

    ax.set_xlabel('Suhu')
    ax.set_ylabel(f'Penjualan Es Krim {jenis_eskrim}')
    ax.set_title(f'Hubungan Penjualan, Suhu, dan Kelembapan ({jenis_eskrim})')

    # colorbar untuk menunjukkan nilai kelembapan
    plt.colorbar(scatter, label='Kelembapan (%)')

    st.pyplot(fig)

    # ringkasan analisis
    st.subheader('Analisis Hubungan')
    st.write(
        f"Grafik ini menampilkan hubungan antara suhu, kelembapan, "
        f"dan penjualan es krim jenis **{jenis_eskrim}**."
    )

# Routing fungsi berdasarkan pilihan menu
if option == "Basic Scatter Plot":
    basic_scatter()
elif option == "Kustomisasi Scatter Plot":
    custom_scatter()
elif option == "Multiple Scatter Plot":
    multiple_scatter()
elif option == "Analisis dengan Scatter Plot":
    scatter_3_variabel()