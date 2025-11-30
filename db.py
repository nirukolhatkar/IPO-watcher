import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def init_db():
    """ initialize the database with the IPOs table """
    conn = create_connection("ipos.db")
    if conn:
        create_table_sql = """CREATE TABLE IF NOT EXISTS ipos (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                date TEXT NOT NULL,
                                price_range TEXT,
                                notifications TEXT
                            );"""
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

def upsert_ipo(name, date, price_range, notifications):
    """ upsert an IPO into the database """
    conn = create_connection("ipos.db")
    if conn:
        upsert_sql = """INSERT INTO ipos (name, date, price_range, notifications) 
                        VALUES (?, ?, ?, ?)
                        ON CONFLICT(name) DO UPDATE SET 
                        date=excluded.date,
                        price_range=excluded.price_range,
                        notifications=excluded.notifications;"""
        try:
            c = conn.cursor()
            c.execute(upsert_sql, (name, date, price_range, notifications))
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

def get_ipo(name):
    """ get an IPO by name """
    conn = create_connection("ipos.db")
    if conn:
        query_sql = "SELECT * FROM ipos WHERE name=?;"
        try:
            c = conn.cursor()
            c.execute(query_sql, (name,))
            ipo = c.fetchone()
            return ipo
        except Error as e:
            print(e)
        finally:
            conn.close()
    return None
