import sqlite3
import bcrypt

salt = "fhaf!jg(%6394regGHUGTgs3029gfjhgG"

class Database:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            login TEXT NOT NULL,
                            password TEXT NOT NULL
                        )
                    ''')
            conn.commit()

    def new_user(self, login: str, password: str):
        encrypted_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                        INSERT INTO users (login, password) VALUES (?, ?)
                    ''', (login, encrypted_password))
            conn.commit()



