import tkinter as tk


def on_change(e):
    print(e.widget.get())

root = tk.Tk()

e = tk.Entry(root)
e.pack()
# Calling on_change when you press the return key
e.bind("<Return>", on_change)

root.mainloop()