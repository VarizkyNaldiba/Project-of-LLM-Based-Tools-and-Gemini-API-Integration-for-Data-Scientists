import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Streamlit Basic Tutorial")

st.write("Ini adalah demo komponen-komponen dasar yang tersedia di Streamlit.")
st.write("Setiap section di bawah menunjukkan cara kerja satu komponen.")

st.header("1. Text Input")
user_input = st.text_input("Masukkan namamu", "Ketik di sini...")

st.header("2. Button")
if st.button("Klik aku!"):
    st.write("Tombol diklik!")

st.header("3. Checkbox")
show_content = st.checkbox("Tampilkan pesan rahasia")
if show_content:
    st.write("Pesan rahasia: kamu keren!")

st.header("4. Selectbox")
option = st.selectbox("Pilih warna favoritmu", ("Merah", "Biru", "Hijau", "Kuning"))

st.header("5. Slider")
age = st.slider("Berapa umurmu?", 0, 100, 25)

st.header("6. Progress Bar")
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)

st.header("7. Sidebar")
with st.sidebar:
    st.header("Panel Samping")
    if st.button("Tombol di Sidebar"):
        st.write("Sidebar diklik!")

st.header("8. Columns")
col1, col2 = st.columns(2)
with col1:
    st.button("Tombol di kolom kiri")
with col2:
    st.button("Tombol di kolom kanan")

st.header("9. Status Messages")
st.success("Ini pesan sukses!")
st.info("Ini pesan informasi")
st.warning("Ini pesan peringatan")
st.error("Ini pesan error")

st.header("10. Charts")

st.subheader("Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Metrik A", "Metrik B", "Metrik C"]
)
st.line_chart(chart_data)

st.subheader("Bar Chart")
bar_data = pd.DataFrame(
    {"Apel": [10, 25, 18, 30], "Mangga": [15, 12, 22, 8]},
    index=["Jan", "Feb", "Mar", "Apr"]
)
st.bar_chart(bar_data)

st.header("11. Dataframe & Tabel")
data = {
    "Nama":  ["Alice", "Bob", "Charlie", "Diana"],
    "Skor":  [88, 72, 95, 80],
    "Level": ["A", "B", "A+", "A"],
}
df = pd.DataFrame(data)
st.dataframe(df)
