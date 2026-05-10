import streamlit as st
from google import genai
from google.genai import types

# Konfigurasi Halaman (Harus dipanggil pertama kali)
st.set_page_config(
    page_title="Konsultan F&B RM Padang",
    layout="centered"
)

# Kustomisasi CSS untuk detail kecil (Bordur tombol & warna avatar chat)
st.markdown("""
<style>
    /* Agar tombol memiliki aksen emas khas Minang */
    .stButton>button {
        border: 1px solid #DAA520 !important;
    }
    
    /* Kustomisasi Chat Bubble Assistant */
    [data-testid="chatAvatarIcon-assistant"] {
        background-color: #C62828;
        color: #FFD700;
    }
    
    /* Kustomisasi Chat Bubble User */
    [data-testid="chatAvatarIcon-user"] {
        background-color: #DAA520;
    }
</style>
""", unsafe_allow_html=True)

# API Key Default secara Aman (Secure Fetching)
import os
from dotenv import load_dotenv

# Muat variabel dari .env (untuk lingkungan lokal)
load_dotenv()

# Coba ambil API Key dari Streamlit Secrets (untuk Cloud) atau dari environment variables (.env lokal)
try:
    DEFAULT_API_KEY = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY", ""))
except Exception:
    DEFAULT_API_KEY = os.getenv("GOOGLE_API_KEY", "")

st.markdown("<h2 style='text-align: center; font-size: 28px;'>Konsultan Pribadi RM Padang </h2>", unsafe_allow_html=True)
st.caption("Asisten pintar untuk mengelola bisnis F&B Rumah Makan Padang Anda. Mengatur HPP, Stok, Pemasaran, hingga Operasional.")
st.divider()

# --- SIDEBAR PENGATURAN ---
with st.sidebar:
    st.markdown("<h3 style='font-size: 20px;'>Pengaturan Bisnis</h3>", unsafe_allow_html=True)
    
    # Input API Key
    api_key_input = st.text_input("Google AI API Key", value=DEFAULT_API_KEY, type="password")
    
    # Pemilihan Topik Konsultasi
    st.markdown("<h4 style='font-size: 16px; margin-top: 15px;'>Pilih Fokus Konteks</h4>", unsafe_allow_html=True)
    topik = st.selectbox(
        "Konteks Saat Ini:",
        (
            "Diskusi Umum",
            "Analisis HPP & Penentuan Harga Menu",
            "Manajemen Stok & Minimalisir Sisa Makanan",
            "Operasional ",
            "Strategi Pemasaran & Paket Catering",
            "Manajemen SDM & Pembagian Shift",
            "Manajemen Suplier & Harga Bahan Pokok",
            "Sistem Kasir & Pembukuan Keuangan",
            "Inovasi Menu Tambahan & Varian Sambal",
            "Pembukaan Cabang Baru & Analisis Lokasi"
        )
    )
    
    st.divider()
    reset_btn = st.button("Reset Percakapan")

# --- VALIDASI API KEY ---
if not api_key_input:
    st.warning("Silakan masukkan API Key di sidebar untuk mulai berkonsultasi.")
    st.stop()

# --- SYSTEM INSTRUCTION (PERSONA) ---
system_instruction = (
    "Anda adalah pakar bisnis F&B dan konsultan spesialis restoran kuliner Nusantara, "
    "khususnya Rumah Makan Padang / Minangkabau. Anda mengerti konsep HPP (Harga Pokok Penjualan), "
    "manajemen bahan baku (santan, daging sapi, rempah-rempah), efisiensi sisa makanan (food waste), "
    "dan perbedaan strategi operasional seperti 'Sistem Hidang' (nasi padang yang dihidangkan di piring kecil-kecil di meja) "
    "dan 'Sistem Rames' (pesan langsung di etalase kaca).\n"
    "Gunakan bahasa Indonesia yang profesional, ramah, dan solutif. Gunakan sentuhan kearifan lokal "
    "dan istilah-istilah lazim dalam operasional RM Padang jika relevan. Jika ditanya mengenai keuangan, "
    "berikan rasio kasaran yang masuk akal di industri ini."
)

# --- INISIALISASI GEMINI CLIENT ---
if ("genai_client" not in st.session_state) or (getattr(st.session_state, "_last_key", None) != api_key_input):
    try:
        st.session_state.genai_client = genai.Client(api_key=api_key_input)
        st.session_state._last_key = api_key_input
        st.session_state.pop("chat", None)
        st.session_state.pop("messages", None)
    except Exception as e:
        st.error(f"Gagal memuat API Key: {e}")
        st.stop()

# --- INISIALISASI CHAT SESSION ---
if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.genai_client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.7
        )
    )

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo, Sanak! Saya siap membantu mengembangkan bisnis Rumah Makan Padang Anda. Mau diskusi tentang apa hari ini?"}
    ]

# --- RESET CHAT ---
if reset_btn:
    st.session_state.pop("chat", None)
    st.session_state.pop("messages", None)
    st.rerun()

# --- TAMPILKAN HISTORI CHAT ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- INPUT USER ---
prompt = st.chat_input("Tanya soal HPP rendang, promosi, atau cara kelola sisa lauk...")

if prompt:
    # Sisipkan konteks topik (tersembunyi dari tampilan user jika perlu, namun untuk ini kita tampilkan saja
    # atau ubah prompt internal yang dikirim ke Gemini)
    if topik != "Diskusi Umum":
        internal_prompt = f"[Konteks Topik: {topik}]\n{prompt}"
    else:
        internal_prompt = prompt

    # Tampilkan prompt asli di layar user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Kirim prompt internal ke Gemini
    try:
        response = st.session_state.chat.send_message(internal_prompt)
        if hasattr(response, "text"):
            answer = response.text
        else:
            answer = str(response)
    except Exception as e:
        answer = f"Maaf, terjadi kesalahan saat menghubungi AI: {e}"
        
    # Tampilkan respons AI
    with st.chat_message("assistant"):
        st.markdown(answer)
        
    st.session_state.messages.append({"role": "assistant", "content": answer})
