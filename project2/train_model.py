# train_model.py

import math
import pandas as pd
from geopy.geocoders import Nominatim

# Function to geocode a city name and return its latitude and longitude
def geocode_city(city_name):
    geolocator = Nominatim(user_agent="hospital_locator")
    location = geolocator.geocode(city_name)
    
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Haversine formula to calculate distance between two lat/lng points
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in km
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c  # Result in kilometers
    return distance

# Function to load hospital data from a CSV file
def load_hospital_data(file_path):
    # Load the dataset using pandas
    df = pd.read_csv(file_path)
    
    # Extract relevant columns: name, latitude, and longitude
    hospitals = []
    for _, row in df.iterrows():
        hospital = {
            'name': row['name'],  # Replace with the correct column name from the dataset
            'lat': row['latitude'],  # Replace with the correct column name from the dataset
            'lon': row['longitude']  # Replace with the correct column name from the dataset
        }
        hospitals.append(hospital)
    return hospitals

# Function to find all hospitals within a specified radius
def find_hospitals_within_radius(user_lat, user_lon, hospitals, radius_km=50):
    hospitals_within_radius = []
    
    for hospital in hospitals:
        distance = haversine(user_lat, user_lon, hospital['lat'], hospital['lon'])
        
        # If the distance is within the radius, add the hospital to the list
        if distance <= radius_km:
            hospitals_within_radius.append({
                'hospital': hospital,
                'distance': distance
            })
    
    return hospitals_within_radius
