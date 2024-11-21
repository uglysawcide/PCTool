import sqlite3
import bcrypt


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
                            password TEXT NOT NULL,
                            salt TEXT NOT NULL,
                            is_login INTEGER NOT NULL
                        )
                    ''')
            conn.commit()

    def register(self, login: str, password: str):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            user = cursor.execute("""
                SELECT login FROM users WHERE login = ?
            """, (login,)).fetchone()
            if user:
                return False
            salt = bcrypt.gensalt()
            encrypted_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            cursor.execute('''
                        INSERT INTO users (login, password, salt, is_login) VALUES (?, ?, ?, 1)
                    ''', (login, encrypted_password, salt.decode('utf-8')))
            conn.commit()
            return user

    def login(self, login: str, password: str):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            salt = cursor.execute(
                """
                    SELECT salt FROM users WHERE login = ?
                    """, (login,)).fetchone()
            if not salt:
                return False
            encrypted_password = bcrypt.hashpw(password.encode('utf-8'), salt[0].encode('utf-8'))
            user = cursor.execute(
                '''
                        SELECT login FROM users WHERE login = ? AND password = ?
                    ''', (login, encrypted_password)).fetchone()
            if not user:
                return False
            cursor.execute("""
                            UPDATE users SET is_login = 1 WHERE login = ?
                        """, (login,))
            conn.commit()
            return user

    def unlogin(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            user = cursor.execute("""
                UPDATE users SET is_login = 0 WHERE is_login = 1
            """).fetchone()
            conn.commit()
