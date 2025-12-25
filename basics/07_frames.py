import tkinter as tk

root = tk.Tk()
root.title("Lesson 7 - Frames")
root.geometry("400x300")

frame_judul = tk.Frame(root, bg="green")
frame_judul.pack(side="top", fill="x")

frame_isi = tk.Frame(root, bg="yellow")
frame_isi.pack(side="top", fill="both", expand="True")

frame_tombol = tk.Frame(root, bg="blue")
frame_tombol.pack(side="bottom", fill="x")

teks_judul = tk.Label(frame_judul, text="CONTOH FRAME JUDUL")
teks_judul.pack()

teks_isi = tk.Label(frame_isi, text="CONTOH FRAME ISI")
teks_isi.pack()

tombol_ok = tk.Button(frame_tombol, text="OK")
tombol_ok.pack()


root.mainloop()