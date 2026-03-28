import tkinter as tk
from tkinter import messagebox, filedialog

def show_msg():
    messagebox.showinfo("Message", "Hello! This is a message box")

def open_file():
    file = filedialog.askopenfilename()
    if file:
        messagebox.showinfo("File Selected", file)

root = tk.Tk()
root.title("Messagebox & File Dialog")

tk.Button(root, text="Show Message", command=show_msg).pack(pady=10)
tk.Button(root, text="Open File", command=open_file).pack(pady=10)

root.mainloop()

