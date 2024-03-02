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



class Institutes(Database):
    def __init__(self):
        super().__init__()
        self.cur.execute("""
                            CREATE TABLE IF NOT EXISTS "Institutes"  (
	                        "id"	INTEGER NOT NULL,
	                        "Name"	TEXT,
	                        "Description"	TEXT,
	                        PRIMARY KEY("id" AUTOINCREMENT)
                            );""")
        self.db.commit()


    def get_names(self):
        data = self.cur.execute("SELECT Name FROM Institutes").fetchall()
        return data

    def get_ids(self):
        data = self.cur.execute("SELECT id FROM Institutes").fetchall()
        return data


class Directions(Database):
    def __init__(self):
        super().__init__()
        self.cur.execute("""
                            CREATE TABLE IF NOT EXISTS "Directions" (
                                "id"	INTEGER NOT NULL,
                                "name"	TEXT,
                                "institute_id"	INTEGER NOT NULL,
                                "description"	INTEGER,
                                "price"	INTEGER,
                                FOREIGN KEY("institute_id") REFERENCES "Institutes"("id"),
                                PRIMARY KEY("id" AUTOINCREMENT)
                        );""")
        self.db.commit()

    def get_names_by_institute(self, institute_id):
        data = self.cur.execute("SELECT NAME FROM Directions WHERE institute_id = ?", (institute_id,)).fetchall()
        return data

    def get_ids(self):
        data = self.cur.execute("SELECT id FROM Directions").fetchall()
        return data





class Focus(Database):
    def __init__(self):
        super().__init__()
        self.cur.execute("""
                            CREATE TABLE IF NOT EXISTS "Focus" (
                                "id"	INTEGER NOT NULL,
                                "name"	TEXT,
                                "direction_id"	TEXT NOT NULL,
                                "description"	TEXT,
                                "specification"	TEXT,
                                "learning_plan"	TEXT,
                                "calendar_schedule"	TEXT,
                                "documents"	TEXT,
                                "passing_points"	INT,
                                FOREIGN KEY("direction_id") REFERENCES "Directions"("id"),
                                PRIMARY KEY("id" AUTOINCREMENT)
                            );""")
        self.db.commit()


    def get_names_by_direction(self, direction_id):
        data = self.cur.execute("SELECT name FROM Focus WHERE direction_id = ?", (direction_id)).fetchall()
        return data