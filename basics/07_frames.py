import tkinter as tk

def keluar_apps(event=None):
    root.destroy()

root = tk.Tk()
root.title("Lesson 7 - Frames")
root.geometry("600x300")

top_frm = tk.Frame(root, bg="yellow")
top_frm.pack(side="top", fill="x")

left_frm = tk.Frame(root, bg="green")
left_frm.pack(side="left", fill="both", expand=True)

right_frm = tk.LabelFrame(root, text="Informasi")
right_frm.pack(side="right")

judul = tk.Label(top_frm, text="BELAJAR MENGATUR FRAME")
judul.pack()

nama_lbl = tk.Label(left_frm, text="Nama")
nama_lbl.grid(row=0, column=0, padx=5, pady=5)

hobby_lbl = tk.Label(left_frm, text="Hobby")
hobby_lbl.grid(row=1, column=0, padx=5, pady=5)

nama_entry = tk.Entry(left_frm)
nama_entry.grid(row=0, column=1, sticky="ew")

hobby_entry = tk.Entry(left_frm)
hobby_entry.grid(row=1, column=1, sticky="ew")

info_text = tk.Text(right_frm, width=30, height=10, wrap="word")
info_text.pack()

info_text.insert("1.0", "Text percobaan jadi kita coba saja masukan apa saja teks kedalam kotak sehingga semua akan menjadi baik baik saja")
info_text.config(state="disabled")

root.bind("<Escape>", keluar_apps)

root.mainloop()