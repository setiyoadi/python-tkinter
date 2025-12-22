import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Lesson 3 - Entry")

nama_label = tk.Label(root, text="Nama:")
nama_label.pack(anchor="w", padx=20)

nama_entry = tk.Entry(root)
nama_entry.pack(fill="x", padx=20)

root.mainloop()