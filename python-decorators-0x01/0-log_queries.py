import sqlite3
import functools
from datetime import datetime


def log_queries():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            query = kwargs.get('query') or (args[0] if args else None)
            if query:
                print(f"Executing SQL query: {query}")
            else:
                print("No SQL query found.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_queries()
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


users = fetch_all_users(query="SELECT * FROM users")
