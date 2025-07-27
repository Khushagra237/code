import tkinter as tk

root = tk.Tk()
root.title('Event Handler')
root.geometry('100x100')
def handle_keypress(event):
    """Print the character associated with the key presses"""
    print(event.char)
root.bind('<Key>', handle_keypress)
def handle_click(event):
    print("\nThe button was clicked")
button = tk.Button(text='Click Me!')
button.bind('<Button-1>', handle_click)
root.mainloop()

