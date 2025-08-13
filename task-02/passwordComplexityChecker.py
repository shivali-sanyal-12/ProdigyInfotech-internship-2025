import tkinter as tk
import re

def check_strength():
    password = entry.get()
    
    if not password.strip():  # check if input is empty or just spaces
        result.set("No password entered")
        feedback.set("Please type a password to check its strength.")
        return

    strength = 0
    suggestions = []

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append(" Use 8+ characters")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append(" Add lowercase letters")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("• Add uppercase letters")

    if re.search(r"\d", password):
        strength += 1
    else:
        suggestions.append("• Add numbers")

    if re.search(r"[@$!%*?&#]", password):
        strength += 1
    else:
        suggestions.append(" Add special characters")

    if strength <= 2:
        result.set("Very Weak")
    elif strength == 3:
        result.set("Weak")
    elif strength == 4:
        result.set("Medium")
    else:
        result.set("Strong")

    feedback.set('\n'.join(suggestions))

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x350")

tk.Label(root, text="Enter Password:", font=("Arial", 14)).pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Check Strength", command=check_strength, font=("Arial", 12)).pack(pady=15)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 16, "bold"), fg="blue").pack(pady=5)

feedback = tk.StringVar()
tk.Label(root, textvariable=feedback, fg="red", wraplength=450, justify="left", font=("Arial", 12)).pack(pady=5)

root.mainloop()


