from tkinter import *

# command functions for button widget
def add():
    result = int(number_1.get()) + int(number_2.get())
    answer.config(text=f"Answer is: {str(result)}")

root = Tk()
root.geometry("300x300")

# Entry(user input) number_1 widget
number_1 = Entry(root)
number_1.pack()

# Entry(user input) number_2 widget
number_2 = Entry(root)
number_2.pack()

# Button widget
button = Button(root, text="add", command=add)
button.pack()

# Label widget for showing result
answer = Label(root)
answer.pack()

root.mainloop()