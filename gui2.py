import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess
import sys

# Main Panel Class
class AdminPanel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Predictive Maintenance Admin Panel")
        self.geometry("800x600")
        self.config(bg="lightgray")  # Set background color

        # Adding a custom frame for decoration
        self.frame = tk.Frame(self, bg="#f8f9fa", bd=5, relief="groove")
        self.frame.place(relwidth=1, relheight=1)

        # Title Label
        self.label_title = tk.Label(self.frame, text="Predictive Maintenance Dashboard", font=("Arial", 24, "bold"), fg="#2e3d49", bg="#f8f9fa")
        self.label_title.pack(pady=30)

        # Decorative Buttons (e.g., Overview, Logs, Alerts, etc.)
        self.setup_buttons()

    def setup_buttons(self):
        # Define button style without bg
        button_style = {
            'font': ("Arial", 14, "bold"),
            'fg': "white",
            'relief': "raised",
            'bd': 5,
            'width': 20
        }

        # Example buttons for different sections of the admin panel
        self.button_system = tk.Button(self.frame, text="System Overview", **button_style, bg="#4CAF50", command=self.system_overview)
        self.button_system.pack(pady=10)

        self.button_maintenance = tk.Button(self.frame, text="Maintenance Logs", **button_style, bg="#4CAF50", command=self.maintenance_logs)
        self.button_maintenance.pack(pady=10)

        self.button_alerts = tk.Button(self.frame, text="Alerts", **button_style, bg="#4CAF50", command=self.alerts)
        self.button_alerts.pack(pady=10)

        # New Button for "Predict Machine Failure"
        self.button_predict_failure = tk.Button(self.frame, text="Predict Machine Failure", **button_style, bg="#FF9800", command=self.predict_machine_failure)
        self.button_predict_failure.pack(pady=10)

        # Remove the `bg` from the style and pass it directly to the Button
        self.button_logout = tk.Button(self.frame, text="Logout", **button_style, bg="red", command=self.logout)
        self.button_logout.pack(pady=20)

    def system_overview(self):
        # Placeholder: Display system status, sensor data, etc.
        messagebox.showinfo("System Overview", "Display system status, sensor data, and other related info.")

    def maintenance_logs(self):
        # Placeholder: Display historical maintenance logs here.
        messagebox.showinfo("Maintenance Logs", "Display historical maintenance logs and related data.")

    def alerts(self):
        # Placeholder: Show predictive alerts based on sensor data.
        messagebox.showinfo("Alerts", "Show predictive alerts and their details.")

    def predict_machine_failure(self):
        # Launch the gui.py when "Predict Machine Failure" is clicked
        try:
            subprocess.run([sys.executable, 'gui.py'])  # Run gui.py as a new process
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch the prediction panel: {str(e)}")

    def logout(self):
        # Close the admin panel (logout)
        self.quit()

# Running the admin panel
if __name__ == "__main__":
    app = AdminPanel()
    app.mainloop()
