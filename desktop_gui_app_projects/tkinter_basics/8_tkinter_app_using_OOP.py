from tkinter import *

class Demo:

    def __init__(self, rootone):

        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame, text="Click Here", command=self.printmessage)
        self.printbutton.pack()

        self.quitbutton = Button(frame, text="Quit", command=frame.quit)
        self.quitbutton.pack()

    def printmessage(self):
        print("Button clicked!")

root = Tk()

d = Demo(root)

root.mainloop()
