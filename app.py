import streamlit as st

# Mengatur judul halaman web
st.set_page_config(page_title="Proteksi Video Streamlit", layout="centered")

# Variabel password yang benar
PASSWORD_BENAR = "1807"  # Ganti dengan password yang Anda inginkan

# Membuat session state agar status login tersimpan saat halaman dimuat ulang
if "akses_diberikan" not in st.session_state:
    st.session_state.akses_diberikan = False

# Tampilan Halaman
st.title("🔒 Website Proteksi Video")

if not st.session_state.akses_diberikan:
    # Form Input Password jika belum login
    st.subheader("Silakan masukkan password untuk menonton")
    
    # Input password (karakter disembunyikan)
    input_user = st.text_input("Password:", type="password")
    
    tombol_submit = st.button("Putar Video")
    
    if tombol_submit:
        if input_user == PASSWORD_BENAR:
            st.session_state.akses_diberikan = True
            st.status("Memproses video...")  # Indikator loading singkat
            st.rerun() # Memuat ulang halaman untuk memunculkan video
        else:
            st.error("❌ Password salah! Silakan coba lagi.")
else:
    # Tampilan jika password BENAR
    st.success("✅ Akses diberikan! Selamat menonton.")
    
    # Membaca dan memutar video dari folder GitHub Anda
    try:
        video_file = open("video.mp4", "rb")
        video_bytes = video_file.read()
        st.video(video_bytes)
    except FileNotFoundError:
        st.error("❌ File 'video.mp4' tidak ditemukan! Pastikan Anda sudah mengunggah video ke GitHub dengan nama yang persis sama.")

    # Tombol untuk mengunci kembali video
    if st.button("Keluar / Kunci Video"):
        st.session_state.akses_diberikan = False
        st.rerun()
