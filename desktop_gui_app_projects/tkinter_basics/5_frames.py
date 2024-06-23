# fram widget allow us to organize the layout of other widgets like a container

from tkinter import *

root = Tk()
root.geometry("300x300")

frame1 = Frame(root, highlightthickness=1, highlightbackground="black", padx="60", pady="60")
frame1.pack()

frame2 = Frame(root)
frame2.pack(side=BOTTOM)

button1 = Button(frame1, text="Button 1")
button2 = Button(frame2, text="Button 2")

button1.pack()
button2.pack()


root.mainloop()