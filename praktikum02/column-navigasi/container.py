import streamlit as st
import pandas as pd
import numpy as np


st.title("Praktikum 2 - Visualisasi Data")
st.caption("Bagian 7: Containers")

st.subheader("Kelompok 4")
st.markdown("""
            **1. Erina Nurul Hodijah - 0110112113**
            
            **2. Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294**
            
            **3. Mohammad Ramdhani - 0110122083**
            """)


with st.container():
    st.write("Element Inside Container")
    st.line_chart(np.random.randn(48, 4))
    st.write("Element Outside Container")


container_one = st.container()
container_one.write("Element One Inside Container")
st.write("Element Outside Container")
container_one.write("Element Two Inside Container")
container_one.line_chart(np.random.randn(40, 4))