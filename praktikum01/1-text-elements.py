# import library yg dibutuhkan 
import streamlit as st

st.title("PRAKTIKUM 01")

st.subheader("Praktikum kita hari ini")
st.markdown("""
            1. Erina Nurul Hodijah - 0110112113
            2. Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
            3. Mohammad Ramdhani - 0110122083
            """)

# text element
st.header("Ini Header") # untuk buat header
st.subheader("Ini Sub Header") #untuk membuat subjudul yg lebih kecil
st.text("ini text biasa tanpa format") #untuk membuat teks polos tanpa fromat
st.markdown("**ini text bold** dan *ini text italic*") #markdown untuk memformat teks tebal/miring
st.markdown("""
            - ini baris 1
            - ini menggunakan markdown multibaris
            1. ini baris 2
            2. ini menggunakan markdown multi baris
            * ini baris 3
            * ini menggunakan markdown multi baris
            """)
st.title("ini judul")
st.caption("ini caption - Semangattt Berprosesss gess") #teks kecil di bawal elemen (untuk penjelasan)

# coba mandiri
# tuliskan
# 1. judul praktikum pakai title()
# 2. bagian praktikum pakai subheader()
# 3. nama lengkap anggota - nim pakai markdown multi baris """ """

st.subheader("Displaying LaTeX")
#bagian 2: menampakkan 
st.latex (r''' \cos^2\theta = 1-2\sin^2\theta ''') #rumus trigonometri
st.latex (''' (a+b)^2 + b^2 + 2ab ''') #rumus kuadrat binominal

# Bagian 3: Menampilkan Kode Program
st.header ("Displaying Code")
st.subheader("Python Code")

# simpan ke variable
code = '''
def hello():
    print("Hello, Hanin)
    '''

#st.code() untuk menampilkan potongan kode dengan format rapi dan syntax highlighting
st.code(code, language='python')


st.subheader("Java Code")
st.code("""
    public class GFG{
        public static void main(String arg[]) {
            Systems.out.printIn("Hello World!);
        }
    }
""", language= 'java' )

#fungsi st.code() bisa di gunakan untuk bahasa pemrograman lain seperti Java, JavaScript, C++, HTML, dll

st.subheader("JavaScript Code")
st.code("""
        <p id="demo"></p>
<script>
    try {
    addalert("Welcome guest!"); //kesalahan ketik (addalsert)
    sengaja dibuat untuk menimbulkan error
    }
    catch(err) {
        document.getElementById("demo").innerHTML = err.message; //
        menampilkanpesan error di elemen HTML dengan id 'demo'
    }
</script>
""", language='javascript')
#kode ini menunjukkan contoh bagaimana menangani error (exception) di javascript
# hasilnya tidak di jalankan di streamlit, tapi di tampilkan sebagai contoh kode.