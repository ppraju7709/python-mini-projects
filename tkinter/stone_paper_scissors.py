import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("STONE-PAPER-SCISSOR")
root.geometry("350x500")
root.resizable(True,True)

# variables
choices = ["Stone",'Paper',"Scissor"]
user_score = 0
comp_score = 0


# funtion conditions
def play(user_choice):
    global user_score, comp_score

    comp_choice = random.choice(choices)

    user_label.config(text=f"Your Choice :- {user_choice}")
    comp_label.config(text=f"Computer Choice :- {comp_choice}")


    if user_choice == comp_choice:
        result_label.config(text="Result: Tie 🤝")

    elif ((user_choice == "Stone" and comp_choice == "Scissor") or
        (user_choice == "Scissor" and comp_choice == "Paper") or
        (user_choice == "Paper" and comp_choice == "Stone")):

        result_label.config(text="Result: You Win 🎉")
        user_score += 1

    else:
        result_label.config(text="Result: Computer Wins 💻")
        comp_score += 1

    score_label.config(text=f"Score → You :- {user_score} | Computer :- {comp_score}")

def reset():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_label.config(text="Your Choice :- ")
    comp_label.config(text="Computer Choice :- ")
    result_label.config(text="Result :- ")
    score_label.config(text="Score → You :- 0  | Computer :- 0")


# Title
title = tk.Label(root, text="Stone Paper Scissors", font=("Algerian", 20))
title.pack(pady=15)

# Choice labels
user_label = tk.Label(root, text="Your Choice :- ", font=("Times New Roman", 14))
user_label.pack()

comp_label = tk.Label(root, text="Computer Choice :- ", font=("Times New Roman", 14))
comp_label.pack()

# Result
result_label = tk.Label(root, text="Result :- ", font=("Times New Roman", 16, "bold"))
result_label.pack(pady=10)

# Score
score_label = tk.Label(root, text="Score → You :- 0 || Computer :- 0", font=("Times New Roman", 13))
score_label.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(button_frame, text="Stone", width=10,
          command=lambda: play("Stone")).grid(row=0, column=0, padx=5)

tk.Button(button_frame, text="Paper", width=10,
          command=lambda: play("Paper")).grid(row=0, column=1, padx=5)

tk.Button(button_frame, text="Scissor", width=10,
          command=lambda: play("Scissor")).grid(row=0, column=2, padx=5)

# Reset button
reset_btn = tk.Button(root, text="Reset Game", command=reset)
reset_btn.pack(pady=10)

# Run app
root.mainloop()