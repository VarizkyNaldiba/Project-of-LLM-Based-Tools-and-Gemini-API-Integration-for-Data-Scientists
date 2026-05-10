# Flow Logic of Store_chatbot

# Streamlit for Chatbot — Materi Training

Source repo: [adiptamartulandi/chatbot-streamlit-demo](https://github.com/adiptamartulandi/chatbot-streamlit-demo)

## Apa itu Streamlit?

**Streamlit** adalah framework Python open-source yang memungkinkan kamu membangun web app interaktif hanya dengan Python — tanpa perlu HTML, CSS, atau JavaScript sama sekali.

Cukup tulis skrip Python biasa, dan Streamlit akan otomatis mengubahnya menjadi tampilan web yang interaktif.

Ini sangat cocok untuk:
- Demo model machine learning
- Dashboard data
- Aplikasi chatbot berbasis LLM
- Prototipe cepat yang bisa langsung dibagikan ke orang lain

## Kenapa Streamlit untuk Chatbot?

| Pendekatan | Kompleksitas | Kecepatan build |
|---|---|---|
| Flask + HTML/JS | Tinggi | Lama |
| FastAPI + React | Sangat tinggi | Sangat lama |
| **Streamlit** | Rendah | Cepat (menit) |

Streamlit punya `st.chat_message()` dan `st.chat_input()` yang dirancang khusus untuk membangun antarmuka chatbot dengan sedikit baris code.

## Struktur Notebook Ini

Notebook ini dibagi menjadi tiga bagian:

1. **Setup** — install Streamlit dan konfigurasi ngrok untuk menjalankan di Google Colab
2. **Part 1: Komponen Dasar Streamlit** — pengenalan elemen-elemen UI yang tersedia
3. **Part 2: Chatbot dengan Gemini** — membangun chatbot lengkap dengan session state dan Gemini API

## Kenapa Pakai ngrok?

Google Colab tidak punya IP publik. Streamlit berjalan di port 8501 di dalam server Colab,
tapi kita tidak bisa mengaksesnya langsung dari browser.

**ngrok** membuat "tunnel" dari internet ke port tersebut — sehingga app kamu bisa diakses
via URL publik tanpa install apapun di komputer lokal.

```
Browser kamu
    ↕  (HTTPS)
  ngrok server  ←→  tunnel  ←→  Google Colab (port 8501)
                                       ↕
                               Streamlit app berjalan
```


---

## Setup: Install Library & Konfigurasi ngrok

### Step 1 — Install Streamlit dan pyngrok

---

### Step 2 — Daftarkan ngrok Auth Token

Cara mendapatkan token:
1. Daftar gratis di [https://ngrok.com](https://ngrok.com)
2. Login → klik **Your Authtoken** di dashboard
3. Copy token-nya, paste ke Colab Secrets dengan nama `NGROK_TOKEN`
   (klik ikon 🔑 di sidebar kiri Colab)

> Token ngrok gratis sudah cukup untuk keperluan training.
> Satu akun ngrok bisa membuka 1 tunnel aktif sekaligus.

---

### Fungsi Helper: Jalankan Streamlit + Buka Tunnel

Kita buat fungsi reusable yang akan kita pakai berulang kali di setiap bagian.
Fungsi ini melakukan tiga hal:
1. Menulis file `.py` ke disk
2. Menjalankan `streamlit run` di background
3. Membuka tunnel ngrok dan menampilkan URL publik

---

---

# Part 1: Komponen Dasar Streamlit

Sebelum membangun chatbot, kita pelajari dulu elemen-elemen UI yang tersedia di Streamlit.
Sumber: `streamlit_app_basic.py` dari repo demo.

## Cara Kerja Streamlit

Streamlit bekerja dengan model yang unik: **setiap kali user berinteraksi dengan UI
(klik tombol, geser slider, ketik input), seluruh skrip Python dijalankan ulang dari atas ke bawah.**

Ini berbeda dengan framework web tradisional. Karena itulah kita nanti butuh `st.session_state`
untuk menyimpan data yang tidak boleh hilang saat skrip dijalankan ulang.

## Elemen-elemen UI Utama

### Teks & Judul
- `st.title()` — judul halaman (paling besar)
- `st.header()` — sub-judul
- `st.subheader()` — sub-sub-judul
- `st.write()` — teks biasa, bisa juga menerima dataframe, chart, dll
- `st.markdown()` — teks dengan format Markdown

### Input dari User
- `st.text_input()` — kotak teks satu baris
- `st.text_area()` — kotak teks multi baris
- `st.button()` — tombol klik
- `st.checkbox()` — toggle on/off
- `st.selectbox()` — dropdown pilihan
- `st.slider()` — slider angka
- `st.file_uploader()` — upload file

### Layout
- `st.sidebar` — panel samping yang bisa disembunyikan
- `st.columns()` — bagi halaman jadi beberapa kolom
- `st.expander()` — section yang bisa dilipat/dibuka

### Notifikasi
- `st.success()` — pesan hijau (berhasil)
- `st.info()` — pesan biru (informasi)
- `st.warning()` — pesan kuning (peringatan)
- `st.error()` — pesan merah (error)

### Data & Chart
- `st.dataframe()` — tabel interaktif
- `st.line_chart()`, `st.bar_chart()`, `st.area_chart()` — chart bawaan Streamlit
- `st.pyplot()` — tampilkan chart Matplotlib

Mari kita tulis dan jalankan file demo-nya:

---

Setelah file ditulis, jalankan dengan ngrok:

---

### Yang Perlu Diperhatikan

Coba berinteraksi dengan semua komponen di app yang baru terbuka. Perhatikan bahwa:

1. **Setiap interaksi menyebabkan skrip jalan ulang** — Progress bar akan berputar lagi setiap kali kamu klik sesuatu. Ini adalah perilaku normal Streamlit.
2. **Sidebar bisa disembunyikan** — klik panah kecil di pojok kiri atas app.
3. **Chart otomatis responsif** — coba resize jendela browser.

Untuk menghentikan app dan menjalankan app berikutnya, jalankan cell di bawah:

---

---

# Part 2: Chatbot dengan Gemini

Sekarang kita masuk ke bagian utama — membangun chatbot berbasis LLM menggunakan Streamlit + Gemini API.
Sumber: `streamlit_chat_app.py` dari repo demo.

## Konsep Kunci: st.session_state

Ini adalah konsep paling penting untuk memahami cara kerja chatbot di Streamlit.

Ingat bahwa Streamlit menjalankan ulang seluruh skrip setiap kali ada interaksi.
Ini artinya semua variabel Python akan di-reset ke nilai awal setiap kali user kirim pesan.

**Masalah:** Kalau pesan-pesan chat disimpan di variabel biasa, semua pesan akan hilang setiap kali user mengetik sesuatu!

**Solusi:** `st.session_state` adalah dictionary khusus yang **nilainya tetap tersimpan** meskipun skrip dijalankan ulang.

```python
# Variabel biasa — akan HILANG setiap rerun
messages = []

# st.session_state — akan BERTAHAN setiap rerun  
st.session_state.messages = []
```

Di chatbot kita, `st.session_state` digunakan untuk menyimpan:
- `messages` — riwayat semua pesan (user + assistant)
- `chat` — objek chat session dari Gemini API (menyimpan konteks percakapan)
- `genai_client` — client Gemini yang sudah terinisialisasi
- `_last_key` — API key terakhir yang dipakai (untuk deteksi perubahan key)

## Komponen Chat Khusus Streamlit

```python
# Menampilkan bubble chat — role bisa "user" atau "assistant"
with st.chat_message("user"):
    st.markdown("pesan dari user")

with st.chat_message("assistant"):
    st.markdown("jawaban dari AI")

# Kotak input di bagian bawah halaman
prompt = st.chat_input("Ketik pesanmu...")
```

## Alur Logic Chatbot

```
Skrip dijalankan (setiap interaksi)
         ↓
Cek API key di sidebar
         ↓
Inisialisasi client & chat session (hanya kalau belum ada di session_state)
         ↓
Tampilkan semua pesan dari st.session_state.messages
         ↓
Tunggu input dari st.chat_input()
         ↓
User kirim pesan?
   ↓ Ya
Tambah pesan user ke messages
Tampilkan bubble user
Kirim ke Gemini API
Tampilkan bubble assistant
Tambah jawaban ke messages
   ↓
Kembali ke atas (skrip dijalankan ulang)
```

## Cara Mendapatkan Google AI API Key

1. Buka [https://aistudio.google.com](https://aistudio.google.com)
2. Klik **Get API Key** → **Create API Key**
3. Copy key-nya
4. Di app Streamlit nanti, paste langsung ke kotak "Google AI API Key" di sidebar

> Key tidak perlu disimpan di Colab Secrets — user memasukkannya langsung di UI app.

---

Jalankan chatbot-nya:

---

### Panduan Mencoba App

1. Buka URL yang muncul di atas
2. Di sidebar, masukkan Google AI API Key kamu
3. Mulai chat di kotak input bagian bawah
4. Coba tanya beberapa pertanyaan — perhatikan bahwa model **mengingat konteks** percakapan sebelumnya
5. Klik **Reset Percakapan** di sidebar — konteks akan hilang dan chat mulai dari awal

### Yang Bisa Dikustomisasi

Coba modifikasi file `streamlit_chat_app.py` untuk:

- **Ganti model** — ubah `"gemini-2.5-flash"` ke `"gemini-2.5-flash-lite"` atau model lain
- **Tambah system prompt** — saat membuat chat session, tambahkan:
  ```python
  st.session_state.chat = st.session_state.genai_client.chats.create(
      model="gemini-2.5-flash",
      config={"system_instruction": "Kamu adalah asisten yang selalu menjawab dalam Bahasa Indonesia"}
  )
  ```
- **Tambah parameter** di sidebar — misalnya slider untuk temperature

---

---

## Menghentikan App

Jalankan cell di bawah untuk menghentikan Streamlit dan menutup tunnel ngrok.

---

## Ringkasan

| Konsep | Penjelasan |
|---|---|
| `%%writefile` | Magic command Colab untuk menulis konten cell ke file di disk |
| `subprocess.Popen` | Menjalankan proses (Streamlit) di background tanpa memblokir notebook |
| `ngrok.connect()` | Membuat URL publik yang mengarah ke port lokal |
| `st.session_state` | Dictionary yang nilainya bertahan meskipun skrip dijalankan ulang |
| `st.chat_message()` | Membuat bubble chat dengan role user/assistant |
| `st.chat_input()` | Kotak input yang muncul di bagian bawah halaman |
| `st.stop()` | Menghentikan eksekusi skrip di titik tersebut |
| `st.rerun()` | Memaksa Streamlit me-refresh halaman dari awal |

## Referensi

- [Dokumentasi Streamlit](https://docs.streamlit.io)
- [Streamlit Chat Elements](https://docs.streamlit.io/develop/api-reference/chat)
- [Session State](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state)
- [Repo Demo](https://github.com/adiptamartulandi/chatbot-streamlit-demo)
