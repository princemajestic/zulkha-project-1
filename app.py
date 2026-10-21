import streamlit as str

# Mengatur judul halaman web
str.set_page_config(page_title="Proteksi Video Streamlit", layout="centered")

# Variabel password yang benar
PASSWORD_BENAR = "1807"  

# Membuat session state agar status login tersimpan saat halaman dimuat ulang oleh Streamlit
if "akses_diberikan" not in str.session_state:
    str.session_state.akses_diberikan = False

# Tampilan Halaman
str.title("🔒 Website Proteksi Video")

if not str.session_state.akses_diberikan:
    # Form Input Password jika belum login
    str.subheader("Silakan masukkan password untuk menonton")
    
    # Input password (karakter akan disembunyikan dengan bintang/titik)
    input_user = str.text_input("Password:", type="password")
    
    tombol_submit = str.button("Putar Video")
    
    if tombol_submit:
        if input_user == PASSWORD_BENAR:
            str.session_state.akses_diberikan = True
            str.rerun() # Memuat ulang halaman untuk memunculkan video
        else:
            str.error("❌ Password salah! Silakan coba lagi.")
else:
    # Tampilan jika password BENAR
    str.success("✅ Akses diberikan! Selamat menonton.")
    
    # Opsi 1: Memutar video dari file lokal yang ada di dalam folder GitHub Anda
    # Pastikan file video (misal: video.mp4) sudah di-upload ke GitHub
    try:
        video_file = open("video.mp4", "rb")
        video_bytes = video_file.read()
        str.video("https://drive.google.com/file/d/1F_f5iIAm1DLrQTgkL7XjkRg0ESoyE6lV/view?usp=drive_link")
    except FileNotFoundError:
        str.warning("File 'video.mp4' belum diunggah ke GitHub atau tidak ditemukan.")
        
    # Opsi 2: Memutar video dari Link/URL (Hapus tanda pagar '#' di bawah ini jika ingin digunakan)
    # str.video("https://youtube.com")

    # Tombol untuk mengunci kembali video
    if str.button("Keluar / Kunci Video"):
        str.session_state.akses_diberikan = False
        str.rerun()
