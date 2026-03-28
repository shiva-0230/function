import tkinter as tk

root = tk.Tk()
root.title("Geometry Methods")
root.geometry("300x200")

label1 = tk.Label(root, text="Using pack")
label1.pack(pady=10)

frame = tk.Frame(root)
frame.pack()  
label2 = tk.Label(frame, text="Using grid")
label2.grid(row=0, column=0)

label3 = tk.Label(root, text="Using place")
label3.place(x=100, y=150)

root.mainloop()
