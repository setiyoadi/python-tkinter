import tkinter as tk

root = tk.Tk()
root.title("Lesson 6 - Grid layout")
root.geometry("400x300")

nama_label = tk.Label(root, text="Nama")
nama_label.grid(row=0, column=0, sticky="w")

nama_entry = tk.Entry(root)
nama_entry.grid(row=0, column=2)

nama_button = tk.Button(root, text="Check")
nama_button.grid(row=0, column=3, rowspan=2)

kode_label = tk.Label(root, text="Kode")
kode_label.grid(row=1, column=0, sticky="w")

kode_entry = tk.Entry(root)
kode_entry.grid(row=1, column=2)

#kode_button = tk.Button(root, text="Check")
#kode_button.grid(row=1, column=3)

root.mainloop()