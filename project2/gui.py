# gui.py

import tkinter as tk
from tkinter import messagebox
from train_model import geocode_city, find_hospitals_within_radius, load_hospital_data

# Load hospital data from CSV file
hospitals_data = load_hospital_data("hospitals.csv")  # Path to your downloaded Kaggle dataset

# Function to handle user input and call the model
def on_find_hospitals_button_click():
    city_name = city_entry.get()  # Get the city name from the entry field
    radius = radius_entry.get()  # Get the radius from the entry field
    
    try:
        radius_km = float(radius)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric value for the radius.")
        return
    
    # Geocode the city to get latitude and longitude
    user_lat, user_lon = geocode_city(city_name)
    
    if user_lat is None or user_lon is None:
        messagebox.showerror("City Error", "Could not find the city. Please check the name and try again.")
    else:
        # Find all hospitals within the specified radius
        hospitals_within_radius = find_hospitals_within_radius(user_lat, user_lon, hospitals_data, radius_km)
        
        if hospitals_within_radius:
            result_text = f"Hospitals within {radius_km} km of {city_name}:\n"
            for hospital in hospitals_within_radius:
                result_text += f"{hospital['hospital']['name']} - {hospital['distance']:.2f} km\n"
            result_label.config(text=result_text)
        else:
            result_label.config(text=f"No hospitals found within {radius_km} km of {city_name}.")

# GUI: Set up the main window
window = tk.Tk()
window.title("Hospital Locator")

# Label and input field for city name
city_label = tk.Label(window, text="Enter City Name (e.g., Nairobi):")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

# Label and input field for radius
radius_label = tk.Label(window, text="Enter Radius (in km):")
radius_label.pack()

radius_entry = tk.Entry(window)
radius_entry.pack()

# Button to find hospitals within the radius
find_button = tk.Button(window, text="Find Hospitals", command=on_find_hospitals_button_click)
find_button.pack()

# Label to display the result
result_label = tk.Label(window, text="Hospitals within the radius will be shown here.")
result_label.pack()

# Run the GUI application
window.mainloop()
