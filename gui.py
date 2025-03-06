import pandas as pd
import joblib
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess  # To open the external Python file for scheduling maintenance

# Load the trained model
def load_model():
    model = joblib.load('machine_failure_model.pkl')
    return model

# Predict function
def predict_failure():
    try:
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
        
        # Log the prediction history
        history_data = {
            'Machine Type': [entry_machine_type.get()],
            'Air temperature [K]': [float(entry_air_temp.get())],
            'Process temperature [K]': [float(entry_process_temp.get())],
            'Rotational speed [rpm]': [float(entry_rotation_speed.get())],
            'Torque [Nm]': [float(entry_torque.get())],
            'Tool wear [min]': [float(entry_tool_wear.get())],
            'Predicted Failure': [prediction[0]]
        }
        history_df = pd.DataFrame(history_data)
        history_df.to_csv('prediction_history.csv', mode='a', header=False, index=False)
        
        # Display result
        result_label.config(text=f'Predicted machine failure: {prediction[0]}', foreground="#008000")
        
        # Update the history table
        update_history()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during prediction: {str(e)}")

# Update history function
def update_history():
    try:
        history_df = pd.read_csv('prediction_history.csv', names=[ 
            'Machine Type', 'Air temperature [K]', 'Process temperature [K]', 
            'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]', 'Predicted Failure'
        ])
        
        # Clear previous history in the treeview
        for row in history_tree.get_children():
            history_tree.delete(row)
        
        # Insert new history data into the treeview
        for _, row in history_df.iterrows():
            history_tree.insert("", "end", values=tuple(row))
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading history: {str(e)}")

# Delete selected history entry
def delete_history():
    try:
        selected_item = history_tree.selection()
        
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a row to delete.")
            return
        
        # Get the values of the selected row
        selected_values = history_tree.item(selected_item)["values"]
        
        # Load the history from the CSV
        history_df = pd.read_csv('prediction_history.csv', names=[ 
            'Machine Type', 'Air temperature [K]', 'Process temperature [K]', 
            'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]', 'Predicted Failure'
        ])
        
        # Find the row that matches the selected values
        row_to_delete = history_df[
            (history_df['Machine Type'] == selected_values[0]) &
            (history_df['Air temperature [K]'] == selected_values[1]) &
            (history_df['Process temperature [K]'] == selected_values[2]) &
            (history_df['Rotational speed [rpm]'] == selected_values[3]) &
            (history_df['Torque [Nm]'] == selected_values[4]) &
            (history_df['Tool wear [min]'] == selected_values[5]) &
            (history_df['Predicted Failure'] == selected_values[6])
        ]
        
        # Drop the row from the DataFrame
        history_df = history_df.drop(row_to_delete.index)
        
        # Save the updated history back to the CSV
        history_df.to_csv('prediction_history.csv', index=False, header=False)
        
        # Remove the selected row from the Treeview
        history_tree.delete(selected_item)
        
        messagebox.showinfo("Success", "History entry deleted successfully.")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while deleting history: {str(e)}")

# Open maintenance scheduling window (gui1.py)
def open_maintenance_schedule():
    import gui1  # Directly import the gui1 module to open the maintenance scheduling window
    gui1.create_maintenance_schedule_window()  # Call the function that opens the maintenance window

# GUI setup
root = tk.Tk()
root.title('Machine Failure Prediction')
root.geometry("1000x600")  # Set the window size

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
ttk.Label(frame, text="Machine Type").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_machine_type = ttk.Entry(frame)
entry_machine_type.grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Air temperature (K)").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_air_temp = ttk.Entry(frame)
entry_air_temp.grid(row=2, column=1, pady=5)

ttk.Label(frame, text="Process temperature (K)").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_process_temp = ttk.Entry(frame)
entry_process_temp.grid(row=3, column=1, pady=5)

ttk.Label(frame, text="Rotational speed (rpm)").grid(row=4, column=0, sticky=tk.W, pady=5)
entry_rotation_speed = ttk.Entry(frame)
entry_rotation_speed.grid(row=4, column=1, pady=5)

ttk.Label(frame, text="Torque (Nm)").grid(row=5, column=0, sticky=tk.W, pady=5)
entry_torque = ttk.Entry(frame)
entry_torque.grid(row=5, column=1, pady=5)

ttk.Label(frame, text="Tool wear (min)").grid(row=6, column=0, sticky=tk.W, pady=5)
entry_tool_wear = ttk.Entry(frame)
entry_tool_wear.grid(row=6, column=1, pady=5)

# Add a button to trigger prediction
ttk.Button(frame, text="Predict", command=predict_failure).grid(row=7, column=0, columnspan=2, pady=10)

# Add a result label
result_label = ttk.Label(frame, text="", font=("Helvetica", 14, "bold"))
result_label.grid(row=8, column=0, columnspan=2, pady=20)

# Add a history label
history_label = ttk.Label(frame, text="Prediction History", font=("Helvetica", 14, "bold"))
history_label.grid(row=9, column=0, columnspan=2, pady=10)

# Add a treeview widget for the prediction history table
history_tree = ttk.Treeview(frame, columns=[ 
    'Machine Type', 'Air temperature [K]', 'Process temperature [K]', 
    'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]', 'Predicted Failure'
], show='headings')

# Define column headings
history_tree.heading('Machine Type', text='Machine Type')
history_tree.heading('Air temperature [K]', text='Air temperature [K]')
history_tree.heading('Process temperature [K]', text='Process temperature [K]')
history_tree.heading('Rotational speed [rpm]', text='Rotational speed [rpm]')
history_tree.heading('Torque [Nm]', text='Torque [Nm]')
history_tree.heading('Tool wear [min]', text='Tool wear [min]')
history_tree.heading('Predicted Failure', text='Predicted Failure')

# Define column width for better readability
history_tree.column('Machine Type', width=150, anchor='center')
history_tree.column('Air temperature [K]', width=180, anchor='center')
history_tree.column('Process temperature [K]', width=180, anchor='center')
history_tree.column('Rotational speed [rpm]', width=180, anchor='center')
history_tree.column('Torque [Nm]', width=150, anchor='center')
history_tree.column('Tool wear [min]', width=150, anchor='center')
history_tree.column('Predicted Failure', width=180, anchor='center')

# Add the treeview to the frame
history_tree.grid(row=10, column=0, columnspan=2, pady=10)

# Add a delete button
delete_button = ttk.Button(frame, text="Delete Selected History", command=delete_history)
delete_button.grid(row=11, column=0, columnspan=2, pady=10)

# Add the maintenance button (always visible)
maintenance_button = ttk.Button(frame, text="Schedule Maintenance", command=open_maintenance_schedule)
maintenance_button.grid(row=12, column=0, columnspan=2, pady=10)

# Add some spacing for better appearance
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=2)

# Start the GUI loop
root.mainloop()
