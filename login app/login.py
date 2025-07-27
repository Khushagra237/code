import tkinter as tk

def convert():
    try:
        val = float(entry.get())
        unit = unit_var.get()
        if unit == "m":
            result = val * 100
        elif unit == "inch":
            result = val * 2.54
        elif unit == "ft":
            result = val * 30.48
        else:
            result = 0
        result_label.config(text=f"{round(result, 2)} cm")
    except:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("To CM Converter")

entry = tk.Entry(root)
entry.pack()

unit_var = tk.StringVar(value="m")
tk.OptionMenu(root, unit_var, "m", "inch", "ft").pack()

tk.Button(root, text="Convert", command=convert).pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()


