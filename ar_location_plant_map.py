import streamlit as st
import requests
import math
from typing import Dict, List, Optional, Tuple

class PlantLocationFinder:
    def __init__(self):
        self.inaturalist_base_url = "https://api.inaturalist.org/v1"
        self.ipinfo_url = "http://ip-api.com/json"

    def get_user_location(self) -> Optional[Tuple[float, float]]:
        try:
            response = requests.get(self.ipinfo_url, timeout=5)
            data = response.json()
            return data.get("lat"), data.get("lon")
        except:
            return None

    def search_plant_species(self, plant_name: str) -> Optional[Dict]:
        try:
            url = f"{self.inaturalist_base_url}/taxa"
            params = {'q': plant_name, 'rank': 'species', 'per_page': 1}
            response = requests.get(url, params=params)
            results = response.json().get('results', [])
            return results[0] if results else None
        except:
            return None

    def get_plant_observations(self, taxon_id: int, lat: float, lon: float, radius: int = 50):
        url = f"{self.inaturalist_base_url}/observations"
        params = {
            'taxon_id': taxon_id, 'lat': lat, 'lng': lon, 
            'radius': radius, 'per_page': 10, 'photos': 'true', 'geo': 'true'
        }
        return requests.get(url, params=params).json().get('results', [])

def main():
    st.title("🗺️ Plant Discovery Map")
    st.markdown("Find where specific plants have been spotted near you.")

    finder = PlantLocationFinder()
    
    with st.sidebar:
        st.header("Search Settings")
        plant_name = st.text_input("Plant Name", value="Lavender")
        radius = st.slider("Search Radius (km)", 1, 100, 25)
        
        loc_method = st.radio("Location Method", ["Auto-detect", "Manual"])
        lat, lon = None, None
        
        if loc_method == "Auto-detect":
            if st.button("Get My Location"):
                lat, lon = finder.get_user_location()
                if lat: st.success(f"Found: {lat}, {lon}")
        else:
            lat = st.number_input("Lat", value=52.2297)
            lon = st.number_input("Lon", value=21.0122)

    if st.button("Find Nearby Plants", type="primary"):
        if not lat or not lon:
            st.error("Please provide coordinates.")
            return

        with st.spinner("Searching iNaturalist database..."):
            species = finder.search_plant_species(plant_name)
            if species:
                obs = finder.get_plant_observations(species['id'], lat, lon, radius)
                if obs:
                    st.success(f"Found {len(obs)} observations of {species['name']}")
                    for o in obs:
                        with st.expander(f"📍 {o.get('place_guess', 'Unknown Location')}"):
                            col1, col2 = st.columns(2)
                            with col1:
                                st.write(f"**Date:** {o.get('observed_on_string')}")
                                st.write(f"**Accuracy:** {o.get('quality_grade')}")
                                st.markdown(f"[View on iNaturalist]({o.get('uri')})")
                            with col2:
                                if o.get('photos'):
                                    st.image(o['photos'][0]['url'].replace('square', 'medium'))
                else:
                    st.warning("No sightings found in this area.")
            else:
                st.error("Species not found.")

if __name__ == "__main__":
    main()