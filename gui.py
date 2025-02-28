import pandas as pd
import joblib
import tkinter as tk
from tkinter import ttk

# Load the trained model
def load_model():
    model = joblib.load('machine_failure_model.pkl')
    return model

# Predict function
def predict_failure():
    model = load_model()
    
    # Create input data with the correct feature names
    input_data = {
        'Air temperature [K]': [float(entry_air_temp.get())],
        'Process temperature [K]': [float(entry_process_temp.get())],
        'Rotational speed [rpm]': [float(entry_rotation_speed.get())],
        'Torque [Nm]': [float(entry_torque.get())],
        'Tool wear [min]': [float(entry_tool_wear.get())]
    }
    
    # Convert input data to DataFrame
    input_df = pd.DataFrame(input_data)
    
    # Make prediction
    prediction = model.predict(input_df)
    
    # Display result
    result_label.config(text=f'Predicted machine failure: {prediction[0]}')

# GUI setup
root = tk.Tk()
root.title('Machine Failure Prediction')
root.geometry("600x400")  # Set the window size

# Define a custom style
style = ttk.Style()
style.configure("TFrame", background="#f2f2f2")
style.configure("TLabel", background="#f2f2f2", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TEntry", font=("Helvetica", 12), padding=5)

# Create the main frame
frame = ttk.Frame(root, padding="20 20 20 20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Add a title label
title_label = ttk.Label(frame, text="Machine Failure Prediction", font=("Helvetica", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Labels and entry fields for inputs
ttk.Label(frame, text="Air temperature (K)").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_air_temp = ttk.Entry(frame)
entry_air_temp.grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Process temperature (K)").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_process_temp = ttk.Entry(frame)
entry_process_temp.grid(row=2, column=1, pady=5)

ttk.Label(frame, text="Rotational speed (rpm)").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_rotation_speed = ttk.Entry(frame)
entry_rotation_speed.grid(row=3, column=1, pady=5)

ttk.Label(frame, text="Torque (Nm)").grid(row=4, column=0, sticky=tk.W, pady=5)
entry_torque = ttk.Entry(frame)
entry_torque.grid(row=4, column=1, pady=5)

ttk.Label(frame, text="Tool wear (min)").grid(row=5, column=0, sticky=tk.W, pady=5)
entry_tool_wear = ttk.Entry(frame)
entry_tool_wear.grid(row=5, column=1, pady=5)

# Add a button to trigger prediction
ttk.Button(frame, text="Predict", command=predict_failure).grid(row=6, column=0, columnspan=2, pady=10)

# Add a result label
result_label = ttk.Label(frame, text="", font=("Helvetica", 14, "bold"), foreground="#008000")
result_label.grid(row=7, column=0, columnspan=2, pady=20)

# Add some spacing for better appearance
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=2)

# Start the GUI loop
root.mainloop()
