from database import Database

class reminder(object):
    def __init__(self, id_reminder = 0, date_reminder = '', text_reminder = '', status_reminder = ''):
        self.info = {}
        self.id_reminder = id_reminder
        self.date_reminder = date_reminder
        self.text_reminder = text_reminder
        self.status_reminder = status_reminder

    def insert_reminder(self):
        db = Database()

        try:
            c = db.connection.cursor()
            c.execute("""
    INSERT INTO contacts (date_reminder, text_reminder, status_reminder) VALUES (?, ?, ?)""",
    (self.name, self.number, self.email))

            db.connection.commit()
            c.close()
            return 'reminder successfully registered.'
        except:
            return 'Reminder record error.'

    def update_reminder(self):
        db = Database()

        try:
            c = db.connection.cursor()
            c.execute("""
            UPDATE contacts
            SET name = (?), number = (?), email = (?)
            WHERE id = (?)""",
        (self.name, self.number, self.email, self.idContact))

            db.connection.commit()
            c.close()

            return 'Reminder update successfully registered.'
        except:
            return 'Error updating reminder.'

    def delete_reminder(self):
        db = Database()

        try:
            c = db.connection.cursor()
            c.execute("""DELETE FROM reminders WHERE id = (?)""", (self.id_reminder))
            db.connection.commit()
            c.close()
            return 'Reminder successfully deleted.'
        except:
            return 'Error deleting reminder.'

    def search_reminder(self):
        db = Database()

        try:
            c = db.connection.cursor()
            c.execute("""
        SELECT * FROM contacts WHERE id=?;
        """, (self.id_reminder))

            for row in c.fetchall():
                self.date_reminder = row[1]
                self.text_reminder = row[2]
                self.status_reminder = row[3]

            return 'Reminder search performed successfully.'
        except:
            return 'Reminder search error.'



