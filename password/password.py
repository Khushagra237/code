import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        result.set("Please enter a password")
    elif length < 4:
        result.set("Weak Password")
    elif 4 <= length < 8:
        result.set("Moderate Password")
    else:
        result.set("Strong Password")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

heading = tk.Label(root, text="Enter Password", font=("Arial", 14))
heading.pack(pady=10)

entry = tk.Entry(root, show="*", font=("Arial", 12), width=25)
entry.pack(pady=5)

check_btn = tk.Button(root, text="Check Strength", command=check_strength, font=("Arial", 12))
check_btn.pack(pady=10)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 12, "bold"), fg="blue")
result_label.pack(pady=10)

root.mainloop()
