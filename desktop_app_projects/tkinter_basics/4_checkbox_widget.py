from tkinter import *

# command functions for check_buton widget
def selected():
    selection.config(text=check_value.get())

root = Tk()
root.geometry("300x300")

# Check box/check button widget
check_value =BooleanVar()
check_button = Checkbutton(root, text="Accept terms", variable=check_value, command=selected)
check_button.pack()

# Label widget for showing check_button slection
selection = Label(root)
selection.pack()

root.mainloop()