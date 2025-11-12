import streamlit as st
from PIL import Image


st.title("Praktikum 2 - Visualisasi Data")
st.caption("Bagian 8: Padding")

st.subheader("Kelompok 4")
st.markdown("""
            **1. Erina Nurul Hodijah - 0110112113**
            
            **2. Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294**
            
            **3. Mohammad Ramdhani - 0110122083**
            """)


# Membuka gambar dari drive lokal
img = Image.open("../../praktikum01/assets/kucing.jpeg")


st.title("Padding")


# Mendefinisikan padding menggunakan kolom
col1, padding, col2 = st.columns((10, 2, 10))


with col1:
    col1.image(img)


with col2:
    col2.image(img)