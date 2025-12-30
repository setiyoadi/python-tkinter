import tkinter as tk

def show_state():
    print("I agree to the EULA: ", agree_var.get())

def update_status(*arg):
    if agree_var.get():
        status_var.set("Agree")
        print_button.config(state="normal")
    else:
        status_var.set("Not agree")
        print_button.config(state="disabled")

root = tk.Tk()
root.title("Lesson 9 - Checkbutton")
root.geometry("400x300")

agree_var = tk.BooleanVar(value=False)
status_var = tk.StringVar(value="Not agree")
agree_var.trace_add("write", update_status)

eula_state = tk.Label(root, text="Please read the EULA")
eula_state.pack(side="top", padx=10, pady=10)

preview = tk.Label(root, textvariable=status_var)
preview.pack(side="top", padx=10, pady=10)

centang = tk.Checkbutton(root, text="I have read and agree on the terms.", variable=agree_var)
centang.pack(side="bottom", padx=10, pady=10)

print_button = tk.Button(root, text="Print state", command=show_state, state="disabled")
print_button.pack(side="bottom", padx=10, pady=10)

root.mainloop()



