import tkinter as tk
import random

# Function to play game
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(choices)

    if user_choice == comp_choice:
        result.set(f"Tie! Both chose {user_choice}")
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result.set(f"You Win! {user_choice} beats {comp_choice}")
    else:
        result.set(f"You Lose! {comp_choice} beats {user_choice}")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

# Heading
heading = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
heading.pack(pady=15)

# Buttons for choices
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, font=("Arial", 12),
                     command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, font=("Arial", 12),
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, font=("Arial", 12),
                         command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Result Label
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 14), fg="blue")
result_label.pack(pady=20)

root.mainloop()
