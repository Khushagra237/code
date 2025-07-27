import tkinter as tk

def convert():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{cm} cm")
    except:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Inches to Centimeters")

tk.Label(root, text="Enter inches:").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Convert", command=convert).pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()
