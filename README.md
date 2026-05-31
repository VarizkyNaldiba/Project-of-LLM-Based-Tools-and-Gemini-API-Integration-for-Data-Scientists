# Proyek Alat Berbasis LLM dan Integrasi API Gemini untuk Data Scientist

## Ringkasan
Repositori ini berisi **asisten AI pribadi** yang dibangun dengan Google Gemini dan beragam alat berbasis LLM. Proyek ini memperlihatkan cara mengintegrasikan model bahasa besar ke dalam alur kerja data‑science, menyediakan generasi kode, bantuan analisis data, dan notebook interaktif.

## Tujuan
- Menunjukkan integrasi end‑to‑end API Gemini dengan utilitas Python.
- Menyediakan komponen yang dapat dipakai ulang untuk tugas data‑science: pembersihan data, visualisasi, pemilihan model.
- Menyajikan antarmuka web (Streamlit) untuk penggunaan interaktif.

## Arsitektur
```
[Frontend Streamlit] <---> [Backend FastAPI] <---> [LLM Gemini] <---> [Perpustakaan Data‑Science (pandas, scikit‑learn, matplotlib)]
```

## Teknologi
- **Bahasa**: Python 3.11
- **LLM**: Google Gemini API
- **UI Web**: Streamlit
- **Backend**: FastAPI (opsional untuk panggilan API)
- **Data‑Science**: pandas, NumPy, scikit‑learn, matplotlib, seaborn
- **Deployment**: Docker, dapat juga dipasang di Streamlit Sharing atau Render

## Instalasi
```bash
# Clone repositori
git clone https://github.com/VarizkyNaldiba/Project-of-LLM-Based-Tools-and-Gemini-API-Integration-for-Data-Scientists.git
cd Project-of-LLM-Based-Tools-and-Gemini-API-Integration-for-Data-Scientists

# Buat lingkungan virtual
python -m venv venv
source venv/bin/activate   # di Windows: venv\\Scripts\\activate

# Pasang dependensi
pip install -r requirements.txt

# Siapkan kunci API Gemini (buat file .env)
cp .env.example .env

# Jalankan aplikasi Streamlit
streamlit run app.py
```

## Cara Pakai
1. Masukkan kunci API Gemini Anda pada UI atau file `.env`.
2. Pilih tugas yang diinginkan (mis. *pembersihan data*, *visualisasi*, *saran model*).
3. Interaksikan dengan LLM untuk menghasilkan cuplikan kode, penjelasan, atau notebook.
4. Ekspor kode atau notebook yang dihasilkan untuk penggunaan lebih lanjut.

## Hasil
- Asisten AI yang lengkap dapat menghasilkan pipeline pandas, membuat grafik, dan menyarankan model ML.
- Integrasi dengan Gemini berhasil ditampilkan dalam skenario data‑science nyata.
- Pengguna dapat membuat prototipe analisis dalam hitungan menit.

## Pengembangan Selanjutnya
- Menambahkan kemampuan multi‑modal (gambar‑ke‑teks untuk data visual).
- Memperluas dukungan ke bahasa R dan Julia.
- Menyediakan layanan SaaS terkelola dengan otentikasi pengguna.

## Lisensi
MIT © Varizky Naldiba


## Overview
This repository houses a **personal AI assistant** built with Google Gemini and various LLM‑based tools. It demonstrates how to integrate large language models into data‑science workflows, providing code generation, data‑analysis assistance, and interactive notebooks.

## Objectives
- Showcase end‑to‑end integration of Gemini API with Python utilities.
- Offer reusable components for data‑science tasks: data cleaning, visualization, model selection.
- Provide a web interface (Streamlit) for interactive usage.

## Architecture
```
[Streamlit Frontend] <---> [FastAPI Backend] <---> [Gemini LLM] <---> [Data‑Science Libraries (pandas, sklearn, matplotlib)]
```
*(Replace with actual diagram when available.)*

## Tech Stack
- **Language**: Python 3.11
- **LLM**: Google Gemini API
- **Web UI**: Streamlit
- **Backend**: FastAPI (optional for API calls)
- **Data Science**: pandas, NumPy, scikit‑learn, matplotlib, seaborn
- **Deployment**: Docker, optionally Streamlit Sharing / Render

## Installation
```bash
# Clone the repo
git clone https://github.com/VarizkyNaldiba/Project-of-LLM-Based-Tools-and-Gemini-API-Integration-for-Data-Scientists.git
cd Project-of-LLM-Based-Tools-and-Gemini-API-Integration-for-Data-Scientists
# Create virtual environment
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
# Install dependencies
pip install -r requirements.txt
# Set Gemini API key (create .env file)
cp .env.example .env
# Run the Streamlit app
streamlit run app.py
```

## Usage
1. Enter your Gemini API key in the UI or `.env` file.
2. Choose a task (e.g., *data cleaning*, *visualization*, *model suggestion*).
3. Interact with the LLM to generate code snippets, explanations, or notebooks.
4. Export generated code or notebooks for further work.

## Results
- Fully functional AI assistant that can generate pandas pipelines, plot charts, and suggest ML models.
- Demonstrated integration with Gemini in a real‑world data‑science scenario.
- Users can prototype analyses within minutes.

## Future Work
- Add multi‑modal capabilities (image‑to‑text for visual data).
- Expand to support R and Julia code generation.
- Deploy as a managed SaaS with user authentication.

## License
MIT © Varizky Naldiba
