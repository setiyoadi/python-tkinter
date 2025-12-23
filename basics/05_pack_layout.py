import tkinter as tk

root = tk.Tk()
root.title("Lesson 5 - Pack layout")
root.geometry("400x300")

button_a = tk.Button(root, text="AAAAAAAAAAAAA")
button_a.pack(fill="x", padx=10, pady=10)

button_b = tk.Button(root, text="BBBBBBBBBBBBB")
button_b.pack(fill="x", padx=20, pady=10)

entry_a = tk.Entry(root)
entry_a.pack(side="bottom", fill="both", padx=10, pady=10)

root.mainloop()