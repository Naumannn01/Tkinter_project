from tkinter import *
from tkinter import messagebox
import string, random

root = Tk()
root.geometry("300x200")
root.title("Nauman's Secret Language")

def encode():
    clear_widgets()
    str_input = user_input.get()
    if str_input:
        coded=str(str_input[::-1])
        res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
        res2 =''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
        encode = res+coded+res2
    else:
        messagebox.showerror("Error!!", "Enter some text", parent=root)
        return

    label = Label(message_frame, text="Code is Encoded")
    label.configure(font=("Cambria", 12))
    label.pack(pady=10)

    entry_box = Entry(message_frame, font=("Cambria", 12))
    entry_box.insert(0, encode)
    entry_box.pack(pady=10)

def decode():
    clear_widgets()
    str_input = user_input.get()
    if str_input:
        b=str_input[::-1]
        decoded=b[3:-3]
    else:
        messagebox.showerror("Error!!", "Enter some text", parent=root)
        return

    label = Label(message_frame, text="Code is Decoded")
    label.configure(font=("Cambria", 12))
    label.pack(pady=10)

    entry_box = Entry(message_frame, font=("Cambria", 12))
    entry_box.insert(0, decoded)
    entry_box.pack(pady=10)

def clear_widgets():
    for widgets in message_frame.winfo_children():
        widgets.destroy()

user_input = Entry(root, font=("Cambria", 14))
user_input.pack(fill=X, padx=20, pady=10)

frame = Frame(root)
frame.pack()

code_button = Button(frame, text="Encode", font=("Cambria", 12))
code_button.configure(command=encode)
code_button.pack(side=LEFT, padx=5, pady=5)

decode_button = Button(frame, text="Decode", font=("Cambria", 12))
decode_button.configure(command=decode)
decode_button.pack(side=LEFT, padx=5, pady=5)

message_frame = Frame(root)
message_frame.pack()

root.mainloop()