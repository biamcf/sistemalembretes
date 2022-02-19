from cgitb import text
from tkinter import *
from reminders import reminders

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.container1 = Frame(master)
        self.container1.grid(column=0, row=0,sticky=(N, S, E, W))

        # self.label_id = Label(self.container1, text='Search for the ID:')
        # self.label_id.grid(column=0, row=0, sticky=(N, S, E, W))

        # self.input_id = Entry(self.container1)
        # self.input_id.grid(column=1, row=0, sticky=(E, W))

        # self.button_search_id = Button(self.container1, text='Search')
        # self.button_search_id['command'] = self.search_reminder()
        # self.button_search_id.grid(column=3, row=0, sticky=(N, S , E, W))

        # self.label_date = Label(self.container1, text='Date:')
        # self.label_date.grid(column=0, row=1, sticky=(N, S, E, W))

        # self.input_date = Entry(self.container1)
        # self.input_date.grid(column=1, row=1, sticky=(E, W))

        # self.label_reminder = Label(self.container1, text='Reminder:')
        # self.label_reminder.grid(column=0, row=2, sticky=(N, S, E, W))

        # self.input_reminder = Entry(self.container1)
        # self.input_reminder.grid(column=1, row=2, sticky=(E, W))

        # self.label_concluded = Label(self.container1, text='Did you complete this reminder? ')
        # self.label_concluded.grid(column=0, row=3, sticky=(N, S, E, W))

        # self.concluded = StringVar()
        # self.concluded.set('No')

        # self.concluded_option = Radiobutton(
        #   self.container1, 
        #   text='Yes', 
        #   variable=self.concluded, 
        #   value='Yes')
        # self.not_completed_option = Radiobutton(
        #   self.container1, 
        #   text='No', 
        #   variable=self.concluded, 
        #   value='No')

        # self.concluded_option.grid(column=1, row=3, sticky=(W))
        # self.not_completed_option.grid(column=1, row=3, sticky=(E))

        self.insert_button = Button(self.container1, text='Insert')
        self.insert_button['command'] = self.insert_reminder()
        self.insert_button.grid(column=0, row=4, sticky=(W))

        # self.update_button = Button(self.container1, text='Update')
        # self.update_button['command'] = self.update_reminder()
        # self.update_button.grid(column=0, row=4, sticky=(E))

        # self.delete_button = Button(self.container1, text='Delete')
        # self.delete_button['command'] = self.delete_reminder()
        # self.delete_button.grid(column=1, row=4, sticky=(E))

        # self.list_reminders_button = Button(self.container1, text='List all reminders')
        # self.list_reminders_button.grid(column=0, row=5, sticky=(N, S, E, W))

        self.labelResult = Label(self.container1, text="where am I???")
        self.labelResult.grid(column=0, row=6)

        for child in self.container1.winfo_children(): 
            child.grid_configure(padx=3, pady=3)
            

    def insert_reminder(self):
        reminder = reminders()

        # reminder.date_reminder = self.input_date.get()
        # reminder.text_reminder = self.input_reminder.get()
        # reminder.status_reminder = self.concluded.get()

        result = reminder.insert_reminder()

        self.labelResult["text"] = "aksjska"

        self.input_date.delete(0, END)
        self.input_reminder.delete(0, END)
        self.concluded = 'No'

    def search_reminder(self):
      pass
        # reminder = reminders()

        # reminder.id_reminder = self.input_id.get()

        # self.lblmsg['text'] = reminder.search_reminder()

        # self.input_id.delete(0, END)
        # self.input_id.insert(INSERT, reminder.id_reminder)

        # self.input_date.delete(0, END)
        # self.input_date.insert(INSERT, reminder.date_reminder)

    def update_reminder(self):
      pass
        # reminder = reminders()

        # reminder.id_reminder = self.input_id.get()
        # reminder.date_reminder = self.input_date.get()
        # reminder.status_reminder = self.concluded.get()
        # reminder.text_reminder = self.input_reminder.get()

        # self.lblmsg['text'] = reminder.update_reminder()

        # self.input_id.delete(0, END)
        # self.input_date.delete(0, END)
        # self.input_reminder.delete(0, END)
        # self.concluded.set('No')

    def delete_reminder(self):
      pass
        # reminder = reminders()

        # reminder.id_reminder = self.input_id.get()

        # self.lblmsg['text'] = reminder.delete_reminder()

        # self.input_id.delete(0, END)
        # self.input_date.delete(0, END)
        # self.input_reminder.delete(0, END)
        # self.concluded.set('No')
        
root = Tk()
root.title('Lembretes')
root.call('wm', 'iconphoto', root._w, PhotoImage(file='notebook.png'))

myApp = Application(root)
myApp.mainloop()