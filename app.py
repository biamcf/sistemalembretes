from cgitb import text
from tkinter import *
from black import Line

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.container1 = Frame(master)
        self.container1.grid(column=0, row=0,sticky=(N, S, E, W))

        self.label_id = Label(self.container1, text="Search for the ID:")
        self.label_id.grid(column=0, row=0, sticky=(N, S, E, W))

        self.input_id = Entry(self.container1)
        self.input_id.grid(column=1, row=0, sticky=(E, W))

        self.button_search_id = Button(self.container1, text="Search")
        self.button_search_id["command"] = self.search_id
        self.button_search_id.grid(column=3, row=0, sticky=(N, S , E, W))

        self.label_date = Label(self.container1, text="Date:")
        self.label_date.grid(column=0, row=1, sticky=(N, S, E, W))

        self.input_date = Entry(self.container1)
        self.input_date.grid(column=1, row=1, sticky=(E, W))

        self.label_reminder = Label(self.container1, text="Reminder:")
        self.label_reminder.grid(column=0, row=2, sticky=(N, S, E, W))

        self.input_reminder = Entry(self.container1)
        self.input_reminder.grid(column=1, row=2, sticky=(E, W))

        self.label_concluded = Label(self.container1, text="Did you complete this reminder? ")
        self.label_concluded.grid(column=0, row=3, sticky=(N, S, E, W))

        self.concluded = StringVar()
        self.concluded.set("No")

        concluded_option = Radiobutton(self.container1, text="Yes", variable=self.concluded, value="Yes")
        not_completed_option = Radiobutton(self.container1, text="No", variable=self.concluded, value="No")

        concluded_option.grid(column=1, row=3, sticky=(W))
        not_completed_option.grid(column=1, row=3, sticky=(E))

        for child in self.container1.winfo_children(): 
            child.grid_configure(padx=3, pady=3)

    def search_id(self):
        pass
        
root = Tk()
root.title("Lembretes")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='notebook.png'))
myApp = Application(root)
myApp.mainloop()