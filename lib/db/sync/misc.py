import sqlite3

def connect(db_path):
    return sqlite3.connect(db_path)
