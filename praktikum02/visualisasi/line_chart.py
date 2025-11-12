import streamlit as st
import pandas as pd
import numpy as np

st.title("Line Chart")

st.subheader("Kelompok 4")
st.markdown("""
            **1. Erina Nurul Hodijah - 0110112113**
            
            **2. Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294**
            
            **3. Mohammad Ramdhani - 0110122083**
            """)

df = pd.DataFrame(
    np.random.randn(40,4),
    columns=["C1", "C2", "C3", "C4"]
)

st.line_chart(df)
