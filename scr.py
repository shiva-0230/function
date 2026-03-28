import tkinter as tk

root = tk.Tk()

scroll = tk.Scrollbar(root)
scroll.pack(side="right", fill="y")

listbox = tk.Listbox(root, yscrollcommand=scroll.set)
for i in range(1, 21):
    listbox.insert("end", f"Item {i}")

listbox.pack()
scroll.config(command=listbox.yview)

root.mainloop()

