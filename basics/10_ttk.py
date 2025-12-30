import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Lesson 10 - Themed TK")
root.geometry("400x300")

labelnama = ttk.Label(root, text="Nama")
labelnama.pack()

entrynama = ttk.Entry(root)
entrynama.pack()

tombolnama = ttk.Button(root, text="Cek nama")
tombolnama.pack()

root.mainloop()