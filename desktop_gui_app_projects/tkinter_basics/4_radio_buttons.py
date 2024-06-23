from tkinter import *

def selected():
    label.config(text=f"Choice of fuel is: {fuel.get()}")

root = Tk()
root.geometry("300x300")

fuel = StringVar(value="Petrol")

# Radio Button widgets
radio1 = Radiobutton(root, text="Petrol", variable=fuel, value="Petrol", command=selected)
radio2 = Radiobutton(root, text="Diesel", variable=fuel, value="Diesel", command=selected)
radio3 = Radiobutton(root, text="Electric", variable=fuel, value="Electric", command=selected)

label = Label(root)

radio1.pack()
radio2.pack()
radio3.pack()
label.pack()

root.mainloop()