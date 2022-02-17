import sqlite3

class Database():
  def __init__(self):
    self.connection = sqlite3.connect("data_base.db")
    self.create_table()

  def create_table(self):
    c = self.connection.cursor()

    c.execute("""
      CREATE TABLE IF NOT EXISTS reminders (
          id_reminder INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          date_reminder TEXT NOT NULL,
          text_reminder TEXT NOT NULL,
          status_reminder TEXT NOT NULL
      );
    """)
    self.connection.commit()

    c.close()