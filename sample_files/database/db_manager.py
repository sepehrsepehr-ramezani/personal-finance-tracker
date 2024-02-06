from jdatetime import datetime
import sqlite3

class Database:
    def __init__(self, db_name):
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%B")
        print(f"usrs/{db_name}/{year}/{month}")
        self.conn = sqlite3.connect(f"usrs/{db_name}/{year}/{month}/database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS expense(
                            date TEXT,
                            text TEXT,
                            amount BIGINT
        );""")
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS income(
                            date TEXT,
                            text TEXT,
                            amount BIGINT
        );""")
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS cash_income(
                            date TEXT,
                            text TEXT,
                            amount BIGINT
        );""")
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS cash_expense(
                            date TEXT,
                            text TEXT,
                            amount BIGINT
        );""")
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS cash_withdrawal(
                            date TEXT,
                            text TEXT,
                            amount BIGINT
        );""")

    def store_data(self, table_name, date, text, amount):
        print(table_name, date, text,amount)
        self.cursor.execute(f"INSERT INTO {table_name} VALUES(?,?,?)", [date, text, amount])
        self.conn.commit()
    
    def read_data(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        abc = self.cursor.fetchall()
        return abc
    
    def __delete__(self):
        self.conn.close()