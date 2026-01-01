import tkinter as tk

root = tk.Tk()
root.title("Smart Greeter")
root.geometry("600x400")

judulfrm = tk.Frame(root, bd=2, relief="solid")
judulfrm.pack(side="top", fill="x", padx=5, pady=5)

inputfrm = tk.Frame(root, bd=2, relief="solid")
inputfrm.pack(side="top", fill="x", padx=5, pady=5)

optionfrm = tk.Frame(root, bd=2, relief="solid")
optionfrm.pack(side="top", fill="x", padx=5, pady=5)

judul = tk.Label(judulfrm, text="Selamat datang di Smart Greeter")
judul.pack()

root.mainloop()


