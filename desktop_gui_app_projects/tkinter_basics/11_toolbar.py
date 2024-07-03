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

status = Label(text="This is the current status", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# Tool bar
tool_bar = Frame(root, bg="green")

insert_button = Button(tool_bar, text="Insert File", command=func)
delete_button = Button(tool_bar, text="Delete File", command=func)

insert_button.pack(side=LEFT, padx=2, pady=3)
delete_button.pack(side=LEFT, padx=2, pady=3)
tool_bar.pack()

root.mainloop()
