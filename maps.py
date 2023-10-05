import streamlit as st
import requests
from geopy.geocoders import Nominatim
from geopy import distance
import pandas as pd

MAPBOX_API_KEY = "sk.eyJ1IjoiaXNoYWFuMTMxMyIsImEiOiJjbGhoY21yMzQyZWh0M2ZudWdlMnk5cHE1In0.xfIE3yTkzMCvXyCP_DTDCg"

# Geocoding function to obtain latitude and longitude
def geocode_location(location):
    geolocator = Nominatim(user_agent="hospital-finder")
    location_data = geolocator.geocode(location)
    return location_data.latitude, location_data.longitude

# Function to fetch hospital data near the given coordinates
def fetch_hospitals(latitude, longitude):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/hospital.json?proximity={longitude},{latitude}&access_token={MAPBOX_API_KEY}"
    response = requests.get(url)
    data = response.json()
    hospitals = data.get("features", [])
    return hospitals

# Main Streamlit app code
def main():
    st.title("Hospital Finder")

    # Get user location
    location = st.text_input("Enter your location:")
    if not location:
        st.warning("Please enter a location.")
        return

    # Obtain latitude and longitude
    try:
        latitude, longitude = geocode_location(location)
    except:
        st.error("Error occurred while geocoding. Please try again.")
        return

    # Fetch hospitals near the given location
    hospitals = fetch_hospitals(latitude, longitude)

    # Display hospital information
    if not hospitals:
        st.warning("No hospitals found near your location.")
    else:
        st.success(f"Found {len(hospitals)} hospitals near your location.")

        # Prepare the hospital data for mapping
        hospital_data = []
        for hospital in hospitals:
            name = hospital.get("text", "")
            hospital_center = hospital.get("center", [])
            if len(hospital_center) == 2:
                hospital_data.append({"name": name, "latitude": hospital_center[1], "longitude": hospital_center[0]})

        # Display the map centered at the specified location
        if hospital_data:
            df = pd.DataFrame(hospital_data)
            st.map(df)

        for hospital in hospital_data:
            name = hospital["name"]
            address = ", ".join(hospital.get("place_name", "").split(",")[:-2])
            distance_to_hospital = distance.distance((latitude, longitude), (hospital["latitude"], hospital["longitude"])).kilometers
            st.write(f"- {name}")
            st.write(f"  Address: {address}")
            st.write(f"  Distance: {distance_to_hospital:.2f} km")

if __name__ == "__main__":
    main()
