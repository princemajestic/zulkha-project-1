import streamlit as st

# Mengatur judul halaman web
st.set_page_config(page_title="Proteksi Video Streamlit", layout="centered")

# Variabel password yang benar
PASSWORD_BENAR = "1807"  # Ganti dengan password yang Anda inginkan

# Masukkan ID video Google Drive Anda di bawah ini
# Contoh: jika link Anda https://google.com, maka ID-nya adalah 1A2B3C4D5E
ID_VIDEO_GD = "1F_f5iIAm1DLrQTgkL7XjkRg0ESoyE6lV" 
LINK_DIRECT_GD = f"https://drive.google.com/uc?id={ID_VIDEO_GD}"

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
            st.rarun() if hasattr(st, 'rarun') else st.rerun() # Mengatasi pembaruan metode Streamlit
        else:
            st.error("❌ Password salah! Silakan coba lagi.")
else:
    # Tampilan jika password BENAR
    st.success("✅ Akses diberikan! Selamat menonton.")
    
    # Memutar video langsung menggunakan link eksternal Google Drive
    st.video(LINK_DIRECT_GD)

    # Tombol untuk mengunci kembali video
    if st.button("Keluar / Kunci Video"):
        st.session_state.akses_diberikan = False
        st.rarun() if hasattr(st, 'rarun') else st.rerun()
