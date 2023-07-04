from tkinter import *
root=Tk()
root.title("My Notebook")
canvas_width=450
canvas_heigth=520
root.geometry(f"{canvas_width}x{canvas_heigth}")

can_widget=Canvas(root,width=canvas_width,height=canvas_heigth)
can_widget.pack()

# co ordinates x1 y1 x2 y2
can_widget.create_line(0,70, 450, 70,fill="pink")
can_widget.create_line(0,67, 450, 67,fill="pink")
can_widget.create_line(45,0, 45, 650,fill="pink")
can_widget.create_line(48,0, 48, 650,fill="pink")

for i in range(85,505,15):
    can_widget.create_line(0,i, 450, i)



# can_widget.create_line(0,85, 450, 85)
# can_widget.create_line(0,100, 450, 100)
# can_widget.create_line(0,115, 450, 115)
# can_widget.create_line(0,130, 450, 130)
# can_widget.create_line(0,145, 450, 145)
# can_widget.create_line(0,160, 450, 160)
# can_widget.create_line(0,175, 450, 175)
# can_widget.create_line(0,190, 450, 190)
# can_widget.create_line(0,205, 450, 205)
# can_widget.create_line(0,220, 450, 220)
# can_widget.create_line(0,235, 450, 235)
# can_widget.create_line(0,250, 450, 250)
# can_widget.create_line(0,265, 450, 265)
# can_widget.create_line(0,280, 450, 280)
# can_widget.create_line(0,295, 450, 295)
# can_widget.create_line(0,310, 450, 310)
# can_widget.create_line(0,325, 450, 325)
# can_widget.create_line(0,340, 450, 340)
# can_widget.create_line(0,355, 450, 355)
# can_widget.create_line(0,370, 450, 370)
# can_widget.create_line(0,385, 450, 385)
# can_widget.create_line(0,400, 450, 400)
# can_widget.create_line(0,415, 450, 415)
# can_widget.create_line(0,430, 450, 430)
# can_widget.create_line(0,445, 450, 445)
# can_widget.create_line(0,460, 450, 460)
# can_widget.create_line(0,475, 450, 475)
# can_widget.create_line(0,490, 450, 490)
# can_widget.create_line(0,505, 450, 505)

#text starting point declaration
can_widget.create_text( 80,79, text="Repent",font=("Times new roman",13, "bold"))
#rectangle(starting pt top left x,starting pt top left y,breadth,height )
can_widget.create_rectangle( 80, 110,300,200,fill="white")
#oval(top left x,top left y,bottom right x , bottom right y)
can_widget.create_oval(80,230,320,350,fill="blue")

root.mainloop()