import streamlit as st

st.title("COLUMN")

st.subheader("Kelompok 4")
st.markdown("""
            **1. Erina Nurul Hodijah - 0110112113**
            
            **2. Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294**
            
            **3. Mohammad Ramdhani - 0110122083**
            """)

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image("../../praktikum01/assets/kucing.jpeg")

col2.write("Ini adalah kolom kedua")
col2.image("../../praktikum01/assets/kelinci.jpeg")
