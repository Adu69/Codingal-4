import tkinter as tk

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x400")
root.resizable(False, False)

def check_password_strength():
    password = password_entry.get()
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
        strength += 1

    if strength == 0:
        result_label.config(text="Password is very weak", fg="red")
    elif strength == 1:
        result_label.config(text="Password is weak", fg="orange")
    elif strength == 2:
        result_label.config(text="Password is moderate", fg="yellow")
    elif strength == 3:
        result_label.config(text="Password is strong", fg="lightgreen")
    elif strength == 4:
        result_label.config(text="Password is very strong", fg="green")
    else:
        result_label.config(text="Password is extremely strong", fg="darkgreen")

password_label = tk.Label(root, text="Enter your password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", fg="black")
result_label.pack(pady=10)

root.mainloop()