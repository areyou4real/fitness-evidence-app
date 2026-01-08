import streamlit as st
from db.schema import create_schema

create_schema()

st.set_page_config(page_title="Fitness Evidence App", layout="wide")

st.title("Fitness Evidence App")
st.write("Streamlit setup complete.")

import sqlite3
from db.connection import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
st.write(cursor.fetchall())
