# grid layout manager places widget side by side whereas pack simply stacks the widget
from tkinter import *

root =Tk()
root.geometry("300x300")

email_label = Label(root, text="Email")
password_label = Label(root, text="Password")

email_value = Entry(root)
password_value = Entry(root)

email_label.grid(row=0, column=0)
email_value.grid(row=0, column=1)

password_label.grid(row=1, column=0)
password_value.grid(row=1, column=1)

login_button = Button(root, text="Login")
login_button.grid(row=2, column=1)

root.mainloop()