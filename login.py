import tkinter as tk
from tkinter import messagebox
import json
import os
import sys
import subprocess

# Function to load users from the file
def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
            return json.load(file)
    else:
        return {}

# Function to handle login logic
def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    users = load_users()

    if username in users and users[username] == password:
        root.destroy()  # Close the login window
        try:
            # Run gui2.py (make sure it is in the same directory)
            subprocess.run([sys.executable, 'gui2.py'])  # This should launch gui2.py as a new process
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch the admin panel: {str(e)}")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

# Creating the login window
root = tk.Tk()
root.title("Login")
root.geometry("500x350")  # Increased size for better visibility
root.config(bg="#e0f7fa")  # Light cyan background color

# Decorative frame with rounded corners effect (using relief)
frame = tk.Frame(root, bg="white", bd=15, relief="solid", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.7)

# Title Label with more emphasis
label_title = tk.Label(frame, text="Admin Panel Login", font=("Arial", 24, "bold"), fg="#00796b", bg="white")
label_title.pack(pady=20)

# Username Entry Section with proper padding and style
label_username = tk.Label(frame, text="Username:", font=("Arial", 14), bg="white", fg="#00796b")
label_username.pack(pady=10, anchor="w")
entry_username = tk.Entry(frame, font=("Arial", 14), bd=2, relief="groove", justify="center")
entry_username.pack(pady=5, fill="x")

# Password Entry Section with emphasis on security
label_password = tk.Label(frame, text="Password:", font=("Arial", 14), bg="white", fg="#00796b")
label_password.pack(pady=10, anchor="w")
entry_password = tk.Entry(frame, show="*", font=("Arial", 14), bd=2, relief="groove", justify="center")
entry_password.pack(pady=5, fill="x")

# Add a little space for better visual balance
spacer = tk.Label(frame, bg="white")
spacer.pack(pady=15)

# Login Button with a custom style
login_button = tk.Button(frame, text="Login", font=("Arial", 16, "bold"), bg="#26a69a", fg="white", relief="raised", bd=5, command=validate_login)
login_button.pack(pady=10, fill="x")

# Register Button (Added as an option for users to register if they haven't already)
register_button = tk.Button(frame, text="Not Registered? Register", font=("Arial", 12), bg="#f44336", fg="white", relief="raised", command=lambda: open_registration())
register_button.pack(pady=10, fill="x")

# Function to open registration window (create or open a separate file for registration)
def open_registration():
    root.quit()
    try:
        subprocess.run([sys.executable, 'register.py'])  # Opens the registration window
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch the registration panel: {str(e)}")

# Run the login window
root.mainloop()
