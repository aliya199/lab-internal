import tkinter as tk
from tkinter import messagebox

# Function to display message after registration
def register():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()
    if username and password and email:
        messagebox.showinfo("Success", f"User {username} registered successfully!")
    else:
        messagebox.showerror("Error", "Please fill all fields!")

# Create main window
root = tk.Tk()
root.title("Registration Form")

# Username
tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=5)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)

# Password
tk.Label(root, text="Password").grid(row=1, column=0, padx=10, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

# Email
tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

# Register button
tk.Button(root, text="Register", command=register).grid(row=3, columnspan=2, pady=10)

root.mainloop()
