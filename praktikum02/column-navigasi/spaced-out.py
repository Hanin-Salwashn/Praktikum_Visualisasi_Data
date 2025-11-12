import streamlit as st  # type: ignore
from PIL import Image

# Membuka gambar
img = Image.open("../../praktikum01/assets/kelinci.jpeg")

st.title("Spaced-Out Columns")

st.subheader("Kelompok 4")
st.markdown("""
**1. Erina Nurul Hodijah - 0110112113**

**2. Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294**

**3. Mohammad Ramdhani - 0110122083**
""")

# Membuat dua baris dengan kolom berjarak
for _ in range(2):
    # Membuat kolom dengan proporsi lebar berbeda untuk memberi jarak antar kolom
    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)