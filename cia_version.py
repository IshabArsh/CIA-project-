# age_app_custom.py
import tkinter as tk
from tkinter import messagebox

def show_age():
    val = entry.get().strip()
    if val == "":
        messagebox.showwarning("Age", "Please enter your age.")
        return
    # optional: numeric check
    try:
        age_int = int(val)
    except ValueError:
        messagebox.showerror("Age", "Enter a valid number.")
        return
    messagebox.showinfo("Age", f"Your Age: {age_int}")

root = tk.Tk()
root.title("Age")
root.geometry("260x120")
root.resizable(False, False)

label = tk.Label(root, text="Enter age:")
label.pack(pady=(10, 0))

entry = tk.Entry(root, width=20)
entry.pack(pady=5)
entry.focus_set()

enter_btn = tk.Button(root, text="Enter", width=10, command=show_age)
enter_btn.pack(pady=(5, 10))

# allow pressing Enter key
root.bind("<Return>", lambda event: show_age())

root.mainloop()