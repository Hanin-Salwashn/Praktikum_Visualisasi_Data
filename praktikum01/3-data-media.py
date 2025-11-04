import streamlit as st
import base64
from PIL import Image

# membuat judul
st.title("PRAKTIKUM 01 - Data Media")
st.caption("di kerjakan tanggal 04 - November 2025")

# membuat subjudul
st.subheader("Kelompok 4")
st.markdown("""
            **1. Erina Nurul Hodijah - 0110112113**
            
            **2. Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294**
            
            **3. Mohammad Ramdhani - 0110122083**
            """)

# Displaying an Image
st.subheader("Displaying an Image")

st.write("Displaying an Images")  # Menampilkan teks deskriptif
# Displaying Image by specifying path
# Menampilkan satu gambar dari folder assets
st.image("assets/kucing.jpeg")
# Image Courtesy by unsplash
st.write("Image Courtesy: unsplash.com")


# Displaying Multiple Images
st.subheader("Displaying Multiple Images")

st.write("Displaying Multiple Images")  # Menampilkan teks deskriptif
# Listing out animal images
# Membuat list berisi path gambar dari folder assets
animal_images = [
    'assets/katak.jpeg',
    'assets/kelinci.jpeg',
    'assets/kucing.jpeg',
    'assets/marmut.jpg'
]

# Displaying Multiple images with width 150
# Menampilkan beberapa gambar sekaligus dengan lebar 150 piksel
st.image(animal_images, width=150)
# Image Courtesy
st.write("Image Courtesy: Unsplash")


# Background Image
st.subheader("Background Image")

# Function to set Image as Background
def add_local_background_image(_image):
    # Membuka file gambar dalam mode 'rb' (read binary)
    with open(_image, "rb") as image:
        # Mengubah data gambar menjadi string base64 agar bisa ditampilkan di CSS
        encoded_string = base64.b64encode(image.read())
    st.write("Image Courtesy: unsplash")  # Menampilkan sumber gambar
    # Menyisipkan CSS untuk menjadikan gambar sebagai background
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:files/jpg;base64,{encoded_string.decode()});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.write("Background Image")  # Menampilkan teks deskriptif
# Calling Image in function
# Memanggil fungsi untuk menambahkan background dari folder assets
add_local_background_image('assets/kucing.jpeg')


# Resizing an Image
st.subheader("Resizing an Image")

# Membuka file gambar dari folder assets
original_image = Image.open("assets/kelinci.jpeg")
# Display Original Image
st.title("Original Image")  # Menampilkan judul bagian
st.image(original_image)    # Menampilkan gambar asli

# Resizing Image to 600*400
# Mengubah ukuran gambar menjadi 600x400 piksel
resized_image = original_image.resize((600, 400))
# Displaying Resized Image
st.title("Resized Image")   # Menampilkan judul untuk gambar hasil resize
st.image(resized_image)     # Menampilkan gambar yang sudah diubah ukurannya