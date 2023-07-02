from tkinter import*
def click(event):
    global scvalue
    text=event.widget.cget("text") #with cget you get the val of the text
    if text =="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
              print(e)
              value="Error"
                
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update() 

#NAUMAN HEREE hello peeps!
#can also be done using list and loops
root=Tk()
# root.geometry("600x800")
root.title("Nauman's Calculator")
root.configure(bg="Grey")

#entry widget
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="lucida 30 bold")
screen.pack(fill=X,ipadx=15,padx=10,pady=10)

#Line 0-------------------------
# frame
f=Frame(root,bg="black")
b=Button(f,text="%",padx=26,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click) #binded with click event

b=Button(f,text=" / ",padx=20,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="^",padx=26,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)


b=Button(f,text="C",padx=24,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
f.pack()

#Line 1-------------------------
f=Frame(root,bg="black")

b=Button(f,text="7",padx=28,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click) #binded with click event

b=Button(f,text="8",padx=28,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="9",padx=28,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)


b=Button(f,text="*",padx=27,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
f.pack()

#Line 2---------------
f=Frame(root,bg="black")
b=Button(f,text="4",padx=28,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click) #binded with click event

b=Button(f,text="5",padx=28,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="6",padx=28,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)


b=Button(f,text="-",padx=28,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
f.pack()

#Line3------------------
f=Frame(root,bg="black")
b=Button(f,text="1",padx=28,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click) #binded with click event

b=Button(f,text="2",padx=28,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="3",padx=28,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)


b=Button(f,text="+",padx=24,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
f.pack()


#Line 4-------------------------
f=Frame(root,bg="black")
b=Button(f,text="0",padx=28,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click) #binded with click event

b=Button(f,text="00",padx=20,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text=".",padx=28,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)


b=Button(f,text="=",padx=28,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
f.pack()
root.mainloop()