from tkinter import *

root = Tk()
root.geometry("300x300")
hello = Label(root, text="Hello World! This is first desktop app.", fg="green", bg="black", font=("Arial", 12))
hello.pack()

root.mainloop()