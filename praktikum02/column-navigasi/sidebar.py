import streamlit as st # type: ignore


st.title("Sidebar")

st.subheader("Kelompok 4")
st.markdown("""
            **1. Erina Nurul Hodijah - 0110112113**
            
            **2. Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294**
            
            **3. Mohammad Ramdhani - 0110122083**
            """)


st.sidebar.title("Sidebar Menu")
st.sidebar.radio("Are you a New User?", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0, 10)
