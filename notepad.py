from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
root=Tk()
#All functions
def newfile():
   global file
   root.title("Untitled -Notepad")
   file=None
   TextArea.delete(1.0,END)    

def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file =="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            #save as new file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
   showinfo("Notepad","Notepad by Code With Nauman")
#creating inside main for a better flow
if __name__=='__main__':
    #basic tkinter setup
    root.title("Untitled - Notepad")
    # root.wm_iconbitmap("") haven't added any icon
    root.geometry("644x600")
    #add text area
    TextArea= Text(root,font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)

    #menubar
    Menubar=Menu(root)
    #filemenu starts---------
    FileMenu=Menu(Menubar,tearoff=0)
    #Features new open save exit
    FileMenu.add_command(label="New",command=newfile)
    FileMenu.add_command(label="Open", command=openfile)
    FileMenu.add_command(label="Save", command=savefile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    Menubar.add_cascade(label="File",menu=FileMenu)
    #filemenu ends---------

    #editmenu starts---------
    EditMenu=Menu(Menubar,tearoff=0)
    #feature of cut, copy ,paste
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    Menubar.add_cascade(label="Edit",menu=EditMenu)
    #Editmenu ends---------

    #formatmenu and view menu are non functional
    #Formatmenu starts---------
    FormatMenu=Menu(Menubar,tearoff=0)
    FormatMenu.add_command(label="Wordwrap")
    FormatMenu.add_command(label="Font")
    Menubar.add_cascade(label="Format",menu=FormatMenu)
    #Formatmenu ends---------

    #formatmenu and view menu are non functional
    #Viewmenu starts---------
    ViewMenu=Menu(Menubar,tearoff=0)
    ViewMenu.add_command(label="Zoom")
    ViewMenu.add_command(label="Status Bar")
    Menubar.add_cascade(label="View",menu=ViewMenu)
    #Viewmenu ends---------

    #helpmenu starts---------
    HelpMenu=Menu(Menubar,tearoff=0)
    #feature of help
    HelpMenu.add_command(label="About Notepad",command=about)
    Menubar.add_cascade(label="Help",menu=HelpMenu)
    #help menu ends---------------
    root.config(menu=Menubar)

    #adding scroll bar
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    #scrollbar ends
    #footer
    Label(root,text=" copyright @Nauman 15/06/23 ").pack(side=BOTTOM)
    # root.mainloop()
root.mainloop()
