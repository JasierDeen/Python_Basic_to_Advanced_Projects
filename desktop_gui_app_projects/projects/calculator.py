from tkinter import *
import ast

root = Tk()

i = 0
def get_number(num):
    global i
    display.insert(i, num)
    i+=1

def get_operation(operator):
    global i 
    display.insert(i, operator)
    i+=len(operator)

def clear_all():
    display.delete(0, END)


def calculate():
    entire_string = display.get()
    try:
        node = ast.parse(entire_string, mode="eval")
        result = eval(compile(node, "<string>", "eval"))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "")


display = Entry(root)
display.grid(row=1, columnspan=6)

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
counter=0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text=button_text, width=4, height=2, command=lambda text=button_text:get_number(text))
        button.grid(row=x+2, column=y)
        counter+=1
        
button = Button(root, text="0", width=4, height=2, command=lambda :get_number(0))
button.grid(row=5, column=1)

operations = ["+", "-", "*", "/", "*3.14", "%", "(", "**", ")", "**2"]
count = 0
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button_text = operations[count]
            button = Button(root, text=button_text, width=4, height=2, command=lambda operator=button_text:get_operation(operator))
            count+=1
            button.grid(row=x+2, column=y+3)

Button(root, text="AC", width=4, height=2, command=clear_all).grid(row=5, column=0)
Button(root, text="=", width=4, height=2, command=calculate).grid(row=5, column=2)
Button(root, text="<-", width=4, height=2, command=lambda :undo()).grid(row=5, column=2)
root.mainloop()