import streamlit as st

# TUTAJ I TYLKO TUTAJ konfigurujemy stronę
st.set_page_config(
    page_title="PlantVerse AR",
    page_icon="🌿",
    layout="wide"
)

from plant_identification import main as plant_identifier_main
from ar_location_plant_map import main as ar_location_main

st.sidebar.title("🌱 PlantVerse Navigation")
app_choice = st.sidebar.radio("Select Module:", ["Plant Identifier", "AR + Location Explorer"])

if app_choice == "Plant Identifier":
    plant_identifier_main()
elif app_choice == "AR + Location Explorer":
    ar_location_main()