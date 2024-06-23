from tkinter import *

def selected():
    sugar = "Sugar" if sugar_value.get() else "No sugar"
    ice = "Ice" if ice_value.get() else "No Ice"
    cream = "Cream" if cream_value.get() else "No cream"

    label.config(text=f"Options selected are: {sugar}, {ice} & {cream}")


root = Tk()
root.geometry("300x300")

sugar_value = BooleanVar()
ice_value = BooleanVar()
cream_value = BooleanVar()

sugar_checkbox = Checkbutton(root, text="Sugar", variable=sugar_value, command=selected)
ice_checkbox = Checkbutton(root, text="Ice", variable=ice_value, command=selected)
cream_checkbox = Checkbutton(root, text="Cream", variable=cream_value, command=selected)

label = Label(root)

sugar_checkbox.pack()
ice_checkbox.pack()
cream_checkbox.pack()
label.pack()

root.mainloop()