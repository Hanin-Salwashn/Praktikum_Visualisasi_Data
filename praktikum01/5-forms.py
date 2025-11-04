import streamlit as st
from datetime import time, date  # <-- pastikan 'time' diimpor

st.title("TUGAS 3 VISUALISASI DATA")
st.subheader("Anggota Kelompok 4:")
st.markdown("""
1. Erina Nurul Hodijah - 0110122113
2. Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
3. Mohammad Ramdhani - 0110122083
""")

# Membuat Form Pengguna 
with st.form("form_data_pengguna"):
    st.header("Silahkan Isi Data di Bawah Ini")

    # Text Box => elemen input yang memungkinkan pengguna untuk memasukkan teks
    nama = st.text_input("Masukkan Nama Anda", max_chars=25)
    password = st.text_input("Masukkan Password", type="password")

    # Text Area => elemen input yang digunakan untuk menerima masukan teks panjang dari pengguna
    deskripsi = st.text_area("Tuliskan deskripsi singkat tentang diri Anda")

    # Number Input => elemen input yang memungkinkan pengguna untuk memasukkan angka
    usia = st.number_input("Masukkan usia Anda", min_value=10, max_value=100, step=1)

    # Time => elemen input yang memungkinkan pengguna untuk memilih waktu tertentu (jam dan menit)
    waktu_favorit = st.time_input("Pilih waktu favorit Anda", value=time(8, 0))

    # Date => elemen yang memungkinkan pengguna untuk memilih tanggal tertentu melalui antarmuka interaktif
    tanggal_lahir = st.date_input("Masukkan tanggal lahir Anda", value=date(2000, 1, 1))

    # Color => elemen yang memungkinkan pengguna memilih warna melalui antarmuka pemilih warna (color picker)
    warna_favorit = st.color_picker("Pilih warna favorit Anda", "#00f900")

    # Dataset Upload =>  fitur yang memungkinkan pengguna mengunggah file (seperti dataset) ke aplikasi Streamlit untuk diproses atau dianalisis
    dataset = st.file_uploader("Unggah dataset (format CSV)", type=["csv"])

    # Submit Button => elemen yang digunakan untuk mengirimkan atau memproses data dalam sebuah formulir (form)
    submit = st.form_submit_button("Submit")

# Tindakan Setelah Tombol Submit Ditekan
if submit:
    st.success("Data berhasil dikirim!")
    st.subheader("Data yang Anda Masukkan:")
    st.write(f"*Nama:* {nama}")
    st.write(f"*Usia:* {usia} tahun")
    st.write(f"*Tanggal Lahir:* {tanggal_lahir}")
    st.write(f"*Waktu Favorit:* {waktu_favorit}")
    st.write(f"*Warna Favorit:* {warna_favorit}")
    st.write(f"*Deskripsi:* {deskripsi}")

    if dataset is not None:
        st.write(f"*File yang diunggah:* {dataset.name}")
    else:
        st.warning("Belum ada file yang diunggah.")