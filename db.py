import sqlite3

class Database():
    def __init__(self):
        self.db = sqlite3.connect('botDB.sqlite3')
        self.cur = self.db.cursor()





class EnterCalendar(Database):
    def __init__(self):
        super().__init__()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS enterCalendar(
                                                                            id INTEGER PRIMARY KEY,
                                                                            form TEXT,
                                                                            date TEXT,
                                                                            description TEXT
                                                                            )
                                """)
        self.db.commit()

    def get_budget(self):
        data = self.cur.execute("SELECT date, description  FROM enterCalendar WHERE form=?", ("buget", )).fetchall()
        return data

    def get_contract(self):
        data = self.cur.execute("SELECT date, description  FROM enterCalendar WHERE form=?", ("contract", )).fetchall()
        return data

    def get_kvot(self):
        data = self.cur.execute("SELECT date, description  FROM enterCalendar WHERE form=?", ("kvot", )).fetchall()
        return data

