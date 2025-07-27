import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Virus Detector")
root.geometry("200x200")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found")

button = tk.Button( text="Scan", command=msg)   
button.place(x=40, y=80)
button.pack()
root.mainloop()