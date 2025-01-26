import tkinter
from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("600x300")
root.title("Form")

l=Label(text="REGISTRATION FORM",font=("TImes new roman",19,"bold"))
l.grid(row=0,column=1)
Fstname=Label(text="Name:",font=("Helvetica",15),padx=4,pady=5)
Mobile=Label(text="Mobile:",font=("Helvetica",15),padx=4,pady=5)


Radiobutton(root,text="Male",padx=14,value=1).grid(row=5,column=0)
Radiobutton(root,text="Female",padx=14,value=2).grid(row=5,column=1)
Checkbutton(text="Agree to T & C").grid(row=6,column=1)

Fstname.grid(row=3,column=0)
Mobile.grid(row=4,column=0)

Fstnameval=StringVar()
Mobileval=IntVar()

Fstentry=Entry(textvariable=Fstnameval)
Mobileentry=Entry(textvariable=Mobileval)

Fstentry.grid(row=3,column=1)
Mobileentry.grid(row=4,column=1)
def message_box():
    val=tmsg.askquestion("Was your experience good","You used this gui.. was your exp good")
    if val=="yes":
        msg="rate us on apstore"
    else:
        msg="tell us the problem"
    tmsg.showinfo("Feedback",msg)

Button(text="Reset",padx=10).grid(row=10,column=0)
Button(text="Submit",padx=10,command=message_box).grid(row=10,column=1)

root.mainloop()