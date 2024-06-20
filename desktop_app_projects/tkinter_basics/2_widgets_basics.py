from tkinter import *

# command functions for widgets
def display():
    data = entry.get()
    print(f"Button clicked. Data is {data}")

root = Tk()
root.geometry("300x300")

# Entry(user input) widget
entry = Entry()
entry.pack()

# Button widget
button = Button(root, text="click here", command=display)
button.pack()

root.mainloop()