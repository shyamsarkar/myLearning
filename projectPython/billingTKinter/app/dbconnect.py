import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

class SimpleSQLiteDB:
    def __init__(self, db_name='example.db'):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self._connect()

    def _connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def _commit_and_close(self):
        self.connection.commit()
        self.connection.close()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        self._commit_and_close()

    def insert_record(self, username, email):
        self.cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
        self._commit_and_close()

    def fetch_records(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        self._commit_and_close()
        return rows

    def delete_record(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        self._commit_and_close()

# Example Usage:

# Create an instance of the SimpleSQLiteDB class
db = SimpleSQLiteDB()

# Create the 'users' table
db.create_table()

# Insert a record
db.insert_record('john_doe', 'john@example.com')

# Fetch all records
records = db.fetch_records()
print("Records:", records)

# Delete a record (Assuming 'id' is the primary key)
db.delete_record(1)
