import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())
        
        simple_interest = (principal * rate * time) / 100
        compound_interest = principal * ((1 + rate / 100) ** time - 1)
        
        messagebox.showinfo("Result", 
                            f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x250")
root.configure(bg="lightblue")

tk.Label(root, text="Principal Amount:", bg="lightblue").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Time Period (years):", bg="lightblue").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack()

tk.Label(root, text="Rate of Interest (%):", bg="lightblue").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Button(root, text="Calculate", command=calculate_interest, bg="green", fg="white").pack(pady=15)

root.mainloop()
