from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("300x300")

# tkinter.messagebox.showinfo("Title", "This is a message box")\

response = tkinter.messagebox.askquestion("Question1", "Do you like coffee?")

if response == "yes":
    print("Here is a coffee for you")

root.mainloop()
