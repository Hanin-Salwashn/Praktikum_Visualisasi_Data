import streamlit as st
import matplotlib.pyplot as plt

st.title("Line Chart")
st.subheader("Kelompok 4")
st.markdown("""
            **1. Erina Nurul Hodijah - 0110112113**
            
            **2. Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294**
            
            **3. Mohammad Ramdhani - 0110122083**
            """)

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10, 20, 15, 25, 30, 45, 40, 50, 60, 55, 65, 70]
product_B_sales = [5, 10, 8, 15, 18, 20, 22, 30, 25, 35, 40, 45]

# Streamlit layout
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")

# Selectbox untuk memilih tipe visualisasi
option = st.sidebar.selectbox(
    "Pilih Tipe Visualisasi",
    ("Line Plot", 
     "Kustomisasi Line Plot", 
     "Garis Berbeda untuk Menunjukkan Trend", 
     "Subplot")
)

def line_plot():
    # Line Plot Sederhana
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales)
    ax.set_title('Penjualan Produk A Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    st.pyplot(fig) # Menampilkan plot di Streamlit

def customize_line_plot():
    # Line Plot dengan Kustomisasi dan Multiple Lines
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', color='blue', linestyle='--', marker='o')
    ax.plot(months, product_B_sales, label='Product B', color='red', linestyle='-', marker='x')
    ax.set_title('Penjualan Produk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def trend_lines_plot():
    # Line Plot untuk Trend
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A Trend', linestyle='--', color='blue')
    ax.plot(months, product_B_sales, label='Product B Trend', linestyle=':', color='red')
    ax.set_title('Tren Penjualan Produk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def subplots():
    # Subplot
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Plot for Product A
    axs[0].plot(months, product_A_sales, label='Product A', color='blue', marker="o")
    axs[0].set_title('Penjualan Produk A Per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid(True)

    # Plot for Product B
    axs[1].plot(months, product_B_sales, label='Product B', color='red', marker='x')
    axs[1].set_title('Penjualan Produk B Per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)

# Memanggil fungsi berdasarkan pilihan user
if option == "Line Plot":
    line_plot()
elif option == "Kustomisasi Line Plot":
    customize_line_plot()
elif option == "Garis Berbeda untuk Menunjukkan Trend":
    trend_lines_plot()
elif option == "Subplot":
    subplots()