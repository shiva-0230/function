import tkinter as tk

root = tk.Tk()

#Menu
menu = tk.Menu(root)
menu.add_command(label="Exit", command=root.quit)
root.config(menu=menu)

# Menubutton
mb = tk.Menubutton(root, text="Click Me")
mb.pack()

m = tk.Menu(mb, tearoff=0)
m.add_command(label="Option 1")
mb.config(menu=m)

root.mainloop()

