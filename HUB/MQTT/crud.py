import sqlite3 
from Application import Application

class Crud:
    
    def __init__(self, db_file):

        self.conn = self.create_connection(db_file)
        
        self.create_table("""CREATE TABLE IF NOT EXISTS app (
                                id integer PRIMARY KEY,
                                topic text NOT NULL
                            );""")
        self.create_table("""CREATE TABLE IF NOT EXISTS object (
                                id integer PRIMARY KEY,
                                topic text NOT NULL
                            );""")


    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Exception as e:
            print(e)
            return conn

    def create_table(self, create_table_sql):
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Exception as e:
            print(e)

    def insert_db(self, table, column, value):
        try:
            c = self.conn.cursor()
            c.execute("INSERT INTO {} ({}) VALUES (?)".format(table, column), (value,))
            self.conn.commit()
        except Exception as e:
            print(e)
    
    def select_all_app(self):
        try:
            c = self.conn.cursor()
            c.execute("SELECT topic FROM app")
            rows = c.fetchall()

            for row in rows:
                Application.APPLICATIONS.append(row)

        except Exception as e:
            print(e)
    
    def select_all_obj(self):
        try:
            c = self.conn.cursor()
            c.execute("SELECT topic FROM object")
            rows = c.fetchall()

            return rows

        except Exception as e:
            print(e)
