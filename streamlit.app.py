import streamlit as st
import pandas as pd
import psycopg2

st.set_page_config(page_title="Program magazynowy", layout="wide")

# --- POŁĄCZENIE Z BAZĄ SUPABASE (POSTGRESQL) ---
conn = psycopg2.connect(
    host=st.secrets["database"]["host"],
    database="postgres",
    user=st.secrets["database"]["user"],
    password=st.secrets["database"]["password"],
    port=st.secrets["database"]["port"]
)

st.title("📦 Program magazynowy")

query = """
SELECT
    p.nazwa AS produkt,
    k.nazwa AS kategoria,
    p.ilosc,
    p.cena
FROM produkty p
JOIN kategorie k ON p.kategoria_id = k.id
ORDER BY k.nazwa, p.nazwa
"""

df = pd.read_sql(query, conn)
st.dataframe(df, use_container_width=True)

