import tkinter as tk
root = tk.Tk()
root.title("Hello World")
root.geometry("300x150")  
label = tk.Label(root, text="Hello World")
label.grid(row=0, column=0)
root.mainloop()
