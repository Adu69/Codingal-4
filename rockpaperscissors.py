import random
import tkinter as tk

def play():
    choices = ["Rock", "Paper", "Scissors", "rock", "paper", "scissors"]
    print(choices)
    user_choice = input("Enter your choice (Rock, Paper, Scissors): ")
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" or user_choice == "rock" and computer_choice == "Scissors" or computer_choice == "scissors") or \
         (user_choice == "Paper" or user_choice == "paper" and computer_choice == "Rock" or computer_choice == "rock") or \
         (user_choice == "Scissors" or user_choice == "scissors" and computer_choice == "Paper" or computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
tk.Button(root, text="Play", command=lambda: play()).pack(pady=20)
root.mainloop()