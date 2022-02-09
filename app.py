from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)

root = Tk()
myApp = Application(root)
myApp.mainloop()