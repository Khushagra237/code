import tkinter as tk
from tkinter import CENTER, messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Denomination Calculator")
root.configure(bg='light blue')
root.geometry("650x400")

upload = Image.open("denomination.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = tk.Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = tk.Label(root,
                  text="Hey User! Welcome to Denomination Counter App",
                  bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    messagebox.showinfo(
        "Alert",
        "This is a denomination counter app that helps you calculate the total value of different currency notes and coins."
    )
    topwin()

def topwin():
    top = tk.Toplevel()
    top.title("Denomination Counter")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")

    label = tk.Label(top, text="Enter total amount", bg='light grey')
    entry = tk.Entry(top)

    lbl = tk.Label(top, text="Here are the numbers of notes for each denomination", bg='light grey')
    l1 = tk.Label(top, text="2000", bg='light grey')
    l2 = tk.Label(top, text="500", bg='light grey')
    l3 = tk.Label(top, text="100", bg='light grey')

    t1 = tk.Entry(top)
    t2 = tk.Entry(top)
    t3 = tk.Entry(top)

    def calculate():
        try:
            total_amount = int(entry.get())
            if total_amount < 0:
                raise ValueError("Amount cannot be negative")

            notes_2000 = total_amount // 2000
            total_amount %= 2000
            notes_500 = total_amount // 500
            total_amount %= 500
            notes_100 = total_amount // 100
            total_amount %= 100

            t1.delete(0, tk.END)
            t2.delete(0, tk.END)
            t3.delete(0, tk.END)

            t1.insert(0, str(notes_2000))
            t2.insert(0, str(notes_500))
            t3.insert(0, str(notes_100))
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    btn = tk.Button(top, text="Calculate", command=calculate, bg='brown', fg='white')

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    topwin.mainloop()

root.mainloop()
