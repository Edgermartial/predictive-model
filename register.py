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

# Function to save users to the file
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

# Function to handle user registration
def register_user():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    # Load existing users
    users = load_users()

    # Check if the username already exists
    if username in users:
        messagebox.showerror("Registration Failed", "Username already exists! Please choose a different username.")
        return

    # Check if passwords match
    if password != confirm_password:
        messagebox.showerror("Registration Failed", "Passwords do not match!")
        return

    # Save new user if validation passes
    users[username] = password
    save_users(users)

    messagebox.showinfo("Registration Successful", "User registered successfully!")
    
    # After successful registration, go to the login screen
    go_to_login()

# Function to go to the login screen
def go_to_login():
    root.quit()  # Close the registration window
    try:
        subprocess.run([sys.executable, 'login.py'])  # Run login.py as a new process
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch the login panel: {str(e)}")

# Creating the registration window
root = tk.Tk()
root.title("Register")
root.geometry("400x350")  # Adjusted window size for better design
root.config(bg="#f3f4f6")  # Soft gray background color

# Title Label with modern, simple design
label_title = tk.Label(root, text="Create Account", font=("Arial", 18), bg="#f3f4f6", fg="#333")
label_title.pack(pady=20)

# Username Entry Section with proper padding and clear font
label_username = tk.Label(root, text="Username:", font=("Arial", 12), bg="#f3f4f6", fg="#555")
label_username.pack(pady=5)
entry_username = tk.Entry(root, font=("Arial", 14), bd=2, relief="solid", justify="center")
entry_username.pack(pady=5, fill="x", padx=40)

# Password Entry Section with a simple but elegant design
label_password = tk.Label(root, text="Password:", font=("Arial", 12), bg="#f3f4f6", fg="#555")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*", font=("Arial", 14), bd=2, relief="solid", justify="center")
entry_password.pack(pady=5, fill="x", padx=40)

# Confirm Password Entry Section
label_confirm_password = tk.Label(root, text="Confirm Password:", font=("Arial", 12), bg="#f3f4f6", fg="#555")
label_confirm_password.pack(pady=5)
entry_confirm_password = tk.Entry(root, show="*", font=("Arial", 14), bd=2, relief="solid", justify="center")
entry_confirm_password.pack(pady=5, fill="x", padx=40)

# Add a little space for better visual balance
spacer = tk.Label(root, bg="#f3f4f6")
spacer.pack(pady=20)

# Register Button with modern design and soft color
register_button = tk.Button(root, text="Register", font=("Arial", 14), bg="#4CAF50", fg="white", bd=0, relief="flat", command=register_user)
register_button.pack(pady=10, fill="x", padx=60)

# Login Button (for users who already have an account) with a clean design
login_button = tk.Button(root, text="Already have an account? Login", font=("Arial", 12), fg="#00796b", bg="#f3f4f6", bd=0, relief="flat", command=go_to_login)
login_button.pack(pady=10)

# Run the registration window
root.mainloop()
