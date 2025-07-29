import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        birth_str = f"{entry_date.get()} {entry_time.get()}"
        birth_datetime = datetime.strptime(birth_str, "%Y-%m-%d %H:%M")
        now = datetime.now()
        
        if birth_datetime > now:
            messagebox.showerror("Error", "Birth date and time cannot be in the future.")
            return

        delta = now - birth_datetime

        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = (delta.days % 365) % 30
        hours = delta.seconds // 3600
        minutes = (delta.seconds % 3600) // 60

        result = (
            f"Age: {years} years, {months} months, {days} days,\n"
            f"{hours} hours, {minutes} minutes"
        )
        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Error", "Invalid date or time format.")

# GUI setup
root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x250")

tk.Label(root, text="Enter your birth date (YYYY-MM-DD):").pack(pady=5)
entry_date = tk.Entry(root)
entry_date.pack(pady=5)

tk.Label(root, text="Enter your birth time (HH:MM, 24-hour):").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack(pady=5)

tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)
label_result = tk.Label(root, text="", font=("Helvetica", 12))
label_result.pack(pady=10)

root.mainloop()
