import streamlit as st  # type: ignore
from PIL import Image

# Membuka gambar
img = Image.open("../../praktikum01/assets/kelinci.jpeg")

st.title("Grid")

st.subheader("Kelompok 4")
st.markdown("""
            **1. Erina Nurul Hodijah - 0110112113**
            
            **2. Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294**
            
            **3. Mohammad Ramdhani - 0110122083**
            """)

# Menentukan jumlah baris grid
for a in range(4):
    # Membuat 4 kolom dengan ukuran yang sama
    cols = st.columns((1, 1, 1, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)
