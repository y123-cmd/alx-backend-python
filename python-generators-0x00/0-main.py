#!/usr/bin/env python3

import seed

connection = seed.connect_db()
if connection:
    print("Connection successful")
    seed.create_table(connection)
    seed.insert_data(connection, 'user_data.csv')

    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user_data';")
    if cursor.fetchone():
        print("Database and table are ready")

    cursor.execute("SELECT * FROM user_data LIMIT 5;")
    print(cursor.fetchall())
    cursor.close()
    connection.close()
