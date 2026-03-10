import streamlit as st
import pandas as pd

# --- CONFIG ---
st.set_page_config(page_title="Data Rekap SPM", layout="wide")

st.title("Data Rekap SPM 2025 BPS Kabupaten Banyumas")

# --- AMBIL DATA DARI GOOGLE SHEET ---
# Ganti link berikut dengan link CSV dari Google Spreadsheet
# Caranya: File -> Share -> Publish to web -> pilih CSV
sheet_url = "https://docs.google.com/spreadsheets/d/1WJR1tCiYRCJYbvfcW8fMySuqzG55QoHdsI7gZsiN_a0/export?format=csv"
df = pd.read_csv(sheet_url)

# --- FITUR PENCARIAN ---
search = st.text_input("Cari Data:", placeholder="Ketik judul pencairan/nomor SPM/nomor FP")

if search:
    df_filtered = df[df.astype(str).apply(lambda x: x.str.contains(search, case=False)).any(axis=1)]
else:
    df_filtered = df

# --- TAMPILKAN TABEL ---
st.dataframe(df_filtered, use_container_width=True)


