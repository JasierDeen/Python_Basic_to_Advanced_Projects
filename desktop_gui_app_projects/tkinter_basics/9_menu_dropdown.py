from tkinter import *

def func():
    print("Menu item clicked")

root = Tk()
root.geometry("300x300")

my_menu = Menu(root)
root.config(menu=my_menu)

sub_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=sub_menu)

sub_menu.add_command(label="Project", command=func)
sub_menu.add_command(label="Save", command=func)

root.mainloop()