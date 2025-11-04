# import library yg dibutuhkan 
import streamlit as st
import pandas as pd 
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.title("PRAKTIKUM 01 - Visualisasi Data")
st.caption("Bagian 2: Data Elements")

st.subheader("Praktikum kita hari ini")
st.markdown("""
            1. Erina Nurul Hodijah - 0110112113
            2. Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
            3. Mohammad Ramdhani - 0110122083
            """)

st.subheader("Data Frame")
df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

#menampilkan dataframe
st.dataframe(df)

#highlight nilai minimum
st.subheader("Highlight Minimum Value di DataFrame")

#highlight nilai terkecil di setiap kolom dataframe
#axis=0 bekerja per kolom
st.dataframe(df.style.highlight_min(axis=0))

#tabel statis
st.subheader("Tabel Statis")
df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)
#menampilakn tabel statis
st.table(df)


#metrics:
st.subheader("Metrics")
st.metric(label="Temperature", value="31 C", delta="1.2 C") #kenaikan 1.2 C

# metrics sesuai delta_color
# delta_color digunakna untuk memberi warna sesuai arah perubahan
# delta_color digunakan untuk memberi warna sesuai arah peruwanan:
# - 'default' (default): naik -> hijau, turun -> merah
# - 'normal': kebalikannya (naik -> merah)
# - 'inverse': kebalikannya (naik -> merah)
# - 'off': tidak menampilkan warna perubahan

# definisikan variabel metrics
col1, col2, col3 = st.columns(3)

# menampilkan indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm") # naik dan baik

col2.metric(label = "Populasi", value="123 Miliar", delta="1 Miliar",
            delta_color="inverse") #naik tapi buruk

col3.metric(label="Pelanggan", value=100, delta=10,
            delta_color="off") # netral (tidak baik, tidak buruk)

# Menampilkan metrik tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0) # kosong # naik baik
                                              # karena di setting default
st.metric("Trees", "91456", "-1132649") # penurunan


st.subheader("The write( ) Function as a Superfunction")

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range (10))
)
st.write('Here is our Data', df, 'Data is in dataframe format.\n', "\nWrite is Super function")

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b']
)

chart = alt.Chart(df).mark_bar().encode(
x='a', y='b', tooltip=['a','b']
)
st.write(chart)


st.subheader("Magic")

"Adding 5 & 4", 5 + 4   # Menampilkan teks dan hasil penjumlahan
a = 5                   # Menyimpan nilai 5 ke dalam variabel a
"a =", a                # Menampilkan teks dan nilai variabel a

# Markdown dengan Magic Feature
# Streamlit dapat langsung menampilkan string markdown tanpa perlu st.markdown()
"Markdown working without defining its function explicitly."

# DataFrame menggunakan Magic
import pandas as pd     # Import pustaka pandas untuk membuat DataFrame
df = pd.DataFrame({'col': [1, 2]})  # Membuat DataFrame sederhana
"dataframe", df

# Membuat data acak menggunakan distribusi logistik
s = np.random.logistic(10, 5, size=5)

# Membuat objek figure dan axis menggunakan matplotlib
chart, ax = plt.subplots()

# Membuat histogram dengan 15 bins
ax.hist(s, bins=15)

# Magic chart — Streamlit otomatis menampilkan objek chart
"chart", chart
