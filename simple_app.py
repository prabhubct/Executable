import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Hello!", "You clicked the button!")

# Create GUI window
root = tk.Tk()
root.title("Simple App")
root.geometry("300x200")

# Button to show message
button = tk.Button(root, text="Click Me!", command=show_message, font=("Arial", 14))
button.pack(pady=50)

# Run the application
root.mainloop()
