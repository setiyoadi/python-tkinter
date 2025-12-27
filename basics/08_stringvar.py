import tkinter as tk
    
# create main window
root = tk.Tk()
root.title("Lesson 8 - StringVar")
root.geometry("400x300")

#define stringvar
guestname = tk.StringVar()

#function to change label upon click
def greet_user():
    name = guestname.get()
    greeting.config(text=f"Hello, {name}")
    guestname.set("")
    name_entry.focus()

#make entry frame on top
entry_frm = tk.Frame(root)
entry_frm.pack(side="top", fill="x", expand=True)

#make label frame to display label in the middle, filling the space
lbl_frm = tk.Frame(root)
lbl_frm.pack(side="top", fill="both", expand=True)

#make button frame at the bottom
bttn_frm = tk.Frame(root)
bttn_frm.pack(side="bottom", fill="x", expand=True)

#add label in the entry_frm
name_label = tk.Label(entry_frm, text="Name")
name_label.grid(row=0, column=0, padx=5, pady=5)

#add entry in the entry_frm
name_entry = tk.Entry(entry_frm, textvariable=guestname)
name_entry.grid(row=0, column=1, padx=5, pady=5)

#add label preview
prev_lbl = tk.Label(lbl_frm, textvariable=guestname)
prev_lbl.pack(padx=5, pady=5)

#add label to greet the user
greeting = tk.Label(lbl_frm, text="")
greeting.pack(padx=5, pady=5)

#add button to print greeting
greet_bttn = tk.Button(bttn_frm, text="Print greeting", command=greet_user)
greet_bttn.pack(padx=5, pady=5)




root.mainloop()