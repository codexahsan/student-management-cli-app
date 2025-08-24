import sqlite3


# Setting Up DataBase


db_name = "students.db"

def connect_db():       #connect to db
    return sqlite3.connect(db_name)


def init_db():
    conn = connect_db()   #creates a db file if not exists
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   age INTEGER NOT NULL,
                   grade TEXT NOT NULL
                   )
''')
    conn.commit()
    conn.close()
