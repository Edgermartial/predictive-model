import tkinter as tk
from tkinter import ttk, messagebox

# Function to save the maintenance task
def save_maintenance_task():
    task_description = task_entry.get()
    maintenance_date = date_entry.get()
    
    if task_description == "" or maintenance_date == "":
        messagebox.showerror("Input Error", "Please provide both Task Description and Maintenance Date.")
        return

    # In a real-world scenario, you can save this information to a file, database, etc.
    messagebox.showinfo("Task Saved", f"Maintenance task saved:\n{task_description}\nDate: {maintenance_date}")

# GUI setup
def create_maintenance_schedule_window():
    window = tk.Tk()
    window.title("Maintenance Schedule")
    window.geometry("400x300")

    # Add a title label
    title_label = ttk.Label(window, text="Schedule Maintenance", font=("Helvetica", 16))
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Task description input
    ttk.Label(window, text="Task Description:").grid(row=1, column=0, sticky=tk.W, pady=5)
    global task_entry
    task_entry = ttk.Entry(window, width=30)
    task_entry.grid(row=1, column=1, pady=5)

    # Maintenance date input
    ttk.Label(window, text="Maintenance Date:").grid(row=2, column=0, sticky=tk.W, pady=5)
    global date_entry
    date_entry = ttk.Entry(window, width=30)
    date_entry.grid(row=2, column=1, pady=5)

    # Save button
    save_button = ttk.Button(window, text="Save Task", command=save_maintenance_task)
    save_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Close button
    close_button = ttk.Button(window, text="Close", command=window.destroy)
    close_button.grid(row=4, column=0, columnspan=2, pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_maintenance_schedule_window()
