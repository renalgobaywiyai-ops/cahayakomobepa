import streamlit as st
# Konfigurasi halaman
st.set_page_config(
    page_title="Cahaya Komobepa",
    page_icon="✨"
    layout="wide"
)
# Judul Utama
st.title("✨Cahaya Komobepa")
st.subheader("Selamat Datang Di Website Resmi Kami")
# Garis Pemisah
st.markdwon("---")
# Bagian Tentang Kami
st.header("Tentang Cahaya Komobepa")
st.write("""
**Cahaya Komobepa** adalah wadah kreativitas
dan informasi yang hadir untuk berbagi karya, ide,
dan wawasan.
Kami berkomitmen untuk memeberikan konten yang 
bermanfaat, inspiratif, dan menghibur bagi semua
pengunjung.
""")
# Bagian Layanan / Fitur
st.header("Apa yang Kami Sajikan?")
col1, = st.columns(1)
with col1:
   st.subheader("Informasi")
   st.write("Berbagai artikel dan pengetahuan seputar topik yang bermanfaat untuk Anda.")
# Bagi Kontak
st.header("Hubungi Kami")
nama = st.text_input("Nama Lengkap")
pesan = st.text_area("Tulis pesan Anda disini")
if st.button("kirim Pesan")
    st.success(f"Terima Kasih {nama}! Pesan Anda
telah terkirim. Kami akan merespon Secepatnya.")
# Footer
st.markdwon("---")
st.markdwon("<center> 2026 Cahaya Komobepa -
Semua Hak Dilindungi<center>",
unsafe_allow_html=True)
