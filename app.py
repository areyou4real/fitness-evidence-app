import streamlit as st
from db.schema import create_schema
from db.seed import seed_exercises

create_schema()
seed_exercises()

st.set_page_config(page_title="Fitness Evidence App", layout="wide")

st.title("Fitness Evidence App")
st.write("Streamlit setup complete.")
