# age_app_simple.py
import tkinter as tk
from tkinter import simpledialog, messagebox

def main():
    root = tk.Tk()
    root.withdraw()  # main window chhupa do
    age = simpledialog.askinteger("Enter age", "Enter your age:")
    if age is None:
        messagebox.showinfo("Age", "No age entered.")
    else:
        messagebox.showinfo("Age", f"Your Age: {age}")
    root.destroy()

if __name__ == "__main__":
    main()
