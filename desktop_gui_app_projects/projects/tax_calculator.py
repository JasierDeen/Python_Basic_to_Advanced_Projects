from tkinter import *

def tax_calculate():
    try:
        result = int(income.get()) * (int(percent.get())/100)
        tax.insert(0, result)
    except Exception:
        tax.insert(0, "Invalid Input")


root = Tk()
root.geometry("300x300")


income_label = Label(root, text="Income:")
income_label.pack()

income = Entry(root)
income.pack()

percent_label = Label(root, text="Percent:")
percent_label.pack()

percent = Entry(root)
percent.pack()

tax_label = Label(root, text="Tax:")
tax_label.pack()

tax = Entry(root)
tax.pack()

button = Button(root, text="Calculate", command=tax_calculate)
button.pack()

# # Label widget for showing result
# answer = Label(root)
# answer.pack()

root.mainloop()