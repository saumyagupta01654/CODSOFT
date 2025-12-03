import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(entry.get())  # Get the length from the user
        if length <= 0:
            messagebox.showerror("Error", "Enter a positive number")
            return
        
        # Characters to use in password
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate password
        password = "".join(random.choice(characters) for _ in range(length))
        
        # Show password in the label
        result_label.config(text=password)
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Create main window
root = tk.Tk()
root.title("Password Generator")

# GUI elements
tk.Label(root, text="Enter password length:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=5)

# Run the window
root.mainloop()
