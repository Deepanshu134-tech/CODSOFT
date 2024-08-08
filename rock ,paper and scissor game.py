import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        # Frame for buttons
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        # Buttons for user choice
        self.rock_button = tk.Button(self.frame, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.grid(row=0, column=0, padx=5)

        self.paper_button = tk.Button(self.frame, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.grid(row=0, column=1, padx=5)

        self.scissors_button = tk.Button(self.frame, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=5)

        # Label to display results
        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=20)

        # Label to display score
        self.score_label = tk.Label(root, text=f"User: {self.user_score}  Computer: {self.computer_score}", font=("Helvetica", 12))
        self.score_label.pack(pady=10)

        # Button to play again
        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again)
        self.play_again_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"You chose {user_choice.capitalize()}, Computer chose {computer_choice.capitalize()}. {result}")
        self.score_label.config(text=f"User: {self.user_score}  Computer: {self.computer_score}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def play_again(self):
        self.result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text=f"User: {self.user_score}  Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
