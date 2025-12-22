import tkinter as tk

root = tk.Tk()
root.title("Lesson 3 - Button")
root.geometry("400x300")

def submit_data():
    print("Data submitted")

def change_label():
    label_test.config(text="Data received")

print_tty = tk.Button(root, text="Print to terminal", command=submit_data)
print_tty.pack()

chng_lbl = tk.Button(root, text="Change the label", command=change_label)
chng_lbl.pack()

label_test = tk.Label(root, text="Waiting data to be submitted")
label_test.pack()

root.mainloop()
