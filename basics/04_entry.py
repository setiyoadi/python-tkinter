import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Lesson 3 - Entry")

def print_to_tty():
    ambil_nama = nama_entry.get()
    print(f"Halo, {ambil_nama}")

def print_to_scr():
    ambil_nama = nama_entry.get()
    output_label.configure(text=f"Halo, {ambil_nama}")
    

nama_label = tk.Label(root, text="Nama:")
nama_label.pack(anchor="w", padx=20, pady=10)

nama_entry = tk.Entry(root)
nama_entry.pack(fill="x", padx=20, pady=10)

tty_button = tk.Button(root, text="Print to tty", command=print_to_tty)
tty_button.pack(anchor="w", padx=20, pady=10)

scr_button = tk.Button(root, text="Print to screen", command=print_to_scr)
scr_button.pack(anchor="w", padx=20, pady=10)

output_label = tk.Label(root, text="")
output_label.pack(anchor="w", padx=20, pady=10)

root.mainloop()