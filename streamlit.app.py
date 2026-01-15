import streamlit as st
from supabase import create_client

# 1️⃣ Połączenie z Supabase
SUPABASE_URL = "https://ahlsfzbzuvfoxvfjwcep.supabase.co"
SUPABASE_KEY = "sb_publishable_TdCmBYcq2Bc3lorekcsZsA_p-oIi_sT"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# 2️⃣ Funkcje do bazy danych
def get_categories():
    ...

def get_products(category_id):
    ...

# 3️⃣ UI Streamlit
st.title("Aplikacja magazynowa")
...
def get_categories():
    return supabase.table("categories").select("*").execute().data


def get_products(category_id):
    return (
        supabase
        .table("products")
        .select("*")
        .eq("category_id", category_id)
        .execute()
        .data
    )
    def add_product(name, category_id):
     supabase.table("products").insert({
        "name": name,
        "category_id": category_id
    }).execute()


def delete_product(product_id):
    supabase.table("products").delete().eq("id", product_id).execute()
    st.title("📦 Aplikacja magazynowa")

categories = get_categories()
category_dict = {c["name"]: c["id"] for c in categories}

selected_category = st.selectbox(
    "Wybierz kategorię",
    category_dict.keys()
)

category_id = category_dict[selected_category]

products = get_products(category_id)

st.subheader("Produkty:")
for product in products:
    col1, col2 = st.columns([3, 1])
    col1.write(product["name"])
    if col2.button("Usuń", key=product["id"]):
        delete_product(product["id"])
        st.experimental_rerun()

st.subheader("➕ Dodaj produkt")
new_product = st.text_input("Nazwa produktu")

if st.button("Dodaj"):
    add_product(new_product, category_id)
    st.experimental_rerun()
