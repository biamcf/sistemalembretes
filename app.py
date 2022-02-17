from cgitb import text
from tkinter import *
from black import Line
from reminders import  reminders

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.container1 = Frame(master)
        self.container1.grid(column=0, row=0,sticky=(N, S, E, W))

        self.label_id = Label(self.container1, text='Search for the ID:')
        self.label_id.grid(column=0, row=0, sticky=(N, S, E, W))

        self.input_id = Entry(self.container1)
        self.input_id.grid(column=1, row=0, sticky=(E, W))

        self.button_search_id = Button(self.container1, text='Search')
        self.button_search_id['command'] = self.search_reminder()
        self.button_search_id.grid(column=3, row=0, sticky=(N, S , E, W))

        self.label_date = Label(self.container1, text='Date:')
        self.label_date.grid(column=0, row=1, sticky=(N, S, E, W))

        self.input_date = Entry(self.container1)
        self.input_date.grid(column=1, row=1, sticky=(E, W))

        self.label_reminder = Label(self.container1, text='Reminder:')
        self.label_reminder.grid(column=0, row=2, sticky=(N, S, E, W))

        self.input_reminder = Entry(self.container1)
        self.input_reminder.grid(column=1, row=2, sticky=(E, W))

        self.label_concluded = Label(self.container1, text='Did you complete this reminder? ')
        self.label_concluded.grid(column=0, row=3, sticky=(N, S, E, W))

        self.concluded = StringVar()
        self.concluded.set('No')

        concluded_option = Radiobutton(self.container1, text='Yes', variable=self.concluded, value='Yes')
        not_completed_option = Radiobutton(self.container1, text='No', variable=self.concluded, value='No')

        concluded_option.grid(column=1, row=3, sticky=(W))
        not_completed_option.grid(column=1, row=3, sticky=(E))

        insert_button = Button(self.container1, text='Insert')
        insert_button['command'] = self.insert_reminder()
        insert_button.grid(column=0, row=4, sticky=(W))

        update_button = Button(self.container1, text='Update')
        update_button['command'] = self.update_reminder()
        update_button.grid(column=0, row=4, sticky=(E))

        delete_button = Button(self.container1, text='Delete')
        delete_button['command'] = self.delete_reminder()
        delete_button.grid(column=1, row=4, sticky=(E))

        list_reminders_button = Button(self.container1, text='List all reminders')
        list_reminders_button.grid(column=0, row=5, sticky=(N, S, E, W))

        for child in self.container1.winfo_children(): 
            child.grid_configure(padx=3, pady=3)

    def insert_reminder(self):
        reminder = reminders()

        reminder.date_reminder = self.input_date.get()
        reminder.text_reminder = self.input_reminder.get()
        reminder.status_reminder = self.concluded.get()

        self.lblmsg['text'] = reminder.insert_reminder()

        self.input_date.delete(0, END)
        self.input_reminder.delete(0, END)
        self.concluded = 'No'

    def search_reminder(self):
        reminder = reminders()

        id_reminder = self.input_id.get()

        self.lblmsg['text'] = reminder.search_reminder(id_reminder)

        self.input_id.delete(0, END)
        self.input_id.insert(INSERT, reminder.id_reminder)

        self.input_date.delete(0, END)
        self.input_date.insert(INSERT, reminder.date_reminder)

    def update_reminder(self):
        reminder = reminders()

        reminder.id_reminder = self.input_id.get()
        reminder.date_reminder = self.input_date.get()
        reminder.status_reminder = self.concluded.get()
        reminder.text_reminder = self.input_reminder.get()

        self.lblmsg['text'] = reminder.update_reminder()

        self.input_id.delete(0, END)
        self.input_date.delete(0, END)
        self.input_reminder.delete(0, END)
        self.concluded.set('No')

    def delete_reminder(self):
        reminder = reminders()

        reminder.id_reminder = self.input_id.get()

        self.lblmsg['text'] = reminder.delete_reminder()

        self.input_id.delete(0, END)
        self.input_date.delete(0, END)
        self.input_reminder.delete(0, END)
        self.concluded.set('No')
        
root = Tk()
root.title('Lembretes')
root.call('wm', 'iconphoto', root._w, PhotoImage(file='notebook.png'))
myApp = Application(root)
myApp.mainloop()